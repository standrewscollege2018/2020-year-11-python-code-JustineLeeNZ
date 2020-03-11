""" Shows how to use try-except for error handling. """

keep_asking = True

while keep_asking == True:
    try:
        age = int(input("Enter your age: "))
        keep_asking = False
    except:
        print("Enter a valid integer")
print(age)