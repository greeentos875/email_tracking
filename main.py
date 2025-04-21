from fastapi import FastAPI, Request
from starlette.responses import Response
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from database.models import EmailLeads
import base64

# Замените на вашу строку подключения к БД на Render
DATABASE_URL = "postgresql+psycopg2://user:password@hostname:port/dbname"

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
