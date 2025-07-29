
# Entered number is even or odd

user_input = input("Enter number:")

if user_input.isdigit():
    user_input = int(user_input)
    if user_input%2==0:
        print(str(user_input) +" is even")
    else:
        print(str(user_input) +" is odd")
        
else:
    print("Please enter number only")
    

    
    
# Multiway Simple Code

num = 44

if num <= 2:
    print("less then or equal to 2")
elif num <= 10:
    print("less then or equal to 10")
elif num <= 50:
    print("less then or equal to 50")
elif num <= 100:
    print("less then or equal to 100")
else:
    print("Something else") 
    



