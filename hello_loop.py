''' uses for loop to repeatedly ask user for name, then print Hello + name ''' 

# ask user how many names to ask for
total_names = int(input("How many names do you wish to enter? "))


# loop number of times specified by user
for count in range(0,total_names) :
    name = input("Enter a name: ")
    print("Hello {}".format(name))
    
