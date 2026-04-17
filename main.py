def main():
    try:
        print("--------------------------------------")
        print("Welcome to Prem Rentals")
        print("--------------------------------------")

        while True:
            print("Select an Option: ")
            print("1. Admin Panel")
            print("2. Customer Panel")
            print("3. Exit")

            user_input = input("Enter your choice: ")

            if user_input == "3":
                print("Exiting the Main Panel")
                break
            elif user_input == "1":
                print("Entering Admin Panle")
            elif user_input == "2":
                print("Entering Customer Panle")
            else:
                print("Invalid Input, Use only 1,2,3")
    except Exception as error:
            print(error)


if __name__ == "__main__":
    main()