#!/usr/bin/env python3

fixedInterestRate = 3.0
houseValue = 5 * 10**5
downPayment = 0.2
totalYears = 20

# Returns true if it can finish in `totalYears` with the underlying assumption
def finishesPayment(payPerMonth):
	remaining = houseValue * (1.0 - downPayment)
	for month in range(totalYears * 12):
		remaining = remaining * (1.0 + (fixedInterestRate / 100 / 12))
		remaining = remaining - payPerMonth
		if remaining < 0:
			break
	return remaining <= 0.0001

def findTargetPaymentPerMonth():
	start = 1
	end = 10000

	while (end - start > 1):
		mid = start + (end - start) / 2
		if not finishesPayment(mid):
			start = mid
		else:
			end = mid
	return start

def statsForPayment(payPerMonth):
	remaining = houseValue * (1.0 - downPayment)
	for month in range(totalYears * 12):
		if month % 12 == 0:
			print (f"After {month / 12} years, we have paid {(1.0 - (remaining / (houseValue * (1.0 - downPayment)))) * 100}%")
		remaining = remaining * (1.0 + (fixedInterestRate / 100 / 12))
		remaining = remaining - payPerMonth
	
requiredMonthlyPayment = findTargetPaymentPerMonth()
print (f"For a property of value {houseValue}, with a {downPayment * 100}% downpayment, with a {totalYears} term, it will cost {requiredMonthlyPayment} per month")
statsForPayment(requiredMonthlyPayment)
