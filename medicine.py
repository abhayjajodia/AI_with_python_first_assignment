
age = int(input("Enter patient's age: "))


if age >= 18:
    print("Medicine can be given.")


elif age >= 15:
    weight = float(input("Enter patient's weight (kg): "))
    if weight >= 55:
        print("Medicine can be given.")
    else:
        print("Medicine cannot be given.")


else:
    print("Medicine cannot be given.")