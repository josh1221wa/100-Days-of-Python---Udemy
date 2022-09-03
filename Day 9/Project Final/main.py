import os
import art

def find_highest(dictionary):
    highest = 0
    for key in dictionary:
        if dictionary[key] > highest:
            highest = dictionary[key]
            break
    return key, highest

print(art.logo)
offers = {}

while True:
    name = input("Enter bidder's name: ")
    price = int(input("Enter bidder's offer: "))
    offers[name] = price
    if input("Are there anymore bidders? Input yes or no: ")=="no":
        break
    else:
        os.system('cls')
        
os.system('cls')
h_name, h_offer = find_highest(offers)
print(f"Winner is {h_name} with offer value {h_offer}!")