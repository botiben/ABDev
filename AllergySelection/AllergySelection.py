# Functions for selecting Allergens

def isMostlyPollen(recommendedResults, allergenCount):
    mostlyPollen=False
    pollenAllergens = [2204, 2306, 1019, 1169, 1664, 2678, 1436, 1061, 2564, 1910, 1703, 2627, 1214, 1541, 1340, 2099, 2051, 1454, 1832, 1661, 537, 1745, 545, 718, 611, 831, 825, 777, 1082, 1859, 2414, 1517, 1301, 2318, 2213, 2058, 1787, 1946, 1406]
    pollenCount = 0

    for result in recommendedResults:
        if result["AllergenID"] in pollenAllergens:
            pollenCount += 1

    if (pollenCount/allergenCount > .5):
        mostlyPollen = True

    if (pollenCount/allergenCount == .5) and (recommendedResults[0]["AllergenID"] in pollenAllergens):  
        mostlyPollen = True  

    return mostlyPollen
 
def recommendAllergens(intakeData, orderedResults):

    # How many allergens to recommend based on therapy
    allergenCount = 0
    therapyType = intakeData['AllergenSelectionInput']['Intake']['Immunotherapy']
    if therapyType == "Shots":
        allergenCount = 5
    elif therapyType == "Drops":
        allergenCount = 10
    else: 
        allergenCount = len(orderedResults)

    # No Contact with animals
    animalInteraction = intakeData['AllergenSelectionInput']['Intake']['AnimalInteraction']
    animalAllergens = [4825, 4084, 4402, 4815, 4350, 4812, 4856 ]
    orderedResults = [result for result in orderedResults if result["AllergenID"] not in animalAllergens]

    # Select the correct number of allergens from the weighted results
    recommendedAllergens = orderedResults[:allergenCount]

    # Pollen or Pets and indoor
    #   - What is the majority of recommended allergens? Pollen or other
    mostlyPollen = isMostlyPollen(recommendedAllergens, allergenCount)
    #   - Remove the minority from ordered results
    pollenAllergens = [2204, 2306, 1019, 1169, 1664, 2678, 1436, 1061, 2564, 1910, 1703, 2627, 1214, 1541, 1340, 2099, 2051, 1454, 1832, 1661, 537, 1745, 545, 718, 611, 831, 825, 777, 1082, 1859, 2414, 1517, 1301, 2318, 2213, 2058, 1787, 1946, 1406]
    if mostlyPollen:
        orderedResults = [result for result in orderedResults if result["AllergenID"] not in pollenAllergens]
    else:
        orderedResults = [result for result in orderedResults if result["AllergenID"] in pollenAllergens]
    #   - Get new recommended allergens from ordered results
    recommendedAllergens = orderedResults[:allergenCount]

    # Change allergen recommendation based on severity
    severityIntake = intakeData['AllergenSelectionInput']['Intake']['Severity']
    severe = 'high' in severityIntake.lower()
    if mostlyPollen and severe and (therapyType == "Shots"):
        # Remove last allergen
        recommendedAllergens.pop()
        # Add Timothy from the ordered results
        timothyResult = [result for result in orderedResults if result["AllergenID"] == 831]
        recommendedAllergens.append(timothyResult)
    
    return recommendedAllergens, mostlyPollen