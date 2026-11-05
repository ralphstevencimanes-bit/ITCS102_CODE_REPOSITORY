s = 0
t = True

while t == True:
    a = int(input("enter a number ---> "))

    if a == 0:
        print("Loop terminated")
        print("Total of all numbers is ", s)
        break

    else:
        print("Continue Loop")
        s += a 
        print("Current total is ", s)
        continue