from PIL import Image, ImageDraw, ImageFont
import base64
import io
from typing import Union, Tuple


def image_to_base64(image: Image.Image) -> str:
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    base64_string = base64.b64encode(buffer.read()).decode("ascii")
    return base64_string


def text_to_image(
    message: str,
    font_size: int = 30,
    bg_color: Tuple[int, int, int, int] = (0, 255, 255, 255),
    font_color: Tuple[int, int, int] = (0, 0, 0),
    image_size: Tuple[int, int] = (400, 300),
    as_base64: bool = True,
) -> Image.Image:
    font = ImageFont.truetype("./Roboto-Medium.ttf", size=font_size)
    image_width, image_height = image_size

    image = Image.new("RGBA", (image_width, image_height), bg_color)
    draw = ImageDraw.Draw(image)
    (text_width, text_height), (offset_x, offset_y) = font.font.getsize(message)

    #
    x = (image_width - text_width - offset_x) // 2
    y = (image_height - text_height - offset_y) // 2
    print("offset: ", (offset_x, offset_y))
    draw.text((x, y), message, font=font, fill=font_color)

    if as_base64:
        return image_to_base64(image)

    return image
