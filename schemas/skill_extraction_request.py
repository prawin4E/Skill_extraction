from pydantic import BaseModel, Field

class SkillExtractionRequest(BaseModel):
    """Request model for skill extraction endpoint"""
    resume_text: str = Field(
        ...,
        min_length=1,
        description="The resume text to extract skills from",
        example="Experienced Python developer with strong leadership skills and expertise in machine learning"
    )