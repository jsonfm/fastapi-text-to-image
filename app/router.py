from app.schemas import TextToImageForm, TextToImageResponse
from fastapi import APIRouter, __version__
from fastapi.responses import HTMLResponse
from app.utils import text_to_image


router = APIRouter(prefix="/api/v1", tags=["API"])


html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from FastAPI@{__version__}</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
            <p>Powered by <a href="https://vercel.com" target="_blank">Vercel</a></p>
        </div>
    </body>
</html>
"""


@router.get("/")
def root():
    return HTMLResponse(html)


@router.post("/text-to-image", tags=["API"], response_model=TextToImageResponse)
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
