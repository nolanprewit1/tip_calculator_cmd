import time
import json
import os

from pyfiglet import Figlet

with open('config.json') as config_file:
    config = json.load(config_file)

class Bill(object):

    num_people = 0
    check_amount = 0
    tip_percentage = 0 
    check_tip =  0 
    check_total = 0
    person_total = 0
    person_tip = 0

def clear_console():
    
    os.system('cls' if os.name=='nt' else 'clear')

def display_figlet():

    # DISPLAY THE APPLICATION NAME USING FIGLET
    figlet = Figlet(font='big')
    print (figlet.renderText(config.get('name')))

def get_bill_information():

    display_figlet()

    while True: 
        try:
            Bill.num_people = int(input("Number of people to split the check by [1]: ") or 1)
        except ValueError:
            print("Please enter a number....")
            continue
        break  

    while True:
        try: 
            Bill.check_amount = float(input("Check Amount: "))
        except ValueError:
            print("Please enter a valide check amount... EXAMPLE: 22.05")
            continue
        break

    while True:
        try:
            Bill.tip_percentage = float(input("Tip % [20]: ") or 20)
        except ValueError:
            print("Please enter a valid tip amount.... EXAMPLE: 15")
            continue
        break

    clear_console()
    return 

def calculate_bill():

    # CALCULATE THE CHECK TIP
    Bill.check_tip = (float(Bill.check_amount) / 100) * float(Bill.tip_percentage)

    # CALCULATE THE CHECK TOTAL
    Bill.check_total = float(Bill.check_tip) + float(Bill.check_amount)

    # CALCULATE THE CHECK TIP PER PERSON
    Bill.person_tip = float(Bill.check_tip) / float(Bill.num_people)
    
    # CALCULATE THE CHECK TOTAL PER PERSON
    Bill.person_total = float(Bill.check_total) / float(Bill.num_people)

def display_bill_information():

    display_figlet()

    print ("#### CALCULATED TOTALS ####")
    print("")
    print ("Check total: \t\t\t $", "{0:.2f}".format(round(Bill.check_total, 2)))
    print ("Check tip: \t\t\t $", "{0:.2f}".format(round(Bill.check_tip, 2)))
    print ("Check total per person: \t $", "{0:.2f}".format(round(Bill.person_total, 2)))
    print ("Check tip per person: \t\t $", "{0:.2f}".format(round(Bill.person_tip, 2)))

    return

def continue_question():

    print("")
    print("")
    
    while True:
        choice = input("Would you like to calculate another bill? (y/N)" or "N")
        choice = choice.upper()
        print(choice)

        if (choice != "Y") and (choice != "N"):
            print("Please enter Y or N...")
            continue

        return choice

def main():
    while True:
        get_bill_information ()

        calculate_bill()    

        display_bill_information()   

        choice = continue_question()
        
        if choice == "Y":
            clear_console()
            continue
        
        clear_console()
        display_figlet()
        print("Closing application....")
        time.sleep(3)
        break
        
if __name__ == '__main__':
    main()
