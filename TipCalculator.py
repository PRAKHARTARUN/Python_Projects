#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


print("Welcome to tip calculator")
bill = float(input("what was the total bill? $"))
percent = int(input("Percent of tip would you like to give 10,12 or 15? "))
people = int(input("How many people to split the bill?"))
total_money = percent/100*bill +bill
money = round(total_money/people,2)
print(f"Each person should pay : ${money}")
