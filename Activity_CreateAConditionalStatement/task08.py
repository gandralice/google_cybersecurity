#Now you'll write another conditional statement. This one will use a organization_hours variable 
#to check if the user logged in during specific organization hours. When that condition is met, 
#the code should display the string "Login attempt made during organization hours.". When that 
#condition isn't met, the code should display the string "Login attempt made outside of organization 
#hours."

organization_hours = True  # Try changing to False

if organization_hours:
    print("Login attempt made during organization hours.")
else:
    print("Login attempt made outside of organization hours.")