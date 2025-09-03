shopping_list = [10,14,22,33,44,13,22,55,66,77]

while True:
    user_choice = int(input("Please enetr the order number from (1-10) or 0 to exit"))
    
    if user_choice == 0:
        total = sum(shopping_list)
        print("Total: ",total)
        user_payment = int(input("what is the payment"))
        if user_payment > total:
            print("change", user_payment - total)
        else:
            print("insufficent amount")
        break
    
    
    elif user_choice > 10:
        print("Shopping list has only 10 item, please choose from 1-10")
        
    else:
        print("Product: ", user_choice, "Price: ", shopping_list[user_choice -1 ])
        
        
        
        