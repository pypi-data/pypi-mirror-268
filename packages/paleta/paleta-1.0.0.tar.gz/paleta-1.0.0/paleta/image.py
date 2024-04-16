from __future__ import annotations

from paleta.palette import Palette, ConversionPalette
from paleta.color import Color

from PIL import Image, ImageDraw, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def extract_palette(f: str) -> Palette:
    image = Image.open(f)
    image = image.convert("RGBA")

    color_list = image.getcolors()
    if color_list is None:
        raise ValueError(
            f'Extracted Palette is NoneType. Use alternative `{extract_palette_ext.__name__}` to extract all instead.'
        )

    new_palette = Palette(*(x[-1] for x in color_list))
    return new_palette


def extract_palette_ext(f: str, alpha_threshold=0) -> Palette:
    image = Image.open(f)
    image = image.convert("RGBA")

    new_palette = Palette()
    for pix in image.getdata():
        if pix[-1] > alpha_threshold:
            new_palette.add(pix)

    return new_palette


def export_palette(palette, f, size=(8, 8)) -> None:
    f_image = Image.new("RGBA", (size[0] * len(palette), size[1]), 0)
    draw = ImageDraw.Draw(f_image)

    for i, color in enumerate(palette):
        if isinstance(color, Color):
            draw.rectangle(((i * size[0], 0), ((i + 1) * size[0], size[1])), color.irgba)
        else:
            draw.rectangle(((i * size[0], 0), ((i + 1) * size[0], size[1])), color)

    f_image.save(f)
    return


def convert_palette(f_in, cmap: ConversionPalette | dict = None, f_out="") -> None:
    if cmap is None:
        return

    if isinstance(cmap, ConversionPalette):
        cmap = cmap.to_dict()

    f_image = Image.open(f_in)
    f_image = f_image.convert("RGBA")

    new_image = Image.new("RGBA", f_image.size)
    for x in range(f_image.width):
        for y in range(f_image.height):
            pix = f_image.getpixel((x, y))

            if pix in cmap:
                new_pix = cmap[pix]
            else:
                new_pix = pix
            new_image.putpixel((x, y), new_pix)

    f_out = f_out if f_out != "" else f_in
    new_image.save(f_out)
    return


def extract_convert_palette(f_a: str, f_b: str, f_out="", method="min_distance") -> None:
    pa = extract_palette_ext(f_a)
    pb = extract_palette_ext(f_b)

    if method == "min_distance":
        cmap = ConversionPalette.map(pa, pb)
    else:
        raise NotImplemented(f"Unable to run {extract_convert_palette.__name__} with method `{method}`.")

    convert_palette(f_a, cmap, f_out=f_out)
    return
