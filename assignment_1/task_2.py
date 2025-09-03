grocery = []
while True:
    user_input=input("Enter a word to add or remove ")
    print("press 1 for Add, 2 for Remove and 3 for Quit")
    user_choice = int(input("which feature are you going to use "))
    
    if user_choice > 3 or user_choice < 0:
        print("Invalid! please select number from above options")
        
    elif user_choice == 1:
        grocery.append(user_input)
        print(user_input, "is added on the list")
        
    elif user_choice == 2:
        if user_input in grocery:
            grocery.remove(user_input)
            print(user_input, "is removed from the list")
        else:
            print("no such item in the list")
    else:
        total = len(grocery)
        print("there are", total, "number of item in the list")
        break
    