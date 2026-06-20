from openai import AsyncOpenAI
from app.core.config import settings

client = AsyncOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=settings.api_key,
)
