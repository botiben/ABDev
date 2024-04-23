# Functions for adding weight to allergen tests

def weightResultFn(testResult, weight):
    testResult['Size'] = testResult['Size'] + weight
    return testResult

def petWeighting (testResult):
    weightResultFn(testResult, 5)
    return testResult


def weightAllergyResults (selectionInput):
    testResults = selectionInput['TestResults']

    

    return testResults