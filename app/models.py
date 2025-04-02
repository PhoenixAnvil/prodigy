from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    mission: Optional[str] = None
    vision: Optional[str] = None
