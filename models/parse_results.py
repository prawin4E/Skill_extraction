
def process_result(data):
    processed_data = list()

    try:
        full_matches = data['results']['full_matches']
        ngram_scored = data['results']['ngram_scored']

        for item in full_matches:
            doc_node_value = item.get('doc_node_value', '')
            skill_id = item.get('skill_id', '')
            processed_data.append((doc_node_value, skill_id))

        for item in ngram_scored:
            doc_node_value = item.get('doc_node_value', '')
            skill_id = item.get('skill_id', '')
            processed_data.append((doc_node_value, skill_id))
    
    except KeyError as e:
        print(f"KeyError: {e} - Make sure the input data structure is correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return processed_data
