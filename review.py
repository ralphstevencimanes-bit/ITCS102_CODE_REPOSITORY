age = int(input("AGE ---> "))
rev = float(input("REVENUE --->"))
cc = int(input("CREDIT SCORE ---> "))
yrs = float(input("YEARS OF BUSINESS --> "))
has_defaults = bool(input("FILE FOR BANCRUPTCY --->"))
collateral = input("COLLATERAL NAME ---> ")
c_value = float(input("COLLATERAL VALUE ---> "))



max_loan = 0
base = 0

if age >= 21 and yrs >= 2.0 and has_defaults == False:
    print("BASELINE PASSEED") 
    if cc >= 720: #Tier1      
        max_loan = rev * 3
        print("Maximum Loanable amount is set to", max_loan)
        print("high credit score")
        if rev >= 5000:
            rate = 1.5 
            base = max_loan * 0.015
            print("you are qualified with a rate of, rate")
            print("Base rate is too", base)

#collateral 
        if collateral >= max:
            print("Your collateral", collateral, " with a value of", c_value, " is accept")
        else:
            print("Revenue less than 50k")
            base = max_loan * 0.025
            print("base fee rate is set to", base)
#supercharge
                surge = max_loan * base
            if max & 500 != 0:
                print("you have a additional charge")
                surge += 250
                print("updated base fee is", base)
    
    else:
        print("INVALID")                  

        
else:
    print("BASELINE FAILED")