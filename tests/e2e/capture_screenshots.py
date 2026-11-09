"""
@file
@package tests.e2e.capture_screenshots
@brief Takes the lecture screenshots (steps 1-7) inside a Docker container.

Run through `docker run` (see tests/e2e/Dockerfile); never on the host desktop
(framework/process/gui-testing.md). Playwright lives in the image and is not a
dependency of the project.
"""

import html
import sys
import threading
from pathlib import Path

from playwright.sync_api import Page, Route, sync_playwright
from werkzeug.serving import make_server

import blog.presentation
from blog.infrastructure.api_post_repository import BundledPostRepository
from blog.presentation.app import create_app

VIEWPORT_WIDTH = 1280
"""@brief Browser window width in pixels."""

VIEWPORT_HEIGHT = 800
"""@brief Browser window height in pixels."""

SETTLE_MS = 1500
"""@brief Milliseconds to wait after the network is idle."""

PRESENTATION = Path(blog.presentation.__file__).resolve().parent
"""@brief Folder holding the templates and static files."""

MONO_STYLE = (
    "body{background:#1e1e1e;color:#d4d4d4;font:16px/1.5 Consolas,'DejaVu Sans Mono',monospace;"
    "padding:24px}pre{margin:0}h3{color:#9cdcfe;margin:16px 0 4px}"
)
"""@brief CSS of the monospace pages."""


def render_tree(root: Path, max_depth: int = 2) -> list[str]:
    """@brief Render a folder as an indented tree, folders first.

    @param root Folder to list.
    @param max_depth Number of levels below `root` to show.
    @return One text line per entry, starting with the name of `root`.
    """
    lines = [f"{root.name}/"]
    _walk(root, "", max_depth, lines)
    return lines


def _walk(folder: Path, prefix: str, depth: int, lines: list[str]) -> None:
    if depth == 0:
        return
    entries = sorted(folder.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    for index, entry in enumerate(entries):
        last = index == len(entries) - 1
        suffix = "/" if entry.is_dir() else ""
        lines.append(f"{prefix}{'└── ' if last else '├── '}{entry.name}{suffix}")
        if entry.is_dir():
            _walk(entry, prefix + ("    " if last else "│   "), depth - 1, lines)


def head_tail(path: Path, head: int, tail: int = 0) -> list[str]:
    """@brief Take the first and last lines of a text file.

    @param path File to read.
    @param head Number of lines from the start.
    @param tail Number of lines from the end; when present an ellipsis separates them.
    @return The selected lines.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    if tail == 0:
        return lines[:head]
    return [*lines[:head], "...", *lines[-tail:]]


def monospace_page(sections: list[tuple[str, list[str]]]) -> str:
    """@brief Build an HTML page that shows titled blocks of monospace text.

    @param sections Pairs of (title, lines).
    @return The HTML document.
    """
    body = "".join(
        f"<h3>{html.escape(title)}</h3><pre>{html.escape(chr(10).join(lines))}</pre>"
        for title, lines in sections
    )
    return (
        f"<!DOCTYPE html><html><head><style>{MONO_STYLE}</style></head><body>{body}</body></html>"
    )


def _abort_subrequests(route: Route) -> None:
    if route.request.resource_type == "document":
        route.continue_()
    else:
        route.abort()


def _settle(page: Page) -> None:
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(SETTLE_MS)


def _shoot_page(page: Page, url: str, target: Path) -> None:
    page.goto(url, wait_until="networkidle")
    _settle(page)
    page.screenshot(path=str(target), full_page=True)


def _shoot_html(page: Page, content: str, target: Path) -> None:
    page.set_content(content)
    _settle(page)
    page.screenshot(path=str(target), full_page=True)


def take_screenshots(output_dir: Path) -> list[Path]:
    """@brief Serve the blog on a free port and photograph every lecture step.

    @param output_dir Folder that receives the PNG files.
    @return The files written.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    templates = PRESENTATION / "templates"
    server = make_server("127.0.0.1", 0, create_app(BundledPostRepository()))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_port}"
    names = (
        "step-1-file-structure",
        "step-2-unstyled-home",
        "step-3-styled-home",
        "step-4-includes",
        "step-5-about",
        "step-5-contact",
        "step-6-home-posts",
        "step-7-post",
    )
    targets = {name: output_dir / f"{name}.png" for name in names}
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT})
            tree = [
                *render_tree(PRESENTATION / "templates"),
                *render_tree(PRESENTATION / "static"),
            ]
            _shoot_html(
                page,
                monospace_page([("src/blog/presentation", tree)]),
                targets["step-1-file-structure"],
            )
            page.route("**/*", _abort_subrequests)
            _shoot_page(page, f"{base}/", targets["step-2-unstyled-home"])
            page.unroute("**/*")
            _shoot_page(page, f"{base}/", targets["step-3-styled-home"])
            sections = [
                ("templates/index.html", head_tail(templates / "index.html", 15, 3)),
                ("templates/header.html", head_tail(templates / "header.html", 8)),
            ]
            _shoot_html(page, monospace_page(sections), targets["step-4-includes"])
            _shoot_page(page, f"{base}/about", targets["step-5-about"])
            _shoot_page(page, f"{base}/contact", targets["step-5-contact"])
            _shoot_page(page, f"{base}/", targets["step-6-home-posts"])
            _shoot_page(page, f"{base}/post/1", targets["step-7-post"])
            browser.close()
    finally:
        server.shutdown()
    return list(targets.values())


def main(argv: list[str]) -> int:
    """@brief Entry point: the first argument is the output folder.

    @param argv Command line arguments.
    @return The process exit code.
    """
    output_dir = Path(argv[1]) if len(argv) > 1 else Path("docs/screenshots")
    for path in take_screenshots(output_dir):
        sys.stdout.write(f"{path}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
