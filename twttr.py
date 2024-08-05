txt = input("Input: ")

print("Output: ", end="")

for symbol in txt:
    if not symbol.lower() in ["a", "e", "i", "o", "u"]:
        print(symbol, end="")

print()
