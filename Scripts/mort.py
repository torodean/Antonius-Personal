#!/bin/python3

import matplotlib.pyplot as plt

# ============================================================
# SETTINGS
# ============================================================

YEARS = 5
MONTHS = YEARS * 12
monthly_income = 7451.99 + 3900
monthly_income = monthly_income * 0.8
emergency_fund = 20000
chikfila_settlement = 0
selling_tn_land = 50000
redfin_benefit = True
mandatory_points = 4000

# -----------------------
# Renting
# -----------------------

monthly_rent = 1113

# List of monthly expenses
rent_misc = [
     75,   # Cable package 
     10,   # Trash
    150,   # water
    200,   # electric
      5,   # Rent fees
   1600,   # food
    400,   # transportation
    150,   # car insurance
      5,   # rental insurance
    500,   # misc spending
]

# -----------------------
# Mortgage
# -----------------------

house_price = 350000
down_payment = 200000
closing_costs = 20000
renting_income = 0
monthly_house_taxes = 750

annual_interest = 0.0699
loan_years = 30

monthly_extra_principal = 0

mortgage_misc = [
    150,   # Cable and internet 
     20,   # Trash
    200,   # water
    350,   # electric
     50,   # gas
   1600,   # food
    800,   # transportation
    150,   # car insurance
    400,   # rental insurance
   1000,   # misc spending
    210*2/12, # phone
]

# ============================================================
# Mortgage payment calculation
# ============================================================

def calculate_mortgage_payment(loan, r, n):
    """
    Calculates the required monthly mortgage payment.

    Parameters:
        loan (float): Amount borrowed.
        monthly_interest_rate (float): Monthly interest rate as a decimal.
        n (int): Total number of monthly payments.

    Returns:
        float: Required monthly payment.
    """

    payment = (
        loan * r * (1 + r) ** n
    ) / ((1 + r) ** n - 1)

    return payment

loan = house_price - down_payment + closing_costs
r = annual_interest / 12
n = loan_years * 12

minimum_payment = calculate_mortgage_payment(loan, r, n)

# ============================================================
# Renting Simulation
# ============================================================

rent_waste = []
rent_savings = []

# Add initial savings fund.
rent_total_waste = 0
rent_total_savings = emergency_fund + down_payment

rent_misc_total = sum(rent_misc)

for month in range(MONTHS):

    available = (
        monthly_income
        - monthly_rent
        - rent_misc_total
    )

    if available > 0:
        rent_total_savings += available

    rent_total_waste += monthly_rent
    
    if month == 12:
        rent_total_savings += selling_tn_land 
    
    if month == 24:
        rent_total_savings += chikfila_settlement 

    rent_waste.append(rent_total_waste)
    rent_savings.append(rent_total_savings)

# ============================================================
# Mortgage Simulation
# ============================================================

# Remaining balance on the mortgage loan
remaining_balance = loan

# Values to plot
mortgage_interest_paid = []
waste_to_mortgage = [] # amount of money 'wasted' to interest and taxes similar to how renting is 'waste'
mortgage_equity = []
mortgage_savings = []

# Running totals
total_interest_paid = mandatory_points
total_taxes_paid = 0
total_equity = down_payment      # Starts with the down payment
total_savings = emergency_fund   # Start with emergency fund.

monthly_expenses = sum(mortgage_misc) + monthly_house_taxes

for month in range(MONTHS):

    # redfin offers a 1% reduced interest for the first year.
    if redfin_benefit:
        if month <= 12:
            r = (annual_interest - 0.01) / 12 #redfin benefit.
            minimum_payment = calculate_mortgage_payment(loan, r, n)
        else:
            r = annual_interest / 12
            minimum_payment = calculate_mortgage_payment(loan, r, n)

    # ---------------------------------------------------------
    # Mortgage is already paid off
    # ---------------------------------------------------------
    if remaining_balance <= 0:

        monthly_savings = (
            monthly_income
            - monthly_expenses
        )

        total_savings += monthly_savings + renting_income

        mortgage_interest_paid.append(total_interest_paid)
        total_taxes_paid += monthly_house_taxes
        waste_to_mortgage.append(total_interest_paid + total_taxes_paid)
        mortgage_equity.append(total_equity)
        mortgage_savings.append(total_savings)

        continue

    # Calculate monthly_extra_principal based on savings:
    if total_savings > emergency_fund:
        potential_spending_money = total_savings - emergency_fund
        monthly_extra_principal = 0.8 * potential_spending_money
    else:
        potential_spending_money = 0

    # ---------------------------------------------------------
    # Interest charged this month
    # ---------------------------------------------------------
    monthly_interest = remaining_balance * r

    # Portion of the required payment that reduces the loan
    principal_payment = minimum_payment - monthly_interest     
   

    # Extra payment applied directly to the principal
    principal_payment += monthly_extra_principal

    # Don't pay more principal than remains on the loan
    principal_payment = min(principal_payment, remaining_balance)

    # Total amount paid to the bank this month
    monthly_mortgage_payment = monthly_interest + principal_payment

    # Update the remaining loan balance
    remaining_balance -= principal_payment

    # Update cumulative totals
    total_interest_paid += monthly_interest
    total_taxes_paid += monthly_house_taxes
    total_equity += principal_payment

    # Money left over after all expenses
    monthly_savings = (
        monthly_income
        - monthly_expenses
        - monthly_mortgage_payment
        + renting_income
    )
    
    if month == 12:
        total_savings += selling_tn_land 
    
    if month == 24:
        total_savings += chikfila_settlement 
    

    total_savings += monthly_savings

    # Store values for plotting
    mortgage_interest_paid.append(total_interest_paid)
    waste_to_mortgage.append(total_interest_paid + total_taxes_paid)
    mortgage_equity.append(total_equity)
    mortgage_savings.append(total_savings)
    
    if month % 12 == 0:
        print(
            month,
            monthly_income,
            monthly_expenses,
            monthly_mortgage_payment,
            monthly_savings,
            total_savings,
        )
        
    if month == 60:
        break

# ============================================================
# Plot
# ============================================================

years = [m / 12 for m in range(MONTHS)]

plt.figure(figsize=(12,7))

net_worth = [
    savings + equity
    for savings, equity in zip(mortgage_savings, mortgage_equity)
]

# ============================================================
# Summary
# ============================================================

print("======== Renting ========")
print(f"Total Rent Paid:      ${rent_total_waste:,.2f}")
print(f"Total Savings:        ${rent_total_savings:,.2f}")

print()

print("======== Mortgage ========")
print(f"Interest Paid:        ${total_interest_paid:,.2f}")
print(f"Total Waste:          ${total_interest_paid + total_taxes_paid:,.2f}")
print(f"Savings:              ${total_savings:,.2f}")

plt.plot(years, rent_waste, label="Rent Waste", linestyle="dotted")
plt.plot(years, rent_savings, label="Rent Savings", linestyle="--")
plt.plot(years, waste_to_mortgage, label="Mortgage (Waste)", linestyle="dotted")
plt.plot(years, mortgage_savings, label="Mortgage Savings", linestyle="--")
plt.plot(years, mortgage_equity, label="Home Equity")
plt.plot(years, net_worth, label="Net Worth")
plt.plot(years, mortgage_equity, label="Home Equity")

plt.xlabel("Years")
plt.ylabel("Dollars")
plt.title("Renting vs Mortgage")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


