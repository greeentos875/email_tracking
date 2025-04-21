from fastapi import FastAPI, Request
from datetime import datetime
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from starlette.responses import Response
from user_agents import parse as parse_user_agent

from database.models import EmailLeads

# Замените на ваш реальный URL PostgreSQL (например, от Render)
DATABASE_URL = "postgresql://mybot:qe9UR3fd6ZrSDkXaqlb9Bkv9HC1J4HUt@dpg-d00gv9k9c44c73flrq2g-a.virginia-postgres.render.com/megabot_jqre"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

@app.get("/track_open")
def track_open(id: int, request: Request):
    session = SessionLocal()
    try:
        lead = session.query(EmailLeads).filter_by(id=id).first()
        if lead:
            lead.read_tracking = True
            session.commit()
    finally:
        session.close()

    # Однопиксельный GIF (1x1)
    pixel = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04' \
            b'\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
    return Response(content=pixel, media_type="image/gif")
