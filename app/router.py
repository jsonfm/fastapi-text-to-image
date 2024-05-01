from app.middlewares import RequireXAPIKeyDepedency
from app.schemas import TextToImageForm, TextToImageResponse
from fastapi import APIRouter, __version__
from fastapi.responses import HTMLResponse
from app.utils import text_to_image


router = APIRouter(prefix="/api/v1", tags=["API"])


@router.post("/text-to-image", tags=["API"], response_model=TextToImageResponse)
def text_to_image_api(
    api_key: RequireXAPIKeyDepedency, form: TextToImageForm, with_mime: bool = False
):
    image = text_to_image(
        form.text,
        font_size=form.font_size,
        bg_color=form.bg_color,
        font_color=form.font_color,
        image_size=form.image_size,
    )
    if with_mime:
        image = f"data:image/png;base64,{image}"
    return {"image": image}
