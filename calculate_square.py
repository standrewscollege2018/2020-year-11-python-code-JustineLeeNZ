''' returns the sqaure of a number '''

def calculate_square(my_number) :
    answer = my_number * my_number
    return answer

# get number from user
number = int(input("Enter a number to square: "))

# calculate and display squared value
print(calculate_square(number))
