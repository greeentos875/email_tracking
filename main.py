from fastapi import FastAPI, Request
from fastapi.responses import Response
from datetime import datetime

app = FastAPI()

@app.get("/track_open")
async def track_open(id: str = "", type: str = "first", request: Request = None):
    user_agent = request.headers.get("User-Agent", "Unknown")
    log_line = f"{datetime.utcnow()} | lead_id={id} | type={type} | User-Agent={user_agent}\n"

    with open("opens.log", "a") as f:
        f.write(log_line)

    # Прозрачный 1x1 GIF пиксель
    transparent_gif = (
        b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00"
        b"\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00"
        b"\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
    )
    return Response(content=transparent_gif, media_type="image/gif")
