''' calculate which number is largest '''

# finds which of 2 numbers is larger
def max_of_two( x, y ):
    if x > y:
        return x
    return y

# finds which of 3 numbers is largest
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )

# tests 3 numbers to see which is largest
print(max_of_three(3, 6, -5))