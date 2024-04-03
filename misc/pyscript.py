while True:
    try:
        age = int(input("How old are you?"))
        for x in range(age):
            print("Happy Birthday!")
    except ValueError:
        print("please list your age as an integer number")
