def main():
    say = input("What do you want to say? ")
    txt = convert(say)
    print(txt)

def convert(say):
    say1 = say.replace(":)","🙂")
    say2 = say1.replace(":(","🙁")
    return say2

main()
