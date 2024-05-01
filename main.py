from fastapi import FastAPI
from schemas import TextToImageForm, TextToImageResponse
from utils import text_to_image


app = FastAPI(tags=["API"])


@app.post("/text-to-image", tags=["API"], response_model=TextToImageResponse)
def text_to_image_api(form: TextToImageForm, with_mime: bool = False):
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
