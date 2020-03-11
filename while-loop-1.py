# set Boolean to True
keep_asking = True

# Start asking their name
while keep_asking == True:
    name = input("Enter your name")
    if name == "Ashton":
        keep_asking = False
        print("cool name")
    else:
        print("Wrong name")
        
        
# Loop finished, so greet Ashton
print("Hi Ashton")
