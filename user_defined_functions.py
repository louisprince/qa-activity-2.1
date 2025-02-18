#!/bin/python3

# Personal allowance:£11,850
PERSONAL_ALLOWANCE = 11850

def get_income_tax(salary):
    # 0 to 34,500 taxed at 20%
    if salary < 34500:
        income_tax = (salary - PERSONAL_ALLOWANCE) * .2
        return f"£{income_tax:.2f}"

    # 34,501 to 150,000 taxed at 40%
    elif 34500 < salary < 150000:
        income_tax = (salary - PERSONAL_ALLOWANCE) * .4
        return f"£{income_tax:.2f}"

    # Over 150,000 taxed at 45%
    elif salary > 150000:
        income_tax = (salary - PERSONAL_ALLOWANCE) * .45
        return f"£{income_tax:.2f}"

print(get_income_tax(22275))
print(get_income_tax(47500))
print(get_income_tax(199999))