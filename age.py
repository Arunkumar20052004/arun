from datetime import datetime

def age_calculator():
    birth_year = int(input("Enter your birth year: "))
    current_year = datetime.now().year
    print("Your age is:", current_year - birth_year)

age_calculator()
