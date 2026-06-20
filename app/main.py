from fastapi import FastAPI
from app.api.v1.routes import names, worlds

app = FastAPI(title="Game Lore API")

app.include_router(names.router, prefix="/generate", tags=["generate"])
app.include_router(worlds.router, prefix="/worlds", tags=["worlds"])


@app.get("/health")
async def health():
    return {"status": "ok"}
