from fastapi import FastAPI, Request
from starlette.responses import Response
from datetime import datetime
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/track_open")
async def track_open(request: Request, id: str):
    user_agent = request.headers.get("user-agent", "unknown")
    timestamp = datetime.utcnow().isoformat()
    
    logging.info(f"📨 OPEN | id={id} | ua={user_agent} | time={timestamp}")
    
    # 1x1 прозрачное изображение
    pixel_data = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00' \
                 b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00' \
                 b'\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'

    return Response(content=pixel_data, media_type="image/gif")
