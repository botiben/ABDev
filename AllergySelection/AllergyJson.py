import json
import AllergenWeighting


def sortResultFn(testResult):
    return testResult['Size']



def json_file_navigation(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)


    # Sort TestResults array by Size
    ordered_results = sorted(data['AllergenSelectionInput']['TestResults'], key=sortResultFn, reverse=True)

    return ordered_results

# Example usage
json_file_path = './AllergySelectionInput.json'
top_results = json_file_navigation(json_file_path)
print(top_results)
