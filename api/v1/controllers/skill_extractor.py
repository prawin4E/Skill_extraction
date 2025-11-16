import logging
import spacy
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor
from fastapi import APIRouter, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from schemas.skill_extraction_response import SkillExtractionResponse
from schemas.skill_extraction_request import SkillExtractionRequest
from models.parse_results import process_result
from settings import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

# Initialize NLP model and skill extractor
try:
    nlp = spacy.load("en_core_web_lg")
    skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)
    logger.info("Successfully loaded spaCy model and initialized SkillExtractor")
except Exception as e:
    logger.error(f"Failed to initialize NLP model: {str(e)}")
    raise

@router.post("/extract-skills", response_model=SkillExtractionResponse, summary="Extract skills from resume text")
@limiter.limit(f"{settings.rate_limit_per_minute}/minute")
async def extract_skills(request: Request, request_body: SkillExtractionRequest):
    """
    Extract skills from resume text using SkillNER.

    Args:
        request_body: SkillExtractionRequest containing resume text

    Returns:
        SkillExtractionResponse with extracted skills

    Raises:
        HTTPException: If skill extraction fails
    """
    try:
        resume_text = request_body.resume_text

        # Validate input
        if not resume_text or not resume_text.strip():
            raise HTTPException(status_code=400, detail="Resume text cannot be empty")

        logger.info(f"Processing resume text of length: {len(resume_text)}")

        # Extract skills from the resume text
        annotations = skill_extractor.annotate(resume_text)
        processed_annotations = process_result(annotations)

        logger.info(f"Successfully extracted {len(processed_annotations)} skills")

        # Return the extracted skills as a list of dicts
        return SkillExtractionResponse(annotations=processed_annotations)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during skill extraction: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Skill extraction failed: {str(e)}")