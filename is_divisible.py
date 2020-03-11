''' determines if a number a is divisible by number b '''

# takes 2 numbers and says the first is divisible by the second
def is_divisible(number1, number2):
    if number1 % number2 == 0:
        print("{} IS divisible by {}".format(number1, number2))
    else:
        print("{} IS NOT divisible by {}".format(number1, number2))
        
        
test_number1 = int(input("Enter first positive integer: "))
test_number2 = int(input("Enter second positive integer: "))
is_divisible(test_number1, test_number2)
