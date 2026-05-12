#!/usr/bin/env python3
"""
Compile reveal.js deck into a fully standalone single HTML file.

Inlines all CSS, JavaScript, and markdown so the presentation works
completely offline with no external dependencies.

Usage:
    python compile.py              # Creates index-standalone.html
    python compile.py --watch      # Recompile on file changes (requires watchdog)
"""

import re
import sys
from pathlib import Path


def read_file(path: Path) -> str:
    """Read file contents, return empty string if not found."""
    if path.exists():
        return path.read_text(encoding="utf-8")
    else:
        print(f"  Warning: {path} not found, skipping")
        return ""


def inline_css(html: str, deck_dir: Path) -> str:
    """Replace <link rel="stylesheet" href="..."> with inline <style> tags."""

    def replace_link(match):
        href = match.group(1)
        # Skip external URLs (CDN, etc.)
        if href.startswith(("http://", "https://", "//")):
            print(f"  Skipping external CSS: {href}")
            return match.group(0)

        css_path = deck_dir / href
        css_content = read_file(css_path)
        if css_content:
            print(f"  Inlined CSS: {href} ({len(css_content):,} chars)")
            return f"<style>/* {href} */\n{css_content}</style>"
        return match.group(0)

    # Match <link rel="stylesheet" href="...">
    pattern = r'<link\s+rel="stylesheet"\s+href="([^"]+)"[^>]*>'
    return re.sub(pattern, replace_link, html)


def inline_js(html: str, deck_dir: Path) -> str:
    """Replace <script src="..."> with inline <script> tags."""

    def replace_script(match):
        src = match.group(1)
        # Skip external URLs (CDN, etc.)
        if src.startswith(("http://", "https://", "//")):
            print(f"  Skipping external JS: {src}")
            return match.group(0)

        js_path = deck_dir / src
        js_content = read_file(js_path)
        if js_content:
            print(f"  Inlined JS: {src} ({len(js_content):,} chars)")
            return f"<script>/* {src} */\n{js_content}</script>"
        return match.group(0)

    # Match <script src="..."> (but not <script type="text/template">)
    pattern = r'<script\s+src="([^"]+)"[^>]*></script>'
    return re.sub(pattern, replace_script, html)


def inline_markdown(html: str, deck_dir: Path) -> str:
    """Replace external markdown reference with inline content."""

    slides_path = deck_dir / "slides.md"
    if not slides_path.exists():
        print(f"  Warning: slides.md not found")
        return html

    slides_md = slides_path.read_text(encoding="utf-8")
    # Escape closing script tags in markdown
    slides_md_escaped = slides_md.replace("</script>", "<\\/script>")

    # Pattern to match the external markdown section
    pattern = r'<section\s+data-markdown="slides\.md"[^>]*>\s*</section>'

    # Replacement: inline markdown with script template
    replacement = f'''<section data-markdown
                     data-separator="^---$"
                     data-separator-vertical="^--$"
                     data-separator-notes="^Notes:">
                <script type="text/template">
{slides_md_escaped}
                </script>
            </section>'''

    result = re.sub(pattern, replacement, html, flags=re.DOTALL)
    if result != html:
        print(f"  Inlined markdown: slides.md ({len(slides_md):,} chars)")
    return result


def compile_deck(deck_dir: Path = None):
    """Compile deck into a single standalone HTML file."""

    if deck_dir is None:
        deck_dir = Path(__file__).parent

    index_path = deck_dir / "index.html"
    output_path = deck_dir / "index-standalone.html"

    if not index_path.exists():
        print(f"Error: {index_path} not found")
        sys.exit(1)

    print(f"Compiling {index_path}...")
    html = index_path.read_text(encoding="utf-8")

    # Inline everything
    html = inline_css(html, deck_dir)
    html = inline_js(html, deck_dir)
    html = inline_markdown(html, deck_dir)

    # Write output
    output_path.write_text(html, encoding="utf-8")

    final_size = len(html)
    print(f"\nCreated: {output_path}")
    print(f"  Final size: {final_size:,} chars ({final_size / 1024:.0f} KB)")


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    if "--watch" in sys.argv:
        try:
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler
            import time

            class RecompileHandler(FileSystemEventHandler):
                def on_modified(self, event):
                    if event.src_path.endswith((".md", ".html", ".css", ".js")) \
                       and "standalone" not in event.src_path:
                        print(f"\nFile changed: {event.src_path}")
                        compile_deck()

            print("Watching for changes... (Ctrl+C to stop)")
            compile_deck()  # Initial compile

            observer = Observer()
            observer.schedule(RecompileHandler(), ".", recursive=True)
            observer.start()

            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                observer.stop()
            observer.join()

        except ImportError:
            print("Watch mode requires watchdog: pip install watchdog")
            sys.exit(1)
    else:
        compile_deck()


if __name__ == "__main__":
    main()
