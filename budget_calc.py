income_dict = {"Salary": 0, "Rent": 0, "Italki": 0, "Axel": 0}
passive_dict = {"Bills": 0, "Car": 0, "Kids": 0, "Food": 0, "Other": 0}

import time

starting_question = input("Are you adding income or expenditure?\n")


def income():
    categories = ["1.Salary", "2.Rent", "3.Italki", "4.Axel"]
    print("Please chose the category by selecting the number.\n")
    print()
    time.sleep(2)
    for item in categories:
        print(item, end="   ")
        time.sleep(1)
    category_input = int(input())
    if category_input == 1:
        salary_amount = float(input("How much salary did you get?\n"))
        income_dict["Salary"] += salary_amount
    elif category_input == 2:
        rent_amount = float(input("How much rent would you like to add?\n"))
        income_dict["Rent"] += rent_amount
    elif category_input == 3:
        italki_amount = float(input("How much did you make on Italki?\n"))
        income_dict["Italki"] += italki_amount
    elif category_input == 4:
        axel_amount = float(input("How much did Axel pay you?\n"))
        income_dict["Axel"] += axel_amount


def expenditure():
    categories = ["1.Bills", "2.Car", "3.Kids", "4.Food", "5.Other"]
    print("Please chose the category by selecting the number.\n")
    print()
    time.sleep(2)
    for item in categories:
        print(item, end="   ")
        time.sleep(1)
    category_input = int(input())
    if category_input == 1:
        bill_amount = float(input("Please add the amount of bills paid.\n"))
        passive_dict["Bills"] += bill_amount
    elif category_input == 2:
        car_amount = float(input("How much did you spend on the car?\n"))
        passive_dict["Car"] += car_amount
    elif category_input == 3:
        kids_amount = float(input("How much did you spend on the kids?\n"))
        passive_dict["Kids"] += kids_amount
    elif category_input == 4:
        food_amount = float(input("How much did you spend on food?\n"))
        passive_dict["Food"] += food_amount
    else:
        other_amount = float(input("How much did you pay for other expenditures?\n"))
        passive_dict["Other"] += other_amount

if starting_question.lower().strip() == "income":
    income()
    while True:
        question = input("Would you like to add more? y/n\n")
        if question.lower() == "y" or question.lower() == "yes":
            income()
        else:
            break
    questi = input("Would you like to add expenditures or exit program? Add/Exit")
    if questi.lower().strip() == "Add":
        expenditure()
elif starting_question.lower().strip() == "expenditure":
    pass

print(income_dict)
