#to take user input in kilos or pounds
user_weight=int(input("Enter your weight:"))
user_unit=input(("(L)lbs or (K)kg :"))

# conditionals to convert weight
if user_unit.upper() == "L":
    final_weight=user_weight*0.45
    print(f"You are {final_weight} kilograms")
elif user_unit.upper() =="K":
    final_weight = user_weight / 0.45
    print(f"You are {final_weight} pounds")
else:
    print ("Wrong unit entered")