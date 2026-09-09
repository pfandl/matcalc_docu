#!/usr/bin/env python
"""Generate per-direction recoloured copies of the Tutorial 1 screenshots.

The T1 screenshots carry baked-in annotations (red rectangles, red label
letters, yellow highlight fields, yellow leader lines). For the layout-
comparison previews we want each direction's callouts in its own hue instead
of red-for-everyone. CSS can't touch pixels, so we pre-render the variants
here and commit them; build-previews.sh / the Pages workflow then copy the
matching set over the originals in each preview build.

    preview-assets/t1/handbook/*.png    magenta  #D6006C
    preview-assets/t1/companion/*.png   orange   #E8590C
    preview-assets/t1/atlas/*.png       violet   #7C3AED
    (the "current" baseline keeps the original red.)

Run from the repo root:  python tools/gen-preview-images.py
Requires (NOT in requirements.txt - CI only copies the committed PNGs):
    pip install pillow numpy scipy
"""
import io, pathlib
import numpy as np
from PIL import Image
from scipy import ndimage

REPO = pathlib.Path(__file__).resolve().parent.parent
SRC  = REPO / "src" / "tutorials" / "t1" / "img"
OUT  = REPO / "preview-assets" / "t1"

# variant -> (strong callout hue, pale chip tint)
VARIANTS = {
    "handbook":  ((0xD6, 0x00, 0x6C), (0xF5, 0xBF, 0xDA)),
    "companion": ((0xE8, 0x59, 0x0C), (0xF9, 0xD6, 0xC2)),
    "atlas":     ((0x7C, 0x3A, 0xED), (0xDE, 0xCE, 0xFA)),
}

# every T1 image that has a red annotation drawn on it
ANNOTATED = [
    "t1_menu_application_style_6101002.png", "t1_menu_close_workspace_6101002.png",
    "t1_menu_file_6101002.png", "t1_menu_file_new_6101002.png",
    "t1_menu_recent_workdirs_6101002.png", "t1_menu_save_6101002.png",
    "t1_menu_save_as_6101002.png", "t1_menu_show_windows_6101002.png",
    "t1_menu_window_font_6101002.png", "t1_menu_working_directory_6101002.png",
    "t1_menu_workspace_info_6101002.png", "t1_new_file_workspace_6101002.png",
    "t1_new_workspace_button_6101002.png", "t1_restore_window_positions_6101002.png",
    "t1_screenshot_6101002.png", "t1_workdir_dropbox_6101002.png",
    "t1_icon_new_6101002.png", "t1_icon_save_6101002.png", "t1_icon_close_6101002.png",
]
SCREENSHOT = "t1_screenshot_6101002.png"   # the only one with the label/line layer
BOX3 = np.ones((3, 3), bool)


def recolour(png_bytes, rgb):
    """Menu / dialog / toolbar crops: just the red outline box -> hue + faint fill."""
    a = np.asarray(Image.open(io.BytesIO(png_bytes)).convert("RGB")).astype(np.float32)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    mx = np.maximum(G, B)
    # near-pure red only: spares the ladybug logo and the orange console text
    hi  = np.clip((R - 238) / 17.0, 0, 1)
    sat = np.clip((R - mx - 110) / 90.0, 0, 1)
    w = np.clip(hi * sat * 2.4, 0, 1)

    stroke = w > 0.35
    thick = stroke.copy()
    for sh in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        thick |= np.roll(stroke, sh, (0, 1))
    w = np.where(thick & ~stroke, 0.92, w)
    w = np.where(w < 0.10, 0.0, w)

    tgt = np.array(rgb, np.float32)
    out = a * (1 - w[..., None]) + tgt[None, None, :] * w[..., None]

    if R.size <= 260_000:                      # faint wash inside each box
        filled = ndimage.binary_fill_holes(thick)
        interior = filled & ~thick
        lab, n = ndimage.label(interior)
        wash = np.zeros(interior.shape, bool)
        cap = 0.30 * interior.size
        for i in range(1, n + 1):
            comp = lab == i
            if comp.sum() < cap:
                wash |= comp
        wf = np.where(wash, 0.11, 0.0)[..., None]
        out = out * (1 - wf) + tgt[None, None, :] * wf

    return _png(out)


def recolour_screenshot(png_bytes, strong_rgb, chip_rgb):
    """Full-app overview: rectangles + red letters + yellow fields + yellow lines.
    letters / rectangles / lines -> strong hue ; fields -> pale chip tint."""
    strong = np.array(strong_rgb, np.float32)
    chip   = np.array(chip_rgb, np.float32)
    a = np.asarray(Image.open(io.BytesIO(png_bytes)).convert("RGB")).astype(np.float32)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    mx, mnRG = np.maximum(G, B), np.minimum(R, G)

    hi  = np.clip((R - 238) / 17.0, 0, 1)
    sat = np.clip((R - mx - 110) / 90.0, 0, 1)
    wr  = np.clip(hi * sat * 2.4, 0, 1)
    stroke = wr > 0.35
    thick = stroke.copy()
    for sh in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        thick |= np.roll(stroke, sh, (0, 1))
    wr = np.where(thick & ~stroke, 0.92, wr)

    yst   = np.clip((mnRG - B - 70) / 110.0, 0, 1)
    ymask = yst > 0.25
    solid = ndimage.binary_fill_holes(ymask)
    core  = ndimage.binary_erosion(solid, BOX3, iterations=2)
    field = ndimage.binary_dilation(core, BOX3, iterations=3) & ymask
    line  = ymask & ~field

    out = a.copy()
    wf = np.where(field, yst, 0.0)[..., None]
    out = out * (1 - wf) + chip[None, None, :] * wf
    wl = np.where(line, yst, 0.0)[..., None]
    out = out * (1 - wl) + strong[None, None, :] * wl
    wR = np.where(wr > 0.10, wr, 0.0)[..., None]
    out = out * (1 - wR) + strong[None, None, :] * wR
    return _png(out)


def _png(arr):
    buf = io.BytesIO()
    Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).save(buf, "PNG", optimize=True)
    return buf.getvalue()


def main():
    total = 0
    for variant, (strong, chip) in VARIANTS.items():
        d = OUT / variant
        d.mkdir(parents=True, exist_ok=True)
        for name in ANNOTATED:
            raw = (SRC / name).read_bytes()
            if name == SCREENSHOT:
                png = recolour_screenshot(raw, strong, chip)
            else:
                png = recolour(raw, strong)
            (d / name).write_bytes(png)
            total += 1
        print(f"{variant:10} -> {len(ANNOTATED)} images  ({d.relative_to(REPO)})")
    print(f"done: {total} files")


if __name__ == "__main__":
    main()
