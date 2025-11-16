import logging
from typing import List, Dict, Any
from skillNer.general_params import SKILL_DB

logger = logging.getLogger(__name__)


def process_result(data: Dict[str, Any]) -> List[Dict[str, str]]:
    """
    Process the SkillNER result data and extract relevant skill information.

    Args:
        data: The input data dictionary containing the results from SkillNER

    Returns:
        A list of dictionaries containing processed skill data with keys:
        - token: The extracted text token
        - Skill: The standardized skill name
        - Skill_type: The type of skill (Hard Skill, Soft Skill, etc.)

    Raises:
        KeyError: If the input data structure is incorrect
        Exception: If an unexpected error occurs
    """
    processed_data = []

    try:
        # Extract full matches and ngram scored results
        results = data.get('results', {})
        full_matches = results.get('full_matches', [])
        ngram_scored = results.get('ngram_scored', [])

        # Process full matches
        for item in full_matches:
            doc_node_value = item.get('doc_node_value', '')
            skill_id = item.get('skill_id', '')

            if skill_id in SKILL_DB:
                processed_data.append({
                    'token': doc_node_value,
                    'Skill': SKILL_DB[skill_id].get("skill_name", ""),
                    'Skill_type': SKILL_DB[skill_id].get("skill_type", "")
                })
            else:
                logger.warning(f"Skill ID '{skill_id}' not found in SKILL_DB")

        # Process ngram scored matches
        for item in ngram_scored:
            doc_node_value = item.get('doc_node_value', '')
            skill_id = item.get('skill_id', '')

            if skill_id in SKILL_DB:
                processed_data.append({
                    'token': doc_node_value,
                    'Skill': SKILL_DB[skill_id].get("skill_name", ""),
                    'Skill_type': SKILL_DB[skill_id].get("skill_type", "")
                })
            else:
                logger.warning(f"Skill ID '{skill_id}' not found in SKILL_DB")

        logger.info(f"Processed {len(processed_data)} skills from SkillNER results")

    except KeyError as e:
        logger.error(f"KeyError: {e} - Input data structure is incorrect", exc_info=True)
        raise
    except Exception as e:
        logger.error(f"Unexpected error during result processing: {e}", exc_info=True)
        raise

    return processed_data