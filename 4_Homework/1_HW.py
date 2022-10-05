# Вычислить число c заданной точностью d

from decimal import ROUND_HALF_UP, Decimal

a = float(input("Enter a real number: "))
d = str(input("Enter the required accuracy '0.0001': "))

def giv_accuracy (a, d):
    num = Decimal(a)
    print(num.quantize(Decimal(d), ROUND_HALF_UP))
    return num

print(giv_accuracy(a, d))
