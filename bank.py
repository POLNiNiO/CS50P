greeting = input("Greeting:")

capital_greeting = greeting.lower().strip()

if "hello" in capital_greeting:
    print("$0")

elif "h" == capital_greeting[0]:
    print ("$20")

else:
    print("$100")

