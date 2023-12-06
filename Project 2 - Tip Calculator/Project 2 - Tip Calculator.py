# TIP CALCULATOR
print("Welcome, to the tip calculator.")
total_bill = input("What was the total bill? $")
float_total_bill = float(total_bill)
tip_percent = input("What percentage tip would you like to give? 10, 12 or 15?")
float_tip_percent = float(tip_percent)
total_people = input("How many people to split the bill")
float_total_people = float(total_people)
tip_amount = round((((float_tip_percent / 100) * float_total_bill) +
                    float_total_bill) / float_total_people, 2)
print(f'Each person should pay ${tip_amount}')
