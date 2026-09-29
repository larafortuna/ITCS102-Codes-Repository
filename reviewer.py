age = int(input("AGE ---> "))
rev = float(input("REVENUE ---> "))
cc = int(input("Credit Score ---> "))
yrs = float(input("Years of Business ---> "))
has_df = bool(input("File for Bankruptcy ---> "))
colla = input("Collateral Name ---> ")
c_val = float(input("Collateral Value ---> "))

ml = 0
bf = 0 

if age >= 21 and yrs >= 2.0 and has_df == False:
    print("BASELINE PASSED")
    if cc >= 720:
        ml = rev * 3
        print("MAXIMUM LOANABLE AMOUNT IS SET TO", ml)
        print("HIGH CREDIT SCORE")
        if rev >= 50000:
            print("REVENUE HIGHER THAN 50k" )
            bf = ml * 0.015
            print("BASE FEE US SET TO", bf)
        else:
            print("REVENUE LOWER THAN 50k")
            bf = ml * 0.025
            print("BASE FEE RATE IS SET TO", bf)

            #collateral
            if c_val >= ml:
                print("Collateral", colla, "with a value of ", c_val, "is ACCEPTED")
            else:
                print("Rejected: Insufficient collateral value for ", colla)

                #surcharge
                sfr = ml * bf
                print("Additional charge of", sfr)
                if ml % 500 != 0:
                    print("Additional Charge added")
                    sfr += 250
                    print("Updated base fee is ", sfr)

    elif cc >= 620 and cc <720: #TIER2
        print("Credit Score within range of 620 to 720")
        ml = rev * 1.5
        print("Maximum Loan for this credit score is", ml)
        if yrs >= 5:
            print("Business year more than 5 years")
            bf = ml * 0.02
            print("Base fee rate is set to", bf)
        else:
            print("Business year less than 5 years")
            bf = ml * 0.035
            print("Base fee rate is set to", bf)

    elif cc <= 620:
        print("Rejected: Credit score below requirement")
    else:
        print("INVALID")
else:
        print("BASELINE FAILED")