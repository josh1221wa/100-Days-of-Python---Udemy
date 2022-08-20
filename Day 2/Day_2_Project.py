print('Welcome to the tip calculator.')
bill_amt = float(input('What was the total bill? $'))
tip = int(input("What percent tip would you like to give?10, 12 or 15? "))
people_num = int(input('How many people to split the bill? '))

split_amt = (bill_amt / people_num)
split_amt += (split_amt * (tip / 100))

print('Each person should pay $', round(split_amt, 2))