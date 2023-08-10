print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? "))/100
people = float(input("How many people to split the bill? "))
print(f"Each person should pay ${round((bill + bill*percentage)/people, 2)}")
