from typing import List, Literal
from pydantic import BaseModel, Field, field_validator

class Entity(BaseModel):
    """Entity extracted from text."""
    name: str = Field(..., description="Name of the entity, capitalized")
    type: str = Field(..., description="Type of the entity")
    description: str = Field(..., description="Comprehensive description of the entity")

class Relationship(BaseModel):
    """Relationship between two entities."""
    source: str = Field(..., description="Name of the source entity")
    target: str = Field(..., description="Name of the target entity") 
    description: str = Field(..., description="Description of the relationship")
    strength: int = Field(..., ge=1, le=10, description="Strength of relationship (1-10)")

class ExtractedData(BaseModel):
    """Container for extracted entities and relationships."""
    entities: List[Entity] = Field(default_factory=list)
    relationships: List[Relationship] = Field(default_factory=list) 