#!/usr/bin/env python3
"""Validate repository-local links and image references in Markdown and HTML.

External URLs are intentionally not fetched. This checker verifies that files, folders,
relative document links, local image references, and HTML fragment IDs resolve inside
this repository. It is suitable for GitHub Actions and local use.
"""
from __future__ import annotations

import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}
TEXT_EXTS = {".md", ".html", ".htm"}
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}

MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class HTMLRefs(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.refs: list[str] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = {k.lower(): v for k, v in attrs}
        for attr in ("href", "src"):
            value = d.get(attr)
            if value:
                self.refs.append(value)
        for attr in ("id", "name"):
            value = d.get(attr)
            if value:
                self.anchors.add(value)


def is_skipped(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def markdown_refs(text: str) -> list[str]:
    refs: list[str] = []
    for raw in MD_LINK_RE.findall(text):
        raw = raw.strip()
        if raw.startswith("<") and ">" in raw:
            raw = raw[1 : raw.index(">")]
        else:
            # Markdown destinations may optionally be followed by a quoted title.
            m = re.match(r"([^\s]+)(?:\s+[\"'].*)?$", raw)
            if m:
                raw = m.group(1)
        refs.append(raw)
    return refs


def resolve_local(source: Path, ref: str) -> tuple[Path | None, str | None]:
    ref = html.unescape(ref.strip())
    if not ref:
        return None, None

    parsed = urlsplit(ref)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES or parsed.netloc:
        return None, None

    fragment = unquote(parsed.fragment) if parsed.fragment else None
    raw_path = unquote(parsed.path)

    if not raw_path:
        return source, fragment

    if raw_path.startswith("/"):
        target = ROOT / raw_path.lstrip("/")
    else:
        target = source.parent / raw_path

    try:
        target = target.resolve()
        target.relative_to(ROOT.resolve())
    except (ValueError, OSError):
        return Path("/__OUTSIDE_REPOSITORY__"), fragment

    return target, fragment


def html_anchors(path: Path) -> set[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return set()
    parser = HTMLRefs()
    parser.feed(text)
    return parser.anchors


def check_file(source: Path) -> list[str]:
    try:
        text = source.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        return [f"{source.relative_to(ROOT)}: unable to read: {exc}"]

    if source.suffix.lower() == ".md":
        refs = markdown_refs(text)
    else:
        parser = HTMLRefs()
        parser.feed(text)
        refs = parser.refs

    errors: list[str] = []
    for ref in refs:
        target, fragment = resolve_local(source, ref)
        if target is None:
            continue

        rel_source = source.relative_to(ROOT)
        if str(target) == "/__OUTSIDE_REPOSITORY__":
            errors.append(f"{rel_source}: link escapes repository: {ref}")
            continue

        if not target.exists():
            errors.append(f"{rel_source}: missing target: {ref}")
            continue

        # Validate fragments for HTML targets, including same-page HTML links.
        if fragment and target.is_file() and target.suffix.lower() in {".html", ".htm"}:
            if fragment not in html_anchors(target):
                errors.append(f"{rel_source}: missing HTML anchor #{fragment}: {ref}")

    return errors


def main() -> int:
    files = [
        p
        for p in ROOT.rglob("*")
        if p.is_file() and p.suffix.lower() in TEXT_EXTS and not is_skipped(p.relative_to(ROOT))
    ]

    errors: list[str] = []
    for path in sorted(files):
        errors.extend(check_file(path))

    if errors:
        print(f"Internal link/image check FAILED with {len(errors)} issue(s):")
        for err in errors:
            print(f" - {err}")
        return 1

    print(f"Internal link/image check passed: scanned {len(files)} Markdown/HTML files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
