import json

def order_and_select_top_results(json_file):
    """
    Orders the TestResults array in the JSON file by Size and selects the top 5 results.

    Args:
    json_file (str): Path to the JSON file containing TestResults array.

    Returns:
    list: Top 5 TestResults ordered by Size.
    """
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Sort TestResults array by Size
    ordered_results = sorted(data['AllergenSelectionInput']['TestResults'], key=lambda x: x['Size'], reverse=True)

    # Select top 5 results
    top_5_results = ordered_results[:5]

    return top_5_results

# Example usage
json_file_path = 'AllergySelectionInput.json'
top_results = order_and_select_top_results(json_file_path)
print(top_results)
