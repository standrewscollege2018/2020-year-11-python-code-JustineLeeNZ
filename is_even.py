''' determines if a number is even or odd '''

# takes a number and says if it is even or odd
def isEven(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
        
        
test_number = int(input("Enter a positive integer: "))
isEven(test_number)

test_number = int(input("Enter a positive integer: "))
isEven(test_number)
