 #age (integer)
 #is_employed (boolean)
 #credit score (integer)
 #annual_income (float)
 #has collateral (boolean)

age = int(input("Enter your age ---> "))
is_employed = bool(input("Are you currently employed (True/False) ---> "))
credit_score = float(input("Credit score --> "))
annual_income = float(input("What is your annual salary --> "))
has_collateral = bool(input("Do you have any collateral (True / False ) --> "))

base_rate = 0.0

if age >= 21 and is_employed -- True:
    print("Applicant pass baseline requirement")
    if credit_score >= 750: #TIER1
        print("You have a high credit score")
        if annual_income >- 100000:
            base_rate = 4.5
            print("You have a high salary and high credit score, your interest rate is",base_rate)
        else:
            base_rate = 5.0
            print("You have a high salary and high credit score, your interest rate is",base_rate)
    else:
            print("failed")
else:
    print("Rejected: Fails baseline criteria")

    base_rate = 8.0

            #elif credit_score >= 600 and credit_score < 750: #tier2
            #if has_collateral == True:
            #print("Your credit score is less than 750, your interest rate is", base_rate)     
#else:
        #print("Rejected: Fails baseline criteria")
