from pydantic import BaseModel, Field
from typing import List, Dict, Any

class SkillExtractionResponse(BaseModel):
    """Response model for skill extraction endpoint"""
    annotations: List[Dict[str, Any]] = Field(
        description="List of extracted skills with their types",
        example=[
            {"token": "Python", "Skill": "Python", "Skill_type": "Hard Skill"},
            {"token": "leadership", "Skill": "Leadership", "Skill_type": "Soft Skill"}
        ]
    )