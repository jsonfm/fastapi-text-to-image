from fastapi import FastAPI, __version__
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from schemas import TextToImageForm, TextToImageResponse
from utils import text_to_image


app = FastAPI(tags=["API"])
app.mount("/static", StaticFiles(directory="static"), name="static")


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


@app.get("/")
async def root():
    return HTMLResponse(html)


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
