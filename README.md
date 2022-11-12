# Description

Creates standard labels with a simple python program using FPDF2. This program is highly configurable and has **ALREADY BEEN PRE-CONFIGURED for the following Amazon labels.**

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png](https://m.media-amazon.com/images/I/61yPOCT9otL._AC_SL1500_.jpg "Logo Title Text 2"
Reference-style: 
![alt text][logo]

Amazon Labels: https://www.amazon.com/Address-Labels-Sticker-Printer-mailing/dp/B09P16YV2K/
<p align="center">
    <h3>Label Specifications</h3>
    The red text corresponds to the configuration variables inside the code.
</p>

<p align="center">
  <img width="1568" height="1403" alt="Label Specification" src="label_description.jpg">
</p>

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

# FPDF2

Please read the documentation for FPDF2 for help with configuring more advanced labels
FPDF2: https://pyfpdf.github.io/fpdf2/
