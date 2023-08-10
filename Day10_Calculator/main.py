def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operations = {"+": add, "-": sub, "*": mul, "/": div}


def calculator():
    first = float(input("What is the first number? "))
    for i in operations:
        print(i)

    goAgain = True
    while goAgain:
        opeSymbol = input("Pick an operation from above. ")
        second = float(input("What is the second number? "))
        answer = operations[opeSymbol](first, second)

        print(f"{first} {opeSymbol} {second} = {answer}")

        again = input(f"Do you want to do operations on {answer}? 'yes' or 'no'\n")
        while again != "no" and again != "yes":
            print("Invalid input!")
            again = input(f"Do you want to do operations on {answer}? 'yes' or 'no'\n")

        if again == "yes":
            first = answer
        else:
            goAgain = False
            calculator()


calculator()