from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.core.dependencies import get_db
from app.repositories.world_repository import WorldRepository
from app.services.ai import generation

router = APIRouter()


class NameResponse(BaseModel):
    name: str
    race: str
    world: str | None = None


@router.get("/name", response_model=NameResponse)
async def generate_name(
    race: str = "human", world_id: int | None = None, db: AsyncSession = Depends(get_db)
):
    world = None
    if world_id:
        repo = WorldRepository(db)
        world = await repo.get_by_id(world_id)
    name = await generation.generate_name(race, world)
    return NameResponse(name=name, race=race, world=world.name if world else None)
