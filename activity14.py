# age (integer)
# is_employed (boolean)
# credit score (integer)
# annual_income (float)
# has collateral (boolean)

age = int(input("Enter your age ---> "))
is_employed = bool(input("Are you currently employed (True/False) --->  "))
credit_score = int(input("Credit score --> "))
annual_income = float(input("What is your annual salary --> "))
has_collateral = bool(input("Do you have any collateral (True/False) ---> "))

base_rate = 0.0

#BASELINE REQUIREMENT
if age >= 21 and is_employed == True:
    print("---- Applicant passed baseline requirement ----")

    #TIER1
    if credit_score >= 750:
        print("\t\tYou have a high credit score")
        base_rate = 5.0

        if annual_income >= 100000:
            base_rate = 4.5
            print("\t\tYour interest rate is", base_rate, "%")
        else:
            print("\t\tYour interest rate is", base_rate, "%")

    #TIER2
    elif credit_score >= 600 and credit_score < 750:
        print("\t\tYou have a fair credit score")
        base_rate = 8.0

        if has_collateral == True:
            base_rate = 7.0
            print("\t\tYou have collateral")
            print("\t\tYour interest rate is", base_rate, "%")

        elif annual_income < 40000:
            base_rate = 9.5
            print("\t\tYour annual income is below 40,000")
            print("\t\tYour interest rate is", base_rate, "%")

        else:
            print("\t\tYour interest rate is", base_rate, "%")

    #TIER3
    else:
        print("\t\tRejected: Credit score too low")

#FAILED BASELINE
else:
    print("\t\tRejected: Fails baseline criteria")
