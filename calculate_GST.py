'''calculate GST of a price '''

GST_RATE = 15


# calculate and show GST of given price
def show_gst(my_price) :
    print("The item costs ${} and the GST component is ${}".format(my_price,my_price*GST_RATE/100))
    
    
# find GST for the price supplied by the user

price = int(input("Enter a price: "))
show_gst(price)
