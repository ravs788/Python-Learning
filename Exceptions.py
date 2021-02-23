def divide(x, y):
    try:
        result = x/y
        print(" X divided by y: ",result)
    except ZeroDivisionError:
        print(" The result is infinity")
    else:
        print("Division successful")
    try:  
        raise NameError("Hi there")  # Raise Error 
    except NameError: 
        print("An exception")
divide(3,2)
# divide(3, 0)
