#!/usr/bin/env python3
"""Normalize generated profile cards to the portfolio visual identity."""

from pathlib import Path

OUTPUT_DIR = Path("profile-summary-card-output/tokyonight")

# Portfolio palette:
# primary       = #e50914
# primary-light = #ff3333
# primary-dark  = #b20710
# background    = #050505
# card          = #111111
# text          = #ffffff
# secondary     = #b3b3b3
# border        = #242424

def customize_svg(path: Path) -> None:
    svg = path.read_text(encoding="utf-8")

    # Card background/border.
    svg = svg.replace('fill="#1a1b27"', 'fill="#111111"')
    svg = svg.replace('stroke="#1a1b27"', 'stroke="#242424"')

    # Tokyo Night semantic colors -> portfolio palette.
    svg = svg.replace("#70a5fd", "#e50914")  # title
    svg = svg.replace("#38bdae", "#b3b3b3")  # text
    svg = svg.replace("#bf91f3", "#ff3333")  # icon/chart

    path.write_text(svg, encoding="utf-8")


def main() -> None:
    if not OUTPUT_DIR.is_dir():
        raise SystemExit(f"Output directory not found: {OUTPUT_DIR}")

    svg_files = sorted(OUTPUT_DIR.glob("*.svg"))
    if not svg_files:
        raise SystemExit("No SVG cards found.")

    for svg_file in svg_files:
        customize_svg(svg_file)


if __name__ == "__main__":
    main()
