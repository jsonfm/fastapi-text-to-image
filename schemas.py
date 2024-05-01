from typing import Optional, Tuple
from pydantic import BaseModel


class TextToImageForm(BaseModel):
    text: str
    font_size: Optional[int] = 30
    bg_color: Optional[Tuple[int, int, int, int]] = (255, 255, 255, 0)
    font_color: Optional[Tuple[int, int, int]] = (0, 0, 0)
    image_size: Optional[Tuple[int, int]] = (400, 300)


class TextToImageResponse(BaseModel):
    image: str
