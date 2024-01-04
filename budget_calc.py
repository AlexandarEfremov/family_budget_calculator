income_dict = {"Salary": 0, "Rent": 0, "Italki": 0, "Axel": 0}
passive_dict = {"Bills": 0, "Car": 0, "Kids": 0, "Food": 0, "Other": 0}

import time
import sys, subprocess


def clearing():
    subprocess.run("clear", shell=True)
def starting_question():
    while True:
        answer = input("Are you adding income or expense?\n")
        if answer.lower() == "expense" or answer.lower() == "income":
            return answer.lower()
        else:
            print("Invalid input, try again.")


clearing()
answer = starting_question()


def income():
    categories = ["1.Salary", "2.Rent", "3.Italki", "4.Axel"]
    print("Please choose the category by selecting the number.\n")
    time.sleep(2)
    for item in categories:
        print(item, end="   ")
        time.sleep(1)
    print()
    category_input = int(input())
    clearing()
    if category_input == 1:
        salary_amount = float(input("How much salary did you get?\n"))
        income_dict["Salary"] += salary_amount
        print()
        print(f"{salary_amount:.2f} BGN added. "
              f"New total: {income_dict['Salary']:.2f}")
    elif category_input == 2:
        rent_amount = float(input("How much rent would you like to add?\n"))
        income_dict["Rent"] += rent_amount
        print()
        print(f"{rent_amount:.2f} BGN added. "
              f"New total: {income_dict['Rent']:.2f}")
    elif category_input == 3:
        italki_amount = float(input("How much did you make on Italki?\n"))
        income_dict["Italki"] += italki_amount
        print()
        print(f"{italki_amount:.2f} BGN added. "
              f"New total: {income_dict['Italki']:.2f}")
    elif category_input == 4:
        axel_amount = float(input("How much did Axel pay you?\n"))
        income_dict["Axel"] += axel_amount
        print()
        print(f"{axel_amount:.2f} BGN added. "
              f"New total: {income_dict['Axel']:.2f}")


def expenditure():
    categories = ["1.Bills", "2.Car", "3.Kids", "4.Food", "5.Other"]
    print("Please choose the category by selecting the number.\n")
    time.sleep(2)
    for item in categories:
        print(item, end="   ")
        time.sleep(1)
    print()
    category_input = int(input())
    if category_input == 1:
        bill_amount = float(input("Please add the amount of bills paid.\n"))
        passive_dict["Bills"] += bill_amount
        print()
        print(f"{bill_amount:.2f} BGN added. "
              f"New total: {passive_dict['Bills']:.2f}")
    elif category_input == 2:
        car_amount = float(input("How much did you spend on the car?\n"))
        passive_dict["Car"] += car_amount
        print()
        print(f"{car_amount:.2f} BGN added. "
              f"New total: {passive_dict['Car']:.2f}")
    elif category_input == 3:
        kids_amount = float(input("How much did you spend on the kids?\n"))
        passive_dict["Kids"] += kids_amount
        print()
        print(f"{kids_amount:.2f} BGN added. "
              f"New total: {passive_dict['Kids']:.2f}")
    elif category_input == 4:
        food_amount = float(input("How much did you spend on food?\n"))
        passive_dict["Food"] += food_amount
        print()
        print(f"{food_amount:.2f} BGN added. "
              f"New total: {passive_dict['Food']:.2f}")
    elif category_input == 5:
        other_amount = float(input("How much did you pay for other expenditures?\n"))
        passive_dict["Other"] += other_amount
        print()
        print(f"{other_amount:.2f} BGN added. "
              f"New total: {passive_dict['Other']:.2f}")


if answer == "income":
    income()
    while True:
        question = input("Would you like to add more? y/n\n")
        clearing()
        if question.lower().strip() == "y" or question.lower().strip() == "yes":
            income()
        elif question.lower().strip() == "n" or question.lower().strip() == "no":
            break
        else:
            print("Invalid input, try again:")

    quest_two = input("Would you like to add expenditures or exit program? Add/Exit\n")
    if quest_two.lower().strip() == "add":
        expenditure()
        while True:
            question = input("Would you like to add more? y/n\n")
            clearing()
            if question.lower().strip() == "y" or question.lower().strip() == "yes":
                expenditure()
            elif question.lower().strip() == "n" or question.lower().strip() == "no":
                break
            else:
                print("Invalid input, try again:")

    else:
        print(income_dict)
        print(passive_dict)
        exit()


elif answer == "expense":
    expenditure()
    while True:
        question = input("Would you like to add more? y/n\n")
        clearing()
        if question.lower().strip() == "y" or question.lower().strip() == "yes":
            expenditure()
        elif question.lower().strip() == "n" or question.lower().strip() == "no":
            break
        else:
            print("Invalid input, try again:")

    quest_two = input("Would you like to add income or exit program? Add/Exit\n")
    if quest_two.lower().strip() == "add":
        income()
        while True:
            question = input("Would you like to add more? y/n\n")
            clearing()
            if question.lower().strip() == "y" or question.lower().strip() == "yes":
                income()
            elif question.lower().strip() == "n" or question.lower().strip() == "no":
                break
            else:
                print("Invalid input, try again:")
    else:
        print(income_dict)
        print(passive_dict)
        exit()

print(income_dict)
print(passive_dict)
