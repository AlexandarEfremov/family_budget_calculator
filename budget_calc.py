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


def saldo_calc(dictionary):
    total_sum = sum(dictionary.values())
    return total_sum


def net_balance(inflow, outflow):
    inflow_sum = sum(inflow.values())
    outflow_sum = sum(outflow.values())
    if inflow_sum > outflow_sum:
        net_positive = inflow_sum - outflow_sum
        result = f"\033[{92}mYour balance is {net_positive}\033[0m."
        return result
    else:
        net_negative = inflow_sum - outflow_sum
        second_result = f"\033[{91}mYou're {net_negative} in debt.\033[0m"
        return second_result

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
        question = input("Would you like to add more? (y/n)\n")
        clearing()
        if question.lower().strip() == "y" or question.lower().strip() == "yes":
            income()
        elif question.lower().strip() == "n" or question.lower().strip() == "no":
            break
        else:
            print("Invalid input, try again:")

    quest_two = input("Would you like to add expenditures or exit program? (Add/Exit)\n")
    if quest_two.lower().strip() == "add":
        expenditure()
        while True:
            question = input("Would you like to add more? (y/n)\n")
            clearing()
            if question.lower().strip() == "y" or question.lower().strip() == "yes":
                expenditure()
            elif question.lower().strip() == "n" or question.lower().strip() == "no":
                break
            else:
                print("Invalid input, try again:")
        quest_two = input("Would you like to add income or exit program? (Add/Exit)\n")
        if quest_two.lower().strip() == "add":
            income()
            while True:
                question = input("Would you like to add more? (y/n)\n")
                clearing()
                if question.lower().strip() == "y" or question.lower().strip() == "yes":
                    income()
                elif question.lower().strip() == "n" or question.lower().strip() == "no":
                    break
                else:
                    print("Invalid input, try again:")


elif answer == "expense":
    expenditure()
    while True:
        question = input("Would you like to add more? (y/n)\n")
        clearing()
        if question.lower().strip() == "y" or question.lower().strip() == "yes":
            expenditure()
        elif question.lower().strip() == "n" or question.lower().strip() == "no":
            break
        else:
            print("Invalid input, try again:")

    quest_two = input("Would you like to add income or exit program? (Add/Exit)\n")
    if quest_two.lower().strip() == "add":
        income()
        while True:
            question = input("Would you like to add more? (y/n)\n")
            clearing()
            if question.lower().strip() == "y" or question.lower().strip() == "yes":
                income()
            elif question.lower().strip() == "n" or question.lower().strip() == "no":
                break
            else:
                print("Invalid input, try again:")

clearing()
print(f"Total income: {saldo_calc(income_dict):.2f} BGN")
breakdown = list(f"{x}: {y:.2f}" for x, y in income_dict.items())
print(", ".join(breakdown))
print()
print(f"Total expenses: {saldo_calc(passive_dict):.2f} BGN")
breakdown_passive = list(f"{x}: {y:.2f}" for x, y in passive_dict.items())
print(", ".join(breakdown_passive))
print()
enter_command = input("Press ENTER when ready to view net balance.")
if enter_command == "":
    clearing()
    print()
    print("Netto balance:")
    print()
    print(net_balance(income_dict, passive_dict))
