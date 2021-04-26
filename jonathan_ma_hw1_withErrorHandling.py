def main():
    isLeapMsg = "is a leap year."
    notLeapMsg = "is not a leap year."

    while True:

        try:
            userInput = input("Enter a year: ")
            userInt = int(userInput)
            if userInt % 4 == 0:
                if userInt % 400 == 0:
                    print(userInt, isLeapMsg)
                else:
                    if userInt % 100 == 0:
                        print(userInt, notLeapMsg)
                    else:
                        print(userInt, isLeapMsg)

            else:
                print(userInt, notLeapMsg)

        except ValueError:
            print("Input is not a number. Please try again.")



if __name__ == "__main__":
    main()
