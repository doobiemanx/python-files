print("    How much money do you have after taxes    ")

running = True
while True:

    income = float(input("Enter your income: "))

    if income <= 67000 :
        taxes =  income * 0.24

    elif income <= 97000 :
        taxes = income * 0.31

    else:
        taxes = income * 0.34

    income_after_taxes = income - taxes

    print(f"Your income after taxes is {income_after_taxes:.2f} euros")

