#!/usr/bin/env python3
"""Scrape George Hotz's blog (the-singularity-is-nearer) into raw/blog/ as markdown.

Immutable source layer for the wiki. Idempotent + resumable: skips posts already
downloaded. Run again any time to pick up new posts.

    python3 raw/scrape_blog.py
"""
import html
import os
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser

INDEX_URL = "https://geohot.github.io/blog/"
BASE = "https://geohot.github.io"
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog")
UA = "Mozilla/5.0 (geohotclone-wiki scraper; personal knowledge base)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def post_urls():
    idx = fetch(INDEX_URL)
    found = re.findall(r'href="([^"]*\d{4}/\d{2}/\d{2}/[^"]*\.html)"', idx)
    urls = []
    seen = set()
    for h in found:
        u = h if h.startswith("http") else BASE + h
        if u not in seen:
            seen.add(u)
            urls.append(u)
    return sorted(urls)


class PostParser(HTMLParser):
    """Extract title + convert the post-content div to markdown."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None
        self._in_title = False
        self._title_depth = None
        self.depth = 0
        self.active = False           # inside post-content
        self.active_depth = None
        self.out = []                 # markdown chunks
        self.list_stack = []          # 'ul' | 'ol'
        self._href = None
        self._link_text = []
        self._in_link = False
        self._skip = 0                # inside script/style
        self._pre = 0                 # inside pre/code block

    # ---- helpers ----
    def emit(self, s):
        if self.active:
            self.out.append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        if tag in ("script", "style"):
            self._skip += 1
            return
        if tag == "div":
            self.depth += 1
            if not self.active and "post-content" in cls:
                self.active = True
                self.active_depth = self.depth
            return
        if tag in ("h1",) and ("post-title" in cls or "p-name" in cls):
            self._in_title = True
            return
        if not self.active:
            return
        if tag == "p":
            self.emit("\n\n")
        elif tag in ("h1", "h2", "h3", "h4"):
            self.emit("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "br":
            self.emit("  \n")
        elif tag == "strong" or tag == "b":
            self.emit("**")
        elif tag == "em" or tag == "i":
            self.emit("*")
        elif tag == "blockquote":
            self.emit("\n\n> ")
        elif tag == "ul":
            self.list_stack.append("ul")
            self.emit("\n")
        elif tag == "ol":
            self.list_stack.append("ol")
            self.emit("\n")
        elif tag == "li":
            bullet = "- " if (self.list_stack and self.list_stack[-1] == "ul") else "1. "
            self.emit("\n" + "  " * max(0, len(self.list_stack) - 1) + bullet)
        elif tag == "a":
            self._in_link = True
            self._href = a.get("href")
            self._link_text = []
        elif tag == "img":
            src = a.get("src", "")
            if src and not src.startswith("http"):
                src = BASE + src
            self.emit(f"\n\n![{a.get('alt','')}]({src})\n\n")
        elif tag in ("pre", "code"):
            self._pre += 1
            self.emit("`" if tag == "code" and self._pre == 1 else "\n```\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = max(0, self._skip - 1)
            return
        if tag == "h1" and self._in_title:
            self._in_title = False
            return
        if tag == "div":
            if self.active and self.depth == self.active_depth:
                self.active = False
            self.depth -= 1
            return
        if not self.active:
            return
        if tag in ("strong", "b"):
            self.emit("**")
        elif tag in ("em", "i"):
            self.emit("*")
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            self.emit("\n")
        elif tag == "blockquote":
            self.emit("\n")
        elif tag == "a":
            text = "".join(self._link_text).strip()
            href = self._href or ""
            if href and not href.startswith(("http", "#", "mailto")):
                href = BASE + href
            if text:
                self.emit(f"[{text}]({href})" if href else text)
            self._in_link = False
            self._href = None
            self._link_text = []
        elif tag in ("pre", "code"):
            self.emit("`" if tag == "code" and self._pre == 1 else "\n```\n")
            self._pre = max(0, self._pre - 1)

    def handle_data(self, data):
        if self._skip:
            return
        if self._in_title:
            self.title = (self.title or "") + data
            return
        if not self.active:
            return
        if self._in_link:
            self._link_text.append(data)
        else:
            self.emit(data)


def to_markdown(html_text):
    p = PostParser()
    p.feed(html_text)
    title = (p.title or "").strip()
    body = "".join(p.out)
    # tidy whitespace
    body = re.sub(r"[ \t]+\n", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = re.sub(r"[ \t]{2,}", " ", body)
    return title, body.strip()


def parse_url_meta(url):
    m = re.search(r"/(\d{4})/(\d{2})/(\d{2})/([^/]+)\.html$", url)
    y, mo, d, slug = m.groups()
    return f"{y}-{mo}-{d}", slug


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    urls = post_urls()
    print(f"Found {len(urls)} posts")
    new = 0
    for i, url in enumerate(urls, 1):
        date, slug = parse_url_meta(url)
        out_path = os.path.join(OUT_DIR, f"{date}-{slug}.md")
        if os.path.exists(out_path):
            continue
        try:
            html_text = fetch(url)
            title, body = to_markdown(html_text)
        except Exception as e:
            print(f"  ! {url}: {e}", file=sys.stderr)
            continue
        fm = (
            "---\n"
            f"title: {title!r}\n"
            f"date: {date}\n"
            f"slug: {slug}\n"
            f"source_url: {url}\n"
            "author: George Hotz (geohot)\n"
            "---\n\n"
        )
        with open(out_path, "w") as f:
            f.write(fm + f"# {title}\n\n" + body + "\n")
        new += 1
        print(f"  [{i}/{len(urls)}] {date} {title[:60]}")
        time.sleep(0.4)
    print(f"Done. {new} new, {len(urls)} total.")


if __name__ == "__main__":
    main()
