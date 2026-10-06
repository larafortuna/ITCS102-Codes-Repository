#   
import getpass  
  
username = input('Please enter your username to continue: ')  
if username != 'theyvid':  
    print('Incorrect username. Access denied.')  
    exit()  
  
  
password = getpass.getpass('Please enter your password to continue: ')  
if password != 'davidmapagmahal':  
    print('Incorrect password. Access denied.')  
    exit()  
  
owner_age = int(input('What is your age? --> '))  
  
if owner_age not in range(18, 101):  
    print('Invalid input for age. Please enter an age between 18 and 100.')  
    exit()  
  
monthly_revenue = float(input('How much is your monthly revenue? --> '))  
credit_score = int(input('What is your credit score? --> '))  
years_in_business = float(input('How long is your business running? --> '))  
has_defaults = bool(input('Did you file for bankruptcy? --> (True/Leave blank for False) '))  
  
if has_defaults not in [True, False]:  
    print('Invalid input for bankruptcy. Please enter True or False.')  
    exit()  
      
collateral_name = input('What is your collateral? --> ')  
collateral_value = float(input('How much is the value of your collateral? --> '))  
  
max_loan = 0.0  
base_fee_rate = 0.0  
surcharge_fee_rate = 0.0  
  
if owner_age >= 21 and years_in_business >= 2 and has_defaults == False:  
    print('YOU PASSED THE BASELINE REQUIREMENTS')  
    if credit_score >= 720:  
        max_loan = monthly_revenue * 3  
        print ('YOU HAVE A MAX LOAN OF', max_loan)  
        if monthly_revenue >= 50000:             
            base_fee_rate = max_loan * 0.015  
            print('YOU HAVE A BASE FEE RATE OF', base_fee_rate)  
        else:  
            base_fee_rate = max_loan * 0.025  
            print('YOU HAVE A BASE FEE RATE OF', base_fee_rate)  
  
        if collateral_value >= max_loan:  
            print('YOUR COLLATERAL VALUE IS GREATER THAN YOUR MAX LOAN')  
        else:  
            print('Rejected: Insufficient collateral value for', collateral_name)  
  
        surcharge_fee_rate = base_fee_rate * max_loan  
        if int(collateral_value) % 5000 != 0:  
            print('YOU WILL HAVE AN ADDITIONAL FEE')  
            surcharge_fee_rate += 250  
            print(' YOUR ADDED FEE IS', surcharge_fee_rate)  
  
    elif 620 <= credit_score < 720:  
        max_loan = monthly_revenue * 1.5  
        print ('YOU HAVE A MAX LOAN OF', max_loan)  
        if years_in_business >= 5:  
            base_fee_rate = max_loan * 0.02  
            print('YOU HAVE A BASE FEE RATE OF', base_fee_rate)  
        else:  
            base_fee_rate = max_loan * 0.035  
            print('YOU HAVE A BASE FEE RATE OF', base_fee_rate)  
  
        if collateral_value >= max_loan:  
            print('YOUR COLLATERAL VALUE IS GREATER THAN YOUR MAX LOAN')  
        else:  
            print('Rejected: Insufficient collateral value for', collateral_name)  
  
        surcharge_fee_rate = base_fee_rate * max_loan  
        if int(collateral_value) % 5000 != 0:  
            print('YOU WILL HAVE AN ADDITIONAL FEE')  
            surcharge_fee_rate += 250  
            print('YOUR ADDED FEE IS', surcharge_fee_rate)  
  
    elif credit_score < 620:  
        print('YOUR CREDIT SCORE IS TOO LOW')  
  
    else:  
        print('INVALID ')               
else:  
    print('YOU DID NOT PASS THE BASELINE REQUIREMENTS')  
  
print("")  
print('===============================')  
print('SUMMARY OF YOUR LOAN APPLICATION')  
print('===============================')  
print('Username:', username)  
print('Password:', '*' * len(password))  
print('Owner Age:', owner_age)  
print('Monthly Revenue:', monthly_revenue)  
print('Credit Score:', credit_score)  
print('Years in Business:', years_in_business)  
print('Has Defaults:', has_defaults)  
print('Collateral Name:', collateral_name)  
print('Collateral Value:', collateral_value)  
print('Max Loan:', max_loan)  
print('Base Fee Rate:', base_fee_rate)  
print('Surcharge Fee Rate:', surcharge_fee_rate)  
print('Total Fees:', base_fee_rate + surcharge_fee_rate)  
print('===============================')  
