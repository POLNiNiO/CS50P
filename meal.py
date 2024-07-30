def main():
    question = input("What time is it?")
    time = convert(question)

    if 7 <= time <= 8:
        print("breakfast time")

    if 12 <= time <= 13:
        print("lunch time")

    if 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    changed_minutes = float(minutes) / 60
    return float(hours) + changed_minutes

if __name__ == "__main__":
    main()
