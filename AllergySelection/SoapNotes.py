def generateSoapNotes(selectionInput, mostlyPollen):

    # Number of Allergens
    therapyType = selectionInput['AllergenSelectionInput']['Intake']['Immunotherapy']
    therapyShots = 'shots' in therapyType.lower()
    therapyDrops = 'drops' in therapyType.lower()

    # Values for pet
    animalInteraction = selectionInput['AllergenSelectionInput']['Intake']['AnimalInteraction']

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

    # Severity
    severityIntake = selectionInput['AllergenSelectionInput']['Intake']['Severity']
    severe = 'high' in severityIntake.lower()


    soapNotes = ""

    if therapyDrops:
        soapNotes += "\n Patient requests drops, so 10 allergens will be selected."

    if therapyShots:
        soapNotes += "\n Patient requests shots, so 5 allergens will be selected."

    if not animalInteraction:
        soapNotes += "\n Patient does not have contact with animals, so animals should be excluded."

    if animalInteraction and (intakeDog or intakeCat or intakeGPig or intakeHorse or intakeCattle or intakeBird):
        soapNotes += "\n Patient has contact with the following animal(s):"

    if animalInteraction and intakeDog:
        soapNotes += "\n  Dogs"

    if animalInteraction and intakeCat:
        soapNotes += "\n  Cats"    
        
    if animalInteraction and intakeGPig:
        soapNotes += "\n  Guinea Pigs"

    if animalInteraction and intakeBird:
        soapNotes += "\n  Birds"

    if animalInteraction and intakeHorse:
        soapNotes += "\n  Horses"

    if animalInteraction and intakeCattle:
        soapNotes += "\n  Cattle"

    if intakeEarlyYear:
        soapNotes += "\n Symptoms are worse early in the year, so weight is added for trees."

    if intakeEarly:
        soapNotes += "\n Symptoms are worse early in the day, so trees and indoor allergens are weighted."

    if intakeLate:
        soapNotes += "\n Symptoms are worse late in the day, so grasses and weeds are weighted."

    if severe:
        soapNotes += "\n Symptoms are severe, so Timothy Grass should be doubled"

    if mostlyPollen:
        soapNotes += "\n Allergens with highest reaction are mostly pollens.  Recommending only pollens."
    else:
        soapNotes += "\n Allergens with highest reaction are mostly NOT pollens.  Recommending animals and interior allergens."

    return soapNotes