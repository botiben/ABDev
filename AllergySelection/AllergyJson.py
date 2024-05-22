import json
from AllergenWeighting import weightAllergyResults
from SoapNotes import generateSoapNotes
from AllergySelection import recommendAllergens


def sortResultFn(testResult):
    return testResult['Size']

def getAllergenRecommendations(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Weight results according to intake info
    weightedResults = weightAllergyResults(data)

    # Sort weighted results array by score
    orderedResults = sorted(weightedResults, key=sortResultFn, reverse=True)

    # Select allergens for treatment
    mostlyPollen = False
    recommendedAllergens, mostlyPollen = recommendAllergens(data, orderedResults)

    # Generate soap notes on allergy weighting and selection based on intake
    soapNotes = generateSoapNotes(data, mostlyPollen)

    print("Ordered Results:")
    print(orderedResults)
    print("Output:")
    print(recommendedAllergens)
    print(soapNotes)

    # Compile JSON
    outputDict = {

        "SoapNotes" : soapNotes,
        "RecommendedAllergens" : recommendedAllergens
    }

    selectionDict = {
        "AllergenSelectionOutput": outputDict
    }

    jsonResults = json.dumps(selectionDict, indent=4)
    

    # Compose AllergySelectionOutput JSON
    with open('./AllergenSelectionOutput.json', 'w') as outputFile:
        outputFile.write(jsonResults)

    return recommendedAllergens

# Example usage
json_file_path = './AllergySelectionInput.json'
top_results = getAllergenRecommendations(json_file_path)
