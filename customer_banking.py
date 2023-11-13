# Import the create_cd_account and create_savings_account functions
import os
os.chdir('C:/Users/hafto/OneDrive/Desktop/assignment')

from savings_account import create_savings_account
from CD_account import create_cd_account
from Account import Account
from datetime import datetime
import pandas as pd

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print('Saving account activity')
    print('_'*100)
    while True:
        try:
            savings_balance = float(input("Enter current saving balance: "))
            break  # Exit the loop if a valid number is entered
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:       
        try:
            savings_interest = float(input("Enter interest Rate: "))
            break  # Exit the loop if a valid number is entered
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:             
        try:
            savings_maturity = int(input("Enter Saving account maturity: "))   
            break  # Exit the loop if a valid number is entered
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print('-'*40, '\n')

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Interest erned ${round(interest_earned,3)}")
    print(f"Current Balance ${round(updated_savings_balance,3)}")
    
    #Create a Saving account instance
    saving_account = Account(savings_balance, 0.0)
    #Update interest Erned 
    saving_account.set_interest(interest_earned)
    #Saving results in list
    saving_result = {}
    saving_result = {
             'Account Name': 'Saving Account',
             'Initial Balnce': savings_balance,
             'Saving APR' : savings_interest* 100,
             'Saving Interest Erned': interest_earned,
             'savings_maturity in Months': savings_maturity,
             'Final Balance': updated_savings_balance
             }
    print('_'* 100,'\n')
    print("Saving Account Activity log as of ",datetime.now())
    print("----------------------------")
    print(saving_result)
    print('_'*100,'\n')
    
    

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    print('CD account activity')
    print('_'*100)
    while True:
        try:
            cd_balance = float(input("Enter current cd balance: "))
            break  # Exit the loop if a valid number is entered
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:     
        try:
            cd_interest = float(input("Enter CD account interest Rate: "))
            break  # Exit the loop if a valid number is entered
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:     
        try:
            cd_maturity = int(input("Enter CD account maturity: "))
            break  # Exit the loop if a valid number is entered
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print('-'*40, '\n')
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Interest erned ${round(cd_interest_earned,3)}")
    print(f"Current CD Balance ${round(updated_cd_balance,3)}")
    #Create cd_account instance
    cd_account = Account(cd_balance,0.0)
    #Update ac account
    cd_account.set_interest(interest_earned)
    
   
    cd_result = {}
    cd_result = {
             'Account Name': 'CD Account',
             'Initial Balnce': cd_balance,
             'CD APR' : cd_interest* 100,
             'CD Interest Erned': cd_interest_earned,
             'CD maturity in Months': cd_maturity,
             'Final Balance': updated_cd_balance
             }
    print('_'* 100,'\n')
    print("Cd account acctivity log as of ",datetime.now())
    print("----------------------------------------------------")
    print(cd_result)


if __name__ == "__main__":
    # Call the main function.
    run_bunking = True
    while run_bunking  == True:
       main()
       q = input('DO you want to exit, Press (Y)es to continue or (N)o to exit aplication: ')
       if q.lower() == 'y':
           run_bunking = True
           continue
       else:
           run_bunking = False
           break
