camelCase = input("camelCase: ")

print("snake_case: ", end="")

for symbol in camelCase:
    if symbol.isupper():
        print("_" + symbol.lower(), end="")

    else:
        print(symbol, end="")

print()
