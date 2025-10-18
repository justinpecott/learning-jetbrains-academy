import argparse
import math

ANNUITY = "annuity"
DIFF = "diff"
valid_types = [ANNUITY, DIFF]

parser = argparse.ArgumentParser(description="Sweet loan calculator.")
parser.add_argument("--type", help="Type of calculation to use - annuity or diff")
parser.add_argument("--payment", help="Monthly payment amount")
parser.add_argument("--principal", help="Loan principal")
parser.add_argument("--periods", help="Payment periods in months")
parser.add_argument("--interest", help="Interest rate")

args = parser.parse_args()
parameter_count = 0
negative_value = False

if args.type != None:
    parameter_count += 1

if args.payment != None:
    parameter_count += 1
    negative_value = negative_value or (float(args.payment) < 0)

if args.principal != None:
    parameter_count += 1
    negative_value = negative_value or (float(args.principal) < 0)

if args.periods != None:
    parameter_count += 1
    negative_value = negative_value or (int(args.periods) < 0)

if args.interest != None:
    parameter_count += 1
    negative_value = negative_value or (float(args.interest) < 0)

if (parameter_count < 4) or negative_value or args.type not in valid_types or (args.type == DIFF and args.payment):
    print("Incorrect parameters")
    exit
elif args.type == DIFF:
    loan_principal = float(args.principal)
    periods = int(args.periods)
    loan_interest = float(args.interest)

    nominal_interest_rate = loan_interest / (12 * 100)

    payments = []
    for i in range(1, periods + 1):
        pp = loan_principal / periods
        payment = pp + nominal_interest_rate * (loan_principal - pp * (i - 1))
        payments.append(math.ceil(payment))
    
    counter = 1
    for payment in payments:
        print("Month {}: payment is {}".format(counter, payment))
        counter += 1

    overpayment = math.ceil(sum(payments) - loan_principal)
    print()
    print("Overpayment = {}".format(overpayment))

elif args.periods == None:
    loan_principal = float(args.principal)
    monthly_payment = float(args.payment)
    loan_interest = float(args.interest)

    nominal_interest_rate = loan_interest / (12 * 100)
    x = monthly_payment / (monthly_payment - (nominal_interest_rate * loan_principal))
    total_months = math.ceil(math.log(x, 1 + nominal_interest_rate))
    years = total_months // 12
    months = total_months % 12

    months_str = "{} month".format(months) + ("" if months == 1 else "s")
    years_str = "{} year".format(years) + ("" if years == 1 else "s")
    if years == 0:
        msg = "It will take {} to repay this loan!".format(months_str)
    elif months == 0:
        msg = "It will take {} to repay this loan!".format(years_str)
    else:
        msg = "It will take {} and {} to repay this loan!".format(years_str, months_str)

    print(msg)

    overpayment = math.ceil((total_months * monthly_payment) - loan_principal)
    print("Overpayment = {}".format(overpayment))

elif args.principal == None:
    periods = int(args.periods)
    monthly_payment = float(args.payment)
    loan_interest = float(args.interest)
    
    nominal_interest_rate = loan_interest / (12 * 100)
    x = math.pow(1 + nominal_interest_rate, periods)
    loan_principal = monthly_payment / ((nominal_interest_rate * x) / (x - 1))
    rounded_loan_principal = int(loan_principal)
    
    print("Your loan principal = {}!".format(rounded_loan_principal))

    overpayment = math.ceil((periods * monthly_payment) - loan_principal)
    print("Overpayment = {}".format(overpayment))

elif args.payment == None:
    loan_principal = float(args.principal)
    periods = int(args.periods)
    loan_interest = float(args.interest)

    nominal_interest_rate = loan_interest / (12 * 100)
    x = math.pow(1 + nominal_interest_rate, periods)
    monthly_payment = loan_principal * (nominal_interest_rate * x) / (x - 1)
    rounded_monthly_payment = math.ceil(monthly_payment)
    
    print("Your monthly payment = {}!".format(rounded_monthly_payment))

    overpayment = math.ceil((periods * rounded_monthly_payment) - loan_principal)
    print("Overpayment = {}".format(overpayment))

else:
    print('Something went wrong here')