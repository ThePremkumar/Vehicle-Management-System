from src.admin import Admin;
from src.customer import CustomerPanel;

def main():
    try:
        print("--------------------------------------")
        print("Welcome to Prem Rentals")
        print("--------------------------------------")

        vehciles = {}
        customers = {}
        admin = Admin(vehciles)
        customer = CustomerPanel(customers, vehciles)



        while True:
            print("Select an Option: ")
            print("1. Admin Panel")
            print("2. Customer Panel")
            print("3. Exit")

            user_input = input("Enter your choice: ")

            if user_input == "3":
                print("Exiting the Main Panel")
                break
# Admin Panel
            elif user_input == "1":
                print("Entering Admin Panel")

                print("--------------------------------------")
                print("Welcome to Prem Rentals")
                print("--------------------------------------")

                while True:
                    print("Select an Option: ")
                    print("1. Add New Vehicles")
                    print("2. View the inventory")
                    print("3. Exit")

                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        vehicle_id = input("Enter the Vehicle ID: ") 
                        model = input("Enter the Model of the vehicle: ") 
                        type = input("Enter the type vehicle bike/car: ") 
                        rent = int(input("Enter the rent per day: ")) 

                        admin.add_new_vehicles(vehicle_id, model, type, rent)
                    elif admin_choice == "2":
                        admin.view_inventory()
                    elif admin_choice == "3":
                        print("Exiting the Admin Panel")
                        break
                    else:
                        print("Invalid Input, Use only 1,2,3")

# Customer Panle
            elif user_input == "2":
                print("Entering Customer Panle")

                print("--------------------------------------")
                print("Welcome to Prem Rentals")
                print("--------------------------------------")

                while True:
                    print("Select an Option: ")
                    print("1. Register the user")
                    print("2. Check available vehicles")
                    print("3. Rent vehicle")
                    print("4. Retrun vehicle")
                    print("5. Exit")

                    customer_choice = input("Enter your choice: ")

                    if customer_choice == "1":
                        customer_id = int(input("Enter your Id: "))
                        name = input("Enter your name: ")
                        age = int(input("Enter your age: "))

                        customer.register_customer(customer_id, name, age)
                    
                    elif customer_choice == "2":
                        customer.check_available_vehicles()
                    elif customer_choice == "3":
                        customer_id = int(input("Enter your Id: "))
                        vehicle_id = input("Enter the Vehicle ID: ")

                        customer.rent_vehicle(customer_id, vehicle_id)
                    elif customer_choice == "4":
                        customer_id = int(input("Enter your Id: "))
                        vehicle_id = input("Enter the Vehicle ID: ")

                        customer.return_vehicle(customer_id, vehicle_id)
                    elif customer_choice == "5":
                        print("Exiting the Admin Panel")
                        break
                    else:
                        print("Invalid Input, Use only 1,2,3")

            else:
                print("Invalid Input, Use only 1,2,3")
    except Exception as error:
            print(error)


if __name__ == "__main__":
    main()