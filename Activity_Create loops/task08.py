#You would like to incorporate a message that displays Only 10 valid employee ids remaining as a 
#helpful alert once the loop variable reaches 5100.To do so, include an if statement in your code.

i = 5000

while i <= 5150:
    print(i)
    if i == 5100:
        print("Only 10 valid employee ids remaining")
    i = i + 5