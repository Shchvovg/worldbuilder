from app.core.config import settings
from app.services.ai.client import client
from app.models.world import World


async def generate_name(race: str, world: World | None = None) -> str:
    context = f"World: {world.name} - {world.description}\n\n" if world else ""

    response = await client.chat.completions.create(
        model=settings.model,
        messages=[
            {
                "role": "user",
                "content": (
                    f"{context}"
                    f"Generate a single fantasy name for a {race} character."
                    "Return ONLY the first name, nothing else. No punctuation, no surnames."
                ),
            }
        ],
        max_tokens=20,
    )
    return response.choices[0].message.content.strip()
