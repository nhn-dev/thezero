#!/usr/bin/env python3
"""The Zero — IG brand watermark (official pipeline).

Applies clean OG-style wordmark + @hello.the.zero (no pill/box).
See IG-WATERMARK-SPEC.md.
"""

from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

try:
    import cairosvg
except ImportError:  # pragma: no cover
    cairosvg = None

FG = (244, 244, 245, 255)
MUTED = (139, 139, 147, 230)
ACCENT = (124, 255, 178, 230)
HANDLE = "@hello.the.zero"

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOGO = REPO_ROOT / "public" / "brand" / "logo-on-dark.svg"


def _load_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _rasterize_wordmark(svg_path: Path, width: int) -> Image.Image:
    if cairosvg is None:
        raise RuntimeError("cairosvg is required to rasterize the wordmark SVG")
    png = cairosvg.svg2png(url=str(svg_path), output_width=width)
    logo = Image.open(BytesIO(png)).convert("RGBA")
    alpha = logo.split()[-1].point(lambda a: int(a * 0.95))
    logo.putalpha(alpha)
    return logo


def apply_watermark(
    image: Image.Image,
    *,
    logo_svg: Path = DEFAULT_LOGO,
    corner: str = "top-right",
    busy_photo: bool = False,
    handle_accent: bool = False,
) -> Image.Image:
    """Composite official watermark. corner: top-right | bottom-right."""
    base = image.convert("RGBA")
    w, h = base.size
    pad = max(16, int(min(w, h) * 0.045))
    target_w = max(140, int(w * 0.16))
    logo = _rasterize_wordmark(logo_svg, target_w)

    fs = max(18, int(w * 0.022))
    font = _load_font(fs)
    draw_probe = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    bbox = draw_probe.textbbox((0, 0), HANDLE, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    gap = max(6, int(h * 0.008))
    block_w = max(logo.width, tw)
    block_h = logo.height + gap + th

    if corner == "bottom-right":
        x = w - pad - block_w
        y = h - pad - block_h
    else:
        x = w - pad - block_w
        y = pad

    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    if busy_photo:
        scrim_h = block_h + pad
        scrim_w = block_w + pad
        scrim = Image.new("RGBA", (scrim_w, scrim_h), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(scrim)
        for i in range(scrim_h):
            a = int(100 * (i / max(1, scrim_h - 1))) if corner == "top-right" else int(
                100 * (1 - i / max(1, scrim_h - 1))
            )
            sdraw.line([(0, i), (scrim_w, i)], fill=(0, 0, 0, a))
        sx = x - pad // 4
        sy = y - pad // 4 if corner == "top-right" else y - pad // 8
        overlay.paste(scrim, (sx, sy), scrim)

    overlay.paste(logo, (x + (block_w - logo.width) // 2, y), logo)
    draw = ImageDraw.Draw(overlay)
    handle_color = ACCENT if handle_accent else MUTED
    draw.text(
        (x + (block_w - tw) // 2, y + logo.height + gap),
        HANDLE,
        fill=handle_color,
        font=font,
    )
    return Image.alpha_composite(base, overlay).convert("RGB")


def main() -> None:
    p = argparse.ArgumentParser(description="Apply The Zero IG watermark")
    p.add_argument("input", type=Path)
    p.add_argument("-o", "--output", type=Path, required=True)
    p.add_argument("--logo", type=Path, default=DEFAULT_LOGO)
    p.add_argument(
        "--corner",
        choices=("top-right", "bottom-right"),
        default="top-right",
    )
    p.add_argument("--busy", action="store_true", help="soft gradient scrim")
    p.add_argument("--accent-handle", action="store_true")
    p.add_argument("--quality", type=int, default=92)
    args = p.parse_args()

    img = Image.open(args.input)
    out = apply_watermark(
        img,
        logo_svg=args.logo,
        corner=args.corner,
        busy_photo=args.busy,
        handle_accent=args.accent_handle,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.save(args.output, quality=args.quality, optimize=True)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
