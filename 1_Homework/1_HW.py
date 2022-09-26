a = int(input("ВВедите число, соответствующее дню недели: "))
if a <= 5:
    print("Workday")
elif a == 6 or a == 7:
    print("Weekend")
elif a > 7:
    print("It's not a day of the week!")