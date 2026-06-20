from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, ConfigDict
from app.core.dependencies import get_db
from app.repositories.world_repository import WorldRepository

router = APIRouter()


class WorldCreate(BaseModel):
    name: str
    description: str


class WorldResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


@router.post("/", response_model=WorldResponse)
async def create_world(data: WorldCreate, db: AsyncSession = Depends(get_db)):
    repo = WorldRepository(db)
    return await repo.create(data.name, data.description)


@router.get("/{world_id}", response_model=WorldResponse)
async def get_world(world_id: int, db: AsyncSession = Depends(get_db)):
    repo = WorldRepository(db)
    print(repo)
    world = await repo.get_by_id(world_id)
    if not world:
        raise HTTPException(status_code=404, detail="World not found")
    return world
