monthly_income = input("Enter your monthly income: ")

total_expenses = input("Enter your total monthly expenses: ")

monthly_savings = int(monthly_income) - int(total_expenses)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print ("Your monthly savings is:",  monthly_savings)
print ("projected savings after one year is:", projected_savings)