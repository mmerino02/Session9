def greet():
    print("Hello dear, hope you're doing fine")
    # pass  # Do nothing. Useful to suspend for a while to code later

for i in range(10): # Prints it 10 times
    print(f"{i+1} ", end="") #number the lines
    greet()

#A simple function has not imput nor output parameter

x = greet()
print(x) # if it gives you none the function is giving you nothing
