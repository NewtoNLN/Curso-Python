from decimal import Decimal, getcontext
getcontext().prec = 4
result = Decimal(1) / Decimal(7)

print(result)
