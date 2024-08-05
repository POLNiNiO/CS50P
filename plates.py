def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s.isalpha():
            return True
        elif s.isalnum() and s[0:2].isalpha():
            for character in s:
                if character.isdigit():
                    position = s.index(character)

                    if s[position:].isdigit() and int(character) != 0:
                        return True
                    else:
                        return False

main()
