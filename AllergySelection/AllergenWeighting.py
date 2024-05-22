# Functions for adding weight to allergen tests

def weightResultFn(testResult, weight):
    testResult['Size'] = testResult['Size'] + weight
    return testResult

def petWeighting (testResult):
    weightResultFn(testResult, 5)
    return testResult

def seasonWeighting (testResult):
    weightResultFn(testResult, 2)
    return testResult

def timeOfDayWeighting (testResult):
    weightResultFn(testResult, 1)
    return testResult


def weightAllergyResults (selectionInput):
    
    testResults = selectionInput['AllergenSelectionInput']['TestResults']

    # Weight for pet
    petsIntake = selectionInput['AllergenSelectionInput']['Intake']['Pets']
    intakeDog = 'dog' in petsIntake.lower()
    intakeCat = 'cat' in petsIntake.lower()
    intakeGPig = 'guinea' in petsIntake.lower()
    intakeHorse = 'horse' in petsIntake.lower()
    intakeCattle = ('cow' in petsIntake.lower()) or ('cattle' in petsIntake.lower())
    intakeBird = 'bird' in petsIntake.lower()

    # Weight for early year
    seasonIntake = selectionInput['AllergenSelectionInput']['Intake']['Seasons']
    intakeEarlyYear = ('spring' in seasonIntake.lower()) or ('summer' in seasonIntake.lower())

    # Weight for time of day
    timeOfDayIntake = selectionInput['AllergenSelectionInput']['Intake']['TimeOfDay']
    intakeEarly = 'morning' in timeOfDayIntake.lower()
    intakeLate = 'evening' in timeOfDayIntake.lower()

    for testResult in testResults:

        # For dogs
        if intakeDog and ((testResult['AllergenID'] == 4825) or (testResult['AllergenID'] == 4084)):
            testResult = petWeighting(testResult)

        # For cats
        if intakeCat and (testResult['AllergenID'] == 4815):
            testResult = petWeighting(testResult)

        # For guinea pig
        if intakeGPig and (testResult['AllergenID'] == 4402):
            testResult = petWeighting(testResult)

        # For cattle
        if intakeCattle and (testResult['AllergenID'] == 4812):
            testResult = petWeighting(testResult)

        # For horse
        if intakeCat and (testResult['AllergenID'] == 4856):
            testResult = petWeighting(testResult)

        # For bird
        if intakeBird and (testResult['AllergenID'] == 4350):
            testResult = petWeighting(testResult)

        # For Early Year
        if intakeEarlyYear and (testResult['AllergenID'] in { 2204, 2306, 1019, 1169, 1664, 2678, 1436, 1061, 2564, 1910, 1703, 2627, 1214, 1541, 1340, 2099, 2051, 1454, 1832, 1661}):
            testResult = seasonWeighting(testResult)

        # For Early Day (trees and indoor)
        if intakeEarly and ((testResult['AllergenID'] in {2204, 2306, 1019, 1169, 1664, 2678, 1436, 1061, 2564, 1910, 1703, 2627, 1214, 1541, 1340, 2099, 2051, 1454, 1832, 1661}) or (testResult['AllergenID'] in {5009, 5021, 5129, 5125, 5169, 5101, 5049, 6585, 6806, 7099})):
            testResult = timeOfDayWeighting(testResult)

        # For Late Day (grasses and weeds)
        if intakeEarly and ((testResult['AllergenID'] in {537, 1745, 545, 718, 611, 831, 825, 777, 1082}) or (testResult['AllergenID'] in {1859, 2414, 1517, 1301, 2318, 2213, 2058, 1787, 1946, 1406})):
            testResult = timeOfDayWeighting(testResult)

    return testResults