from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.agent import Agent
from app.schemas.agent import AgentResponse

router = APIRouter(prefix="/agents", tags=["agents"])


@router.get("/", response_model=list[AgentResponse])
async def list_agents(
    category: str | None = None,
    db: AsyncSession = Depends(get_db),
) -> list[Agent]:
    query = select(Agent).where(Agent.is_active.is_(True))
    if category:
        query = query.where(Agent.category == category)
    result = await db.execute(query)
    return list(result.scalars().all())


@router.get("/{slug}", response_model=AgentResponse)
async def get_agent(slug: str, db: AsyncSession = Depends(get_db)) -> Agent:
    result = await db.execute(select(Agent).where(Agent.slug == slug, Agent.is_active.is_(True)))
    agent = result.scalar_one_or_none()
    if agent is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agent not found")
    return agent
