from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.world import World


class WorldRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, name: str, description: str) -> World:
        world = World(name=name, description=description, created_at=datetime.now())
        self.db.add(world)
        await self.db.commit()
        await self.db.refresh(world)
        return world

    async def get_by_id(self, world_id: int) -> World | None:
        result = await self.db.execute(select(World).where(World.id == world_id))
        return result.scalar_one_or_none()
