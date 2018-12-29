### IMPORTS ###

from pyfiglet import Figlet
import time

### GLOBAL VARIABLES ###

### CLASS OBJECTS ###

class Bill(object):
    num_people = 0
    check_amount = 0
    tip_percentage = 0 
    check_tip =  0 
    check_total = 0
    person_total = 0
    person_tip = 0

### FUNCTIONS ###

def get_bill_information():
    # IMPORT BILL OBJECT
    bill = Bill()

    # GET THE BILL INFORMATION FROM THE USER
    bill.num_people = input ("Number of people to split the check by [0]: ")
    bill.check_amount = input ("Check Amount: ")
    bill.tip_percentage = input ("Tip % : ")

    # RETURN INFORMATION TO BE CALCULATED
    return bill

def main():
    # GET THE USER INPUT
    bill = get_bill_information ()

    # CALCULATE THE CHECK TIP
    bill.check_tip = (float(bill.check_amount) / 100) * float(bill.tip_percentage)

    # CALCULATE THE CHECK TOTAL
    bill.check_total = float(bill.check_tip) + float(bill.check_amount)

    # CALCULATE THE CHECK TIP PER PERSON
    bill.person_tip = float(bill.check_tip) / float(bill.num_people)
    
    # CALCULATE THE CHECK TOTAL PER PERSON
    bill.person_total = float(bill.check_total) / float(bill.num_people)

    print ("Check total:", round(bill.check_total, 2))
    print ("Check tip:", round(bill.check_tip, 2))
    print ("Check total per person:", round(bill.person_total, 2))
    print ("Check tip per person:", round(bill.person_tip, 2))
    
    time.sleep(5)

### PRIMARY CODE ###

figlet = Figlet(font='big')
print (figlet.renderText('Tip Calculator CMD'))

main()