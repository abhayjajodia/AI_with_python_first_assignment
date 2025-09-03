def askString():
    while True:
        user_input = input("Write something. (quit for end)").lower()
        if user_input == 'quit':
            break
        else:
            tester(user_input)
def tester(given_string):
    if len(given_string) < 10:
        given_string = "Too short"
    print(given_string)
    
askString()