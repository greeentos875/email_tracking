# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

@app.get("/track_open", response_class=HTMLResponse)
async def track_open(id: str = "", request: Request = None):
    user_agent = request.headers.get("User-Agent", "Unknown")
    with open("opens.log", "a") as f:
        f.write(f"{datetime.utcnow()} | lead_id={id} | User-Agent={user_agent}\n")
    
    # Прозрачный 1x1 GIF пиксель
    transparent_gif = (
        b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00"
        b"\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00"
        b"\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
    )
    return HTMLResponse(content=transparent_gif, media_type="image/gif")
