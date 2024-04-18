import json
import logging
import os
import shutil
import subprocess
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple
from urllib.parse import urljoin
from mkdocs.config import base, config_options as c
import pathspec
from mkdocs import utils as mkdocs_utils
from mkdocs.config import Config, config_options
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from watchdog.events import FileSystemEvent

from mkdocs_juvix.utils import (
    compute_hash_filepath,
    compute_sha_over_folder,
    fix_site_url,
    hash_file,
)

log: logging.Logger = logging.getLogger("mkdocs")


class JuvixPlugin(BasePlugin):

    mkconfig: MkDocsConfig

    juvix_md_files: List[Dict[str, Any]]
    site_dir: Optional[str]
    site_url: str
    ROOT_DIR: Path
    DOCS_DIR: Path
    CACHE_DIR: Path
    MARKDOWN_JUVIX_OUTPUT: Path

    JUVIX_ENABLED: bool = bool(os.environ.get("JUVIX_ENABLED", False))
    REMOVE_CACHE: bool = bool(os.environ.get("REMOVE_CACHE", False))
    JUVIX_AVAILABLE: bool = True

    JUVIX_VERSION: Optional[str]
    JUVIX_BIN: str = "juvix"
    JUVIXCODE_CACHE_DIR: Path
    JUVIXCODE_HASH_FILE: Path
    HASH_DIR: Path
    HTML_CACHE_DIR: Path
    FIRST_RUN: bool

    def create_cache_dirs(self):
        self.MARKDOWN_JUVIX_OUTPUT.mkdir(parents=True, exist_ok=True)
        self.JUVIXCODE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        self.HASH_DIR.mkdir(parents=True, exist_ok=True)
        self.HTML_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    def on_startup(self, command, dirty):
        return

    def on_config(self, config: MkDocsConfig, **kwargs) -> MkDocsConfig:

        config_file = config.config_file_path

        self.ROOT_DIR = Path(config_file).parent.absolute()

        self.DOCS_DIR: Path = self.ROOT_DIR / "docs"
        self.CACHE_DIR: Path = self.ROOT_DIR / ".hooks"
        self.MARKDOWN_JUVIX_OUTPUT: Path = self.CACHE_DIR / ".md"

        self.JUVIX_VERSION: Optional[str] = None
        self.JUVIXCODE_CACHE_DIR: Path = self.CACHE_DIR / ".juvix_md"
        self.JUVIXCODE_HASH_FILE = self.CACHE_DIR / ".hash_juvix_md"
        self.HASH_DIR: Path = self.CACHE_DIR / ".hash"
        self.HTML_CACHE_DIR: Path = self.CACHE_DIR / ".html"
        self.FIRST_RUN = True

        self.JUVIX_AVAILABLE = shutil.which(self.JUVIX_BIN) is not None

        if self.JUVIX_ENABLED:

            if self.JUVIX_AVAILABLE:
                cmd = [self.JUVIX_BIN, "--numeric-version"]
                result = subprocess.run(cmd, capture_output=True)
                if result.returncode == 0:
                    JUVIX_VERSION = result.stdout.decode("utf-8")
                    log.info(
                        f"Using Juvix v{JUVIX_VERSION} to render Juvix Markdown files."
                    )

            try:
                subprocess.run([self.JUVIX_BIN, "--version"], capture_output=True)
            except FileNotFoundError:
                log.warning(
                    "The Juvix binary is not available. Please install Juvix and make sure it's available in the PATH."
                )

        if self.REMOVE_CACHE:
            shutil.rmtree(self.CACHE_DIR, ignore_errors=True)
        self.create_cache_dirs()

        config = fix_site_url(config)

        self.mkconfig = config
        self.juvix_md_files: List[Dict[str, Any]] = []
        self.site_dir = config.get("site_dir", None)
        self.site_url = config.get("site_url", "")

        if not self.site_url.endswith("/"):
            self.site_url += "/"

        if not self.JUVIX_ENABLED:
            log.info("Juvix support is disabled. Set JUVIX_ENABLED to true to enable.")
        if not self.JUVIX_AVAILABLE:
            log.info(
                "Juvix is not available on the system. check the JUVIX_BIN environment variable."
            )
        return config

    def on_files(self, files: Files, *, config: MkDocsConfig) -> Optional[Files]:
        for file in files:
            if ".juvix-build" in file.abs_src_path:
                files.remove(file)
        return files

    def on_page_read_source(self, page: Page, config: MkDocsConfig) -> Optional[str]:
        filepath = Path(page.file.abs_src_path)
        return self.generate_markdown(filepath)

    def on_pre_build(self, config: MkDocsConfig) -> None:
        self.pre_build()

    def on_post_build(self, config: MkDocsConfig) -> None:
        self.post_build()

    def on_serve(self, server: Any, config: MkDocsConfig, builder: Any) -> None:

        gitignore = None

        with open(self.ROOT_DIR / ".gitignore") as file:
            gitignore = pathspec.PathSpec.from_lines(
                pathspec.patterns.GitWildMatchPattern, file  # type: ignore
            )

        def callback_wrapper(
            callback: Callable[[FileSystemEvent], None]
        ) -> Callable[[FileSystemEvent], None]:
            def wrapper(event: FileSystemEvent) -> None:
                if gitignore.match_file(
                    Path(event.src_path).relative_to(config.docs_dir).as_posix()
                ):
                    return
                fpath: Path = Path(event.src_path).absolute()
                fpathstr: str = fpath.as_posix()

                if ".juvix-build" in fpathstr:
                    return

                if fpathstr.endswith(".juvix.md"):
                    log.debug("Juvix file changed: %s", fpathstr)
                return callback(event)

            return wrapper

        handler = (
            next(
                handler
                for watch, handler in server.observer._handlers.items()
                if watch.path == config.docs_dir
            )
            .copy()
            .pop()
        )
        handler.on_any_event = callback_wrapper(handler.on_any_event)

    def on_page_markdown(
        self, markdown: str, page, config, files: Files
    ) -> Optional[str]:
        juvix = ".juvix"
        index = "index.juvix"
        readme = "README.juvix"

        def path_change(text):
            page.file.name = page.file.name.replace(text, "")
            page.file.url = page.file.url.replace(text, "")
            page.file.dest_uri = page.file.dest_uri.replace(text, "")
            page.file.abs_dest_path = page.file.abs_dest_path.replace(text, "")

            if not page.title:
                page.title = page.file.name

        if page.file.name == index:
            path_change(index)
        elif page.file.name == readme:
            path_change(readme)
        elif page.file.name.endswith(juvix):
            path_change(juvix)

        return markdown

    def move_html_cache_to_site_dir(self, filepath: Path, site_dir: Path) -> None:
        """
        Move the corresponding HTML output generated by Juvix for the given Juvix
        file to the site_dir, respecting the directory structure. It also takes into
        account that the Juvix html generation produces .html for the .juvix.md,
        which it is problematic, as it replaces the `juvix markdown` output, once
        the move to site takes place.
        """

        filepath = Path(filepath)
        if not filepath.name.endswith(".juvix.md"):
            return

        rel_path = filepath.relative_to(self.DOCS_DIR)

        dest_folder = site_dir.joinpath(rel_path.parent)
        dest_folder.mkdir(parents=True, exist_ok=True)

        for _file in self.JUVIXCODE_CACHE_DIR.rglob("*.juvix.md"):
            file = _file.absolute()
            path_rel_raw = file.relative_to(self.JUVIXCODE_CACHE_DIR)

            log.debug(f"move_html: file: {file}")
            if file.suffixes == [".juvix", ".md"]:
                filename = file.name

                log.debug(f"move_html: filename: {filename}")
                just_name = filename.replace(".juvix.md", "")
                html_file = just_name + ".html"
                html_file_path = self.HTML_CACHE_DIR / path_rel_raw.parent / html_file

                log.debug(f"move_html: html_file: {html_file_path}")
                if html_file_path.exists():
                    log.debug(f"move_html: removing file {html_file_path}")
                    html_file_path.unlink()

        index_file = self.HTML_CACHE_DIR.joinpath("index.html")

        if index_file.exists():
            index_file.unlink()

        log.debug(f"Copying folder: {self.HTML_CACHE_DIR} to {dest_folder}")
        shutil.copytree(self.HTML_CACHE_DIR, dest_folder, dirs_exist_ok=True)
        return

    def new_or_changed_or_no_exist(self, filepath: Path) -> bool:
        content_hash = hash_file(filepath)
        path_hash = compute_hash_filepath(filepath, hash_dir=self.HASH_DIR)
        if not path_hash.exists():
            log.debug(f"File: {filepath} does not have a hash file.")
            return True
        fresh_content_hash = path_hash.read_text()
        return content_hash != fresh_content_hash

    # ------------------ Juvix Preprocessor ------------------

    def pre_build(self) -> None:
        if self.FIRST_RUN:
            try:
                log.info("Updating Juvix dependencies...")
                subprocess.run(
                    [self.JUVIX_BIN, "dependencies", "update"], capture_output=True
                )
            except Exception as e:
                log.error(f"A problem occurred while updating Juvix dependencies: {e}")
                return

        log.info("Generating Markdown for all .juvix.md files.")
        for _file in self.DOCS_DIR.rglob("*.juvix.md"):
            file: Path = _file.absolute()

            relative_to: Path = file.relative_to(self.DOCS_DIR)

            url = urljoin(
                self.site_url, relative_to.as_posix().replace(".juvix.md", ".html")
            )

            self.juvix_md_files.append(
                {
                    "module_name": self.unqualified_module_name(file),
                    "qualified_module_name": self.qualified_module_name(file),
                    "url": url,
                    "file": file.absolute().as_posix(),
                }
            )
            self.generate_markdown(file)

        log.info("Computing SHA over Juvix content.")
        current_sha: str = compute_sha_over_folder(self.JUVIXCODE_CACHE_DIR)

        with open(self.JUVIXCODE_HASH_FILE, "w") as f:
            f.write(current_sha)

        if not self.FIRST_RUN:
            return

        log.info(
            "Generating auxiliary HTML for Juvix files. This may take a while... It's only generated once per session."
        )
        self.generate_html(generate=True, move_cache=True)

        self.juvix_md_files.sort(key=lambda x: x["qualified_module_name"])

        juvix_modules = self.CACHE_DIR.joinpath("juvix_modules.json")
        if juvix_modules.exists():
            juvix_modules.unlink()

        with open(juvix_modules, "w") as f:
            json.dump(self.juvix_md_files, f, indent=4)

        FIRST_RUN = False

    def generate_html(self, generate: bool = True, move_cache: bool = True) -> None:
        everythingJuvix = self.DOCS_DIR.joinpath("everything.juvix.md")

        if not everythingJuvix.exists():
            log.warning(
                "The file 'docs/everything.juvix.md' does not exist. It is recommended to create this file to avoid excessive builds."
            )

        files_to_process = (
            self.juvix_md_files
            if not everythingJuvix.exists()
            else [
                {
                    "file": everythingJuvix,
                    "module_name": self.unqualified_module_name(everythingJuvix),
                    "qualified_module_name": self.qualified_module_name(
                        everythingJuvix
                    ),
                    "url": urljoin(self.site_url, "everything.juvix.md").replace(
                        ".juvix.md", ".html"
                    ),
                }
            ]
        )

        for filepath_info in files_to_process:
            filepath = Path(filepath_info["file"])
            if generate:
                self.generate_html_per_file(filepath)
            if self.site_dir and move_cache:
                self.move_html_cache_to_site_dir(filepath, Path(self.site_dir))

    def generate_html_per_file(
        self, _filepath: Path, remove_cache: bool = False
    ) -> None:

        if remove_cache and self.HTML_CACHE_DIR.exists():
            log.debug(f"Removing folder: {self.HTML_CACHE_DIR}")
            shutil.rmtree(self.HTML_CACHE_DIR)

        self.HTML_CACHE_DIR.mkdir(parents=True, exist_ok=True)

        filepath = _filepath.absolute()

        cmd = (
            [self.JUVIX_BIN, "html"]
            + ["--strip-prefix=docs"]
            + ["--folder-structure"]
            + [f"--output-dir={self.HTML_CACHE_DIR.as_posix()}"]
            + [f"--prefix-url={self.site_url}"]
            + [f"--prefix-assets={self.site_url}"]
            + [filepath.as_posix()]
        )

        log.info(f"Juvix call:\n  {' '.join(cmd)}")

        cd = subprocess.run(cmd, cwd=self.DOCS_DIR, capture_output=True)
        if cd.returncode != 0:
            log.error(cd.stderr.decode("utf-8") + "\n\n" + "Fix the error first.")
            return

        # The following is necessary as this project may
        # contain assets with changes that are not reflected
        # in the generated HTML by Juvix.

        good_assets = self.DOCS_DIR.joinpath("assets")
        assets_in_html = self.HTML_CACHE_DIR.joinpath("assets")
        if assets_in_html.exists():
            shutil.rmtree(assets_in_html, ignore_errors=True)

        shutil.copytree(
            good_assets, self.HTML_CACHE_DIR.joinpath("assets"), dirs_exist_ok=True
        )

    def post_build(self) -> None:

        log.debug("Running Juvix post_build hook.")

        if not self.JUVIXCODE_CACHE_DIR.exists() or not list(
            self.JUVIXCODE_CACHE_DIR.glob("*")
        ):
            return

        sha_filecontent = (
            self.JUVIXCODE_HASH_FILE.read_text()
            if self.JUVIXCODE_HASH_FILE.exists()
            else None
        )

        current_sha: str = compute_sha_over_folder(self.JUVIXCODE_CACHE_DIR)
        log.debug(f"Current sha over Juvix content: {current_sha}")

        equal_hashes = current_sha == sha_filecontent
        if not equal_hashes:
            log.info(
                "The Juvix files have changed. You may need to rebuild the site if you include need libraries."
            )

            with open(self.JUVIXCODE_HASH_FILE, "w") as file:
                file.write(current_sha)

        self.generate_html(generate=False, move_cache=True)

    @lru_cache(maxsize=128)
    def path_juvix_md_cache(self, _filepath: Path) -> Optional[Path]:
        filepath = _filepath.absolute()
        md_filename = filepath.name.replace(".juvix.md", ".md")
        rel_to_docs = filepath.relative_to(self.DOCS_DIR)
        cache_filepath = self.MARKDOWN_JUVIX_OUTPUT / rel_to_docs.parent / md_filename
        return cache_filepath

    @lru_cache(maxsize=128)
    def read_cache(self, filepath: Path) -> Optional[str]:
        if cache_path := self.path_juvix_md_cache(filepath):
            return cache_path.read_text()
        return None

    def generate_markdown(self, filepath: Path) -> Optional[str]:
        if self.new_or_changed_or_no_exist(filepath):
            return self.run_juvix(filepath)
        return self.read_cache(filepath)

    def unqualified_module_name(self, filepath: Path) -> Optional[str]:
        fposix: str = filepath.as_posix()
        if not fposix.endswith(".juvix.md"):
            return None
        return os.path.basename(fposix).replace(".juvix.md", "")

    def qualified_module_name(self, filepath: Path) -> Optional[str]:
        absolute_path = filepath.absolute()
        cmd = [self.JUVIX_BIN, "dev", "root", absolute_path.as_posix()]
        pp = subprocess.run(cmd, cwd=self.DOCS_DIR, capture_output=True)
        root = None
        try:
            root = pp.stdout.decode("utf-8").strip()
        except Exception as e:
            log.error(f"Error running Juvix dev root: {e}")
            return None

        if not root:
            return None

        relative_to_root = filepath.relative_to(Path(root))

        # fixme use juvix dev root

        qualified_name = (
            relative_to_root.as_posix()
            .replace(".juvix.md", "")
            .replace("./", "")
            .replace("/", ".")
        )
        return qualified_name if qualified_name else None

    def md_filename(self, filepath: Path) -> Optional[str]:
        module_name = self.unqualified_module_name(filepath)
        return module_name + ".md" if module_name else None

    def run_juvix(self, _filepath: Path) -> Optional[str]:

        filepath = _filepath.absolute()
        fposix: str = filepath.as_posix()

        if not fposix.endswith(".juvix.md"):
            log.debug(f"The file: {fposix} is not a Juvix Markdown file.")
            return None

        rel_to_docs: Path = filepath.relative_to(self.DOCS_DIR)

        cmd: List[str] = [
            self.JUVIX_BIN,
            "markdown",
            "--strip-prefix=docs",
            "--folder-structure",
            f"--prefix-url={self.site_url}",
            "--stdout",
            fposix,
            "--no-colors",
        ]

        log.debug(f"Juvix\n {' '.join(cmd)}")

        pp = subprocess.run(cmd, cwd=self.DOCS_DIR, capture_output=True)

        if pp.returncode != 0:
            msg = pp.stderr.decode("utf-8").replace("\n", " ").strip()
            log.debug(f"Error running Juvix on file: {fposix} -\n {msg}")

            format_head = f"!!! failure\n\n    {msg}\n\n"
            return format_head + filepath.read_text().replace("```juvix", "```")

        log.debug(f"Saving Juvix markdown output to: {self.MARKDOWN_JUVIX_OUTPUT}")

        new_folder: Path = self.MARKDOWN_JUVIX_OUTPUT.joinpath(rel_to_docs.parent)
        new_folder.mkdir(parents=True, exist_ok=True)

        md_filename: Optional[str] = self.md_filename(filepath)
        if md_filename is None:
            log.debug(f"Could not determine the markdown file name for: {fposix}")
            return None

        new_md_path: Path = new_folder.joinpath(md_filename)

        with open(new_md_path, "w") as f:
            md_output: str = pp.stdout.decode("utf-8")
            f.write(md_output)

        raw_path: Path = self.JUVIXCODE_CACHE_DIR.joinpath(rel_to_docs)
        raw_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            shutil.copy(filepath, raw_path)
        except Exception as e:
            log.error(f"Error copying file: {e}")

        self.update_hash_file(filepath)

        return md_output

    def update_hash_file(self, filepath: Path) -> Optional[Tuple[Path, str]]:
        path_hash = compute_hash_filepath(filepath, hash_dir=self.HASH_DIR)
        try:

            with open(path_hash, "w") as f:
                content_hash = hash_file(filepath)
                f.write(content_hash)
                return (path_hash, content_hash)

        except Exception as e:
            log.error(f"Error updating hash file: {e}")
        return None
