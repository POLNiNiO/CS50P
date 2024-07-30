expression = input("Expression:")

x, y, z = expression.split(" ")

new_x = float(x)
new_z = float(z)

if y == "+":
    final = new_x + new_z

if y == "-":
    final = new_x - new_z

if y == "*":
    final = new_x * new_z

if y == "/":
    final = new_x / new_z

print(final)
