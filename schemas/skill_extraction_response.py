from pydantic import BaseModel
from typing import List, Union

class SkillExtractionResponse(BaseModel):
    # return any
    annotations: Union[str, List[str]]