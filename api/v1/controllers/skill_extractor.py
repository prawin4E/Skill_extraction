from pprint import pprint
import spacy
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor
from fastapi import FastAPI, APIRouter, File, UploadFile, Request
from pydantic import BaseModel
from schemas.skill_extraction_response import SkillExtractionResponse
from schemas.skill_extraction_request import SkillExtractionRequest
from models.parse_results import process_result
import json

router = APIRouter()

nlp = spacy.load("en_core_web_lg")
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)

@router.post("/extract-skills", response_model=SkillExtractionResponse, summary="Extract skills from job description")
async def extract_skills(request_body: SkillExtractionRequest):
    job_description_text = request_body.resume_text

    print(job_description_text)

    if job_description_text is None:
        return SkillExtractionResponse(annotations=["No resume text provided"])

    # Extract skills from the job description
    annotations = skill_extractor.annotate(job_description_text)
    annotations = process_result(annotations)
    # Return the extracted skills
    return SkillExtractionResponse(annotations=json.dumps(annotations))