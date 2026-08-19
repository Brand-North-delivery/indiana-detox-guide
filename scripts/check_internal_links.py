#!/usr/bin/env python3
"""Crawl local HTML links and report broken same-origin routes."""

from __future__ import annotations

import sys
from collections import deque
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.urls.append(href)


def main() -> int:
    start = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8765/"
    origin = urlparse(start).netloc
    queue = deque([start])
    seen: set[str] = set()
    errors: list[str] = []
    while queue:
        url = urldefrag(queue.popleft()).url
        if url in seen:
            continue
        seen.add(url)
        try:
            request = Request(url, headers={"User-Agent": "IndianaDetoxGuide-QA/1.0"})
            with urlopen(request, timeout=10) as response:
                body = response.read()
                content_type = response.headers.get_content_type()
        except (HTTPError, URLError, TimeoutError) as exc:
            errors.append(f"{url}: {exc}")
            continue
        if content_type != "text/html":
            continue
        parser = Links()
        parser.feed(body.decode("utf-8", errors="replace"))
        for href in parser.urls:
            if href.startswith(("mailto:", "tel:", "javascript:")):
                continue
            target = urldefrag(urljoin(url, href)).url
            parsed = urlparse(target)
            if parsed.netloc == origin:
                queue.append(target)
    if errors:
        print("Broken internal links:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Internal link crawl passed: {len(seen)} URLs checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
