

def report(resource):
    for key, value in resource.items():
        if key.lower() == "coffee":
            print(f"{key.title()}: {value}g")
        elif key.lower() == "money":
            print(f"{key.title()}: ${value}")
        else:
            print(f"{key.title()}: {value}ml")


def enoughResources(resource, drink):
    for resourceKey, resourceVal in resource.items():
        for ingredientsKey, ingredientsVal in drink["ingredients"].items():
            if resourceKey == ingredientsKey and resourceVal < ingredientsVal:
                print(f"Sorry there is not enough {ingredientsKey}")
                return False
    return True


def totalAmt(quarter, dime, nickel, penny):
    return round(quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01, 2)


def brew(resource, drink):
    for resourceKey, resourceVal in resource.items():
        for ingredientsKey, ingredientsVal in drink["ingredients"].items():
            if resourceKey == ingredientsKey:
                resource[resourceKey] = resourceVal - ingredientsVal
    resource["money"] += drink["cost"]