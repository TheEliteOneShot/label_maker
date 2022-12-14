from fpdf import FPDF #pip install fpdf2
import random # this import is needed only for testing functionality
import math
from pathlib import Path
import os

#region Configuration
#MASTER section
UNIT_TYPE='in' #'in' means Inches. Can also be 'mm' for millimeter and 'cm' for centimeter
PAGE_HEIGHT=11 #inches
PAGE_WIDTH=8.5 #inches
LEFT_MARGIN=0.137 #inches
TOP_MARGIN=0.5 #inches
#The current RIGHT_MARGIN output has more space than 0.137 inches so this variable isn't really being used. 
#It's somewhere around 0.25 inches but I'm thinking this is how the labels look on the printing paper so it's fine.
#If for some reason the output doesn't fit the printing paper then the other variables will have to be slightly tuned until it works.
RIGHT_MARGIN=0.137 #inches
INNER_MARGIN=0.118 #inches
BOTTOM_MARGIN=None #No option to configure this. It's determined by the calculation of the other margins within page size
LABEL_WIDTH=2.625 #inches
LABEL_HEIGHT=1 #inches
LABEL_COUNT_UP_DOWN=10
LABEL_COUNT_LEFT_RIGHT=3
MASTER_FONT_TYPE='helvetica'
MASTER_FONT_SIZE=7
MASTER_FONT_BOLD=True
LABEL_OUTPUT_FILE_NAME="labels"
LABEL_OUTPUT_FILE_EXTENSION=".pdf"
ADD_LABEL_BORDERS=False #Adds borders to the labels
TESTING_MODE=False #Adds fake people. Turn off when ready to use with real people
TESTING_MODE_FAKE_PEOPLE_AMOUNT=200 #Amount of fake people to add for testing mode

#NAME label section
HEIGHT_ABOVE_NAME=0.25 #inches
NAME_FONT_TYPE='helvetica'
NAME_FONT_SIZE=10
NAME_FONT_BOLD=True
NAME_HEIGHT=0.2 #inches
HEIGHT_BELOW_NAME=0.2 #inches

#ADDRESS label section
ADDRESS_FONT_TYPE='helvetica'
ADDRESS_FONT_SIZE=8
ADDRESS_FONT_BOLD=True
ADDRESS_HEIGHT=0.2 #inches
HEIGHT_BELOW_ADDRESS=0.2 #inches

#STATE, CITY, and ZIP label section
STATE_CITY_ZIP_FONT_TYPE='helvetica'
STATE_CITY_ZIP_FONT_SIZE=8
STATE_CITY_ZIP_BOLD=True
STATE_CITY_ZIP_HEIGHT=0.1 #inches
HEIGHT_BELOW_STATE_CITY_ZIP=0.35 #inches

pdf = FPDF(unit=UNIT_TYPE,format=(PAGE_WIDTH,PAGE_HEIGHT))

pdf.set_margins(LEFT_MARGIN,TOP_MARGIN,RIGHT_MARGIN)
pdf.set_font(MASTER_FONT_TYPE,'B' if MASTER_FONT_BOLD else '',MASTER_FONT_SIZE)
pdf.set_auto_page_break(False)
#endregion

#region Main Code

def get_current_output_files_in_directory():
    '''
    Gets the count of label output files in the current directory
    '''
    current_count = 0
    for x in os.listdir(Path(__file__).parent.absolute()):
        if x.endswith(".pdf"):
            current_count = current_count + 1
    return current_count

def get_current_output_file_name():
    '''
    Gets the output file name and adds a version number if there are more than one so it doesn't overwrite the previous one
    '''
    __version = get_current_output_files_in_directory()
    return f"{Path(__file__).parent.absolute()}\\{LABEL_OUTPUT_FILE_NAME + '_' + str(__version) if __version > 0 else LABEL_OUTPUT_FILE_NAME}{LABEL_OUTPUT_FILE_EXTENSION}"

def get_random_name_for_testing():
    '''
    Gets a random male or female name
    '''
    return random.choice(["John Doe", "Mary Jane"])

def get_random_address_for_testing():
    '''
    Gets a partially randomized address
    '''
    return f"{random.randrange(1, 1000)} blvd. The Address Unit #{random.randrange(100, 1000, 2)}"

people = []

def add_person_for_label(person_id, name, address, city, state, zip, country):
    '''
    Adds a person to the master people list for label creation

    #param person_id: ID for a person used only for testing
    #param name: Name of the person
    #param address: The address for the person
    #param city: The city for the person
    #param state: The state for the person
    #param zip: The zip for the person
    #param country: The country for the person
    '''
    people.append({
        "PERSON_ID": person_id,
        "NAME": name,
        "ADDRESS": address,
        "CITY": city,
        "STATE": state,
        "ZIP": zip,
        "COUNTRY": country
    })

def add_fake_people(amount):
    '''
    This function adds fake people to the labels for testing of the design
    #param amount: Adds this many fake people
    '''
    for person_id in range(1, amount + 1):
        add_person_for_label(person_id, get_random_name_for_testing(), get_random_address_for_testing(), "Honolulu", "HI", 96860)

def get_person_for_label_creation_by_amount(amount):
    '''
    This function pulls a defined number of people from the master people list.
    This is used to get the necessary amount of people to create a row from left to right.
    Note: Every person retrieved is removed (or popped) from the master list
    #param amount: Gets this many people from the master people list
    '''
    result = []
    for i in range(0, min(amount, len(people))): result.append(people.pop(0))
    return result

def read_contacts_from_csv():
    for x in os.listdir(Path(__file__).parent.absolute()):
        if x.endswith(".csv"):
            input_file = open(f"{Path(__file__).parent.absolute()}\\{x}", "r", encoding="utf8")
            for position, line in enumerate(input_file.readlines(),0):
                if position > 0:
                    sections = line.split(",")
                    name = sections[0]
                    address = sections[1]
                    city = sections[2]
                    state = sections[3]
                    zip_code = sections[4]
                    country = sections[5]
                    add_person_for_label(len(people), name, address, city, state, zip_code, country)
            

# Add fake people if testing mode is turned on
add_fake_people(TESTING_MODE_FAKE_PEOPLE_AMOUNT) if TESTING_MODE else read_contacts_from_csv()

# Calculate the amount of label pages needed for the amount of people
total_people = len(people)
page_amount = math.ceil(len(people) / (LABEL_COUNT_UP_DOWN * LABEL_COUNT_LEFT_RIGHT))

print(f'Now starting to generate {page_amount} pages of labels for {len(people)} people.')

for page in range(0, page_amount):
    '''
    This section is called per page
    '''
    pdf.add_page()
    for i in range(LABEL_COUNT_UP_DOWN):
        #LABEL BORDERS
        person = get_person_for_label_creation_by_amount(LABEL_COUNT_LEFT_RIGHT)
        column_count = min(LABEL_COUNT_LEFT_RIGHT, len(person))
        for j in range(column_count):
            pdf.cell(w=LABEL_WIDTH,h=1,fill=False, align="C", border=1 if ADD_LABEL_BORDERS else 0)
            
            #Add the inner margin
            if j < LABEL_COUNT_LEFT_RIGHT - 1:
                pdf.cell(w=INNER_MARGIN,h=1,fill=False, align="C", border=0)

        #LABEL NAMES
        pdf.ln(HEIGHT_ABOVE_NAME)
        for j in range(column_count):
            pdf.set_font(NAME_FONT_TYPE,'B' if NAME_FONT_BOLD else '',NAME_FONT_SIZE)
            name = f"{person[j]['NAME']} ID: {person[j]['PERSON_ID']}" if TESTING_MODE else {person[j]['NAME']}
            pdf.cell(w=LABEL_WIDTH,h=NAME_HEIGHT,txt=name, align="C")

            #Add the inner margin
            if j < LABEL_COUNT_LEFT_RIGHT - 1:
                pdf.cell(w=INNER_MARGIN,h=1,fill=False, align="C", border=0)
        pdf.ln(HEIGHT_BELOW_NAME)

        #LABEL ADDRESSES
        for j in range(column_count):
            pdf.set_font(ADDRESS_FONT_TYPE,'B' if ADDRESS_FONT_BOLD else '',ADDRESS_FONT_SIZE)
            pdf.cell(w=LABEL_WIDTH,h=ADDRESS_HEIGHT,txt=person[j]['ADDRESS'], align="C")
            if j < LABEL_COUNT_LEFT_RIGHT - 1:
                pdf.cell(w=INNER_MARGIN,h=1,fill=False, align="C", border=0)
        pdf.ln(HEIGHT_BELOW_ADDRESS)

        #LABEL STATES, CITIES, ZIP CODES
        for j in range(column_count):
            pdf.set_font(STATE_CITY_ZIP_FONT_TYPE,'B' if STATE_CITY_ZIP_BOLD else '',STATE_CITY_ZIP_FONT_SIZE)
            __city = f"{person[j]['CITY']}, " if person[j]['CITY'].strip() != "" else person[j]['CITY']
            __state = f"{person[j]['STATE']}, " if person[j]['STATE'].strip() != "" else person[j]['STATE']
            __zip = f"{person[j]['ZIP']}, " if person[j]['ZIP'].strip() != "" else person[j]['ZIP']
            # The last item doesn't have a comma behind it
            __country = person[j]['COUNTRY']
            pdf.cell(w=LABEL_WIDTH,h=STATE_CITY_ZIP_HEIGHT,txt=f"{__city}{__state}{__zip}{__country}", align="C")

            #Add the inner margin
            if j < LABEL_COUNT_LEFT_RIGHT - 1:
                pdf.cell(w=INNER_MARGIN,h=1,fill=False, align="C", border=0)
        pdf.ln(HEIGHT_BELOW_STATE_CITY_ZIP)

__output_file_name = get_current_output_file_name()
pdf.output(__output_file_name)
print(f'Successfully created labels for {total_people - len(people)} people out of {total_people} people at location {__output_file_name}')
#endregion
