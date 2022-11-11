# Description

Creates standard labels with a simple python program. Highly configurable

# Installation

Requirements: At least Python version 3.0

1. pip install fpdf2

# Instructions

Call the function below from a list of contacts to add people to the master list and the labels should automatically be generated when the program finishes.

`
def add_person_for_label(person_id, name, address, city, state, zip):
    '''
    Adds a person to the master people list for label creation

    #param person_id: ID for a person used only for testing
    #param name: Name of the person
    #param address: The address for the person
    #param city: The city for the person
    #param state: The state for the person
    #param zip: The zip for the person
    '''
    people.append({
        "PERSON_ID": person_id,
        "NAME": name,
        "ADDRESS": address,
        "CITY": city,
        "STATE": state,
        "ZIP": zip
    })
`
It will currently produce the labels to be printed in the directory where the script is run.

#TODO
Need to implement code to extract a list of people contacts from a file like excel, iphone, word, etc.
