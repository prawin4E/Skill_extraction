from pydantic import BaseModel

class SkillExtractionRequest(BaseModel):
    resume_text: str