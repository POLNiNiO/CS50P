amount_due = 50

while amount_due > 0:
    print("Amount Due:",amount_due)

    insert = int(input("Insert Coin: "))

    if insert in [25, 10, 5]:
        amount_due -= insert

change = abs(amount_due)

print("Change Owed:",change)
