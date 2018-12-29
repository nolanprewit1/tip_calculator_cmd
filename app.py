### IMPORT REQUIRED PYTHON MODULES ###
import time
import json
import os

from pyfiglet import Figlet

### IMPORT CONFIG FILE ### 
with open('config.json') as config_file:
    config = json.load(config_file)

### CREATE THE BILL OBJECT WE WILL USE TO HOLD ALL OF ARE VALUES ###
class Bill(object):
    num_people = 0
    check_amount = 0
    tip_percentage = 0 
    check_tip =  0 
    check_total = 0
    person_total = 0
    person_tip = 0

### DEFINE A FUNCTION TO EASILY CLEAR THE CONSOLE WINDOW ###
def clear_console():    
    os.system('cls' if os.name=='nt' else 'clear')

### DEFINE A FUNCTION TO EASILY REDISPLAY THE APPLICATION NAME USING FIGLET ###
def display_figlet():
    # DEFINE THE FONT TO USE WITH FIGLET
    figlet = Figlet(font='big')

    # PRINT THE APPLICATION NAME FROM THE CONFIG FILE USING FIGLET
    print (figlet.renderText(config.get('name')))


### DEFINE A FUNCTION TO GET THE BILL INFORMATION FROM THE USER ###
def get_bill_information():
    # DISPLAY THE APPLICATION NAME
    display_figlet()

    # GET THE NUMBER OF PEOPLE TO SLIT THE CHECK BETWEEN
    while True: 
        try:
            # ASK FOR THE USERS INPUT BUT ALSO DEFINE A DEFAULT OF 1
            Bill.num_people = int(input("Number of people to split the check by [1]: ") or 1)
        except ValueError:
            print("Please enter a number....")
            continue
        break  

    # GET THE CHECK AMOUNT
    while True:
        try: 
            Bill.check_amount = float(input("Check Amount: "))
        except ValueError:
            print("Please enter a valide check amount... EXAMPLE: 22.05")
            continue
        break

    # GET PERCETNAGE OF THE CHECK THE USER WOULD LIKE TO TIP 
    while True:
        try:
            # ASK FOR THE USERS INPUT BUT ALSO DEFINE A DEFAULT OF 20
            Bill.tip_percentage = float(input("Tip % [20]: ") or 20)
        except ValueError:
            print("Please enter a valid tip amount.... EXAMPLE: 15")
            continue
        break

    # CLEAR THE CONSOLE FOR READABILITY
    clear_console()
    return 

### DFINE A FUNCTION TO CALCULATE ALL THE VALUES OF THE BILL OBJECT ###
def calculate_bill():
    # CALCULATE THE CHECK TIP
    Bill.check_tip = (float(Bill.check_amount) / 100) * float(Bill.tip_percentage)

    # CALCULATE THE CHECK TOTAL
    Bill.check_total = float(Bill.check_tip) + float(Bill.check_amount)

    # CALCULATE THE CHECK TIP PER PERSON
    Bill.person_tip = float(Bill.check_tip) / float(Bill.num_people)
    
    # CALCULATE THE CHECK TOTAL PER PERSON
    Bill.person_total = float(Bill.check_total) / float(Bill.num_people)

### DISPLAY TO THE CONSOLE ALL THE CALCULATED VALUES OF THE BILL OBJECT ###
def display_bill_information():
    # DISPLAY THE APPLICATION NAME
    display_figlet()

    # PRINT ALL THE BILL OBJECT VALUES TO THE CONSOLE IS A READABLE FORMAT
        # {0:.2F} LETS US ADD 2 DECMAL PLACES TO THE VARIABLES
        # ROUND IS USED TO ROUND THE VALUE IF IT IS MORE THAN 2 DECIMAL PLACES
        # \T IS USED TO ADD TAB SPACING FOR BETTER READABILITY
    print ("#### CALCULATED TOTALS ####")
    print("")
    print ("Check total: \t\t\t $", "{0:.2f}".format(round(Bill.check_total, 2)))
    print ("Check tip: \t\t\t $", "{0:.2f}".format(round(Bill.check_tip, 2)))
    print ("Check total per person: \t $", "{0:.2f}".format(round(Bill.person_total, 2)))
    print ("Check tip per person: \t\t $", "{0:.2f}".format(round(Bill.person_tip, 2)))

    return

### DEFINE A FUNCTION TO GET AN ANSWER FROM THE USER OF IF THEY WANT TO RERUN THE APPLICATION OR NOT ###
def continue_question():
    # ADD SPACING IN THE CONSOLE FOR READABILITY
    print("")
    print("")
    
    # GET THE CHOICE ANSWER FROM THE USER
    while True:
        # ASK THE USER FOR INPUT BUT ALSO SET A DEFAULT OF N
        choice = input("Would you like to calculate another bill? (y/N)" or "N")

        # UPPERCASE THE INPUT FROM THE USER
        choice = choice.upper()

        # CHECK TO SEE IF THE ANSWER IS Y OR N. IF NOT RERUN THE FUNCTION
        if (choice != "Y") and (choice != "N"):
            print("Please enter Y or N...")
            continue

        # RETURN THE CHOICE
        return choice


### DEFINE THE MAIN FUNCTION THAT RUNS THE APPLICATION ###
def main():
    while True:
        get_bill_information ()

        calculate_bill()    

        display_bill_information()   

        choice = continue_question()
        
        # CHECK THE USERS CHOICE. IF IT IS YES RERUN THE MAIN FUNCTION 
        if choice == "Y":
            clear_console()
            continue
        
        # IN THIS CASE THE USER CHOSE TO NOT RERUN THE APPLICATION
        clear_console()
        display_figlet()
        print("Closing application....")
        time.sleep(3)
        break
        
if __name__ == '__main__':
    main()
