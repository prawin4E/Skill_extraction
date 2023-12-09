from pprint import pprint
from skillNer.general_params import SKILL_DB

def process_result(data) -> list:
    """
    Process the result data and extract relevant information.

    Args:
        data (dict): The input data containing the results.

    Returns:
        list: A list of dictionaries containing the processed data.

    Raises:
        KeyError: If the input data structure is incorrect.
        Exception: If an unexpected error occurs.
    """
    processed_data = []

    try:
        full_matches = data['results']['full_matches']
        ngram_scored = data['results']['ngram_scored']

        for item in full_matches:
            doc_node_value = item.get('doc_node_value', '')
            skill_id = item.get('skill_id', '')
            processed_data.append({
                'token': doc_node_value,
                'Skill': SKILL_DB[skill_id].get("skill_name"),
                'Skill_type': SKILL_DB[skill_id].get("skill_type")
            })

        for item in ngram_scored:
            doc_node_value = item.get('doc_node_value', '')
            skill_id = item.get('skill_id', '')
            processed_data.append({
                'token': doc_node_value,
                'Skill': SKILL_DB[skill_id].get("skill_name"),
                'Skill_type': SKILL_DB[skill_id].get("skill_type")
            })
    
    except KeyError as e:
        print(f"KeyError: {e} - Make sure the input data structure is correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return processed_data