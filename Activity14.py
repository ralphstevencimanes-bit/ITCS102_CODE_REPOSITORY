age = int(input("Put your Age ---->  "))
is_employed = bool(input("Are you currently employed (True/False)---> "))
credit_score = int(input("Put your creditscore ----> "))
annual_income = float(input("how much your anual income --->  "))
has_collateral = bool(input("Do you have an collateral (True/False) ---->  "))   

base_rate = 0.0 

if age >= 21 and is_employed == True:
    print("You are qualified")

   #Tier 1 
if credit_score >= 750:
    if annual_income >= 110000:
        interest_rate = 4.5
    elif annual_income >= 50000:
        ineterest_rate = 5.0

    print("Approved: ", ineterest_rate, "% interest rate")

    #Tier 2
elif credit_score >= 600 and credit_score < 750:
    if has_collateral == True:
        interest_rate = 7.0
    elif annual_income <= 50000:
        interest_rate = 9.5
    else:
        interest_rate = 8.0

    print("Approved: ", interest_rate< "% interest rate")

    #Tier 3 
elif credit_score < 600:
       print("Rejected: Your credit score is too low for a loan.") 

else:
      print("Rejected: You are not eligible for a loan.")          
