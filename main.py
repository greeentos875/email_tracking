from fastapi import FastAPI, Request
from starlette.responses import Response
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from database.models import EmailLeads
import base64

# Замените на вашу строку подключения к БД на Render
DATABASE_URL = "postgresql://mybot:qe9UR3fd6ZrSDkXaqlb9Bkv9HC1J4HUt@dpg-d00gv9k9c44c73flrq2g-a.virginia-postgres.render.com/megabot_jqre"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# Прозрачный 1x1 GIF пиксель
TRANSPARENT_GIF_BASE64 = (
    b"R0lGODlhAQABAPAAAP///wAAACwAAAAAAQABAAACAkQBADs="
)
TRANSPARENT_GIF_BYTES = base64.b64decode(TRANSPARENT_GIF_BASE64)

@app.get("/track_open")
async def track_open(id: int, request: Request):
    session = SessionLocal()
    lead = session.execute(
        select(EmailLeads).where(EmailLeads.id == id)
    ).scalar_one_or_none()

    if lead:
        lead.read_tracking = True
        session.commit()

    session.close()

    return Response(content=TRANSPARENT_GIF_BYTES, media_type="image/gif")
