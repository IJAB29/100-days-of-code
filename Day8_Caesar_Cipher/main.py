import cipher

cipher.caesar()

option = input("Do you want to go again? 'yes' or 'no'\n").lower()
while option != "yes" and option != "no":
    print("Invalid input!")
    option = input("Do you want to go again? 'yes' or 'no'\n").lower()

while option != "no":
    cipher.caesar()
    option = input("Do you want to go again? 'yes' or 'no'\n").lower()
