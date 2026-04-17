#Check all vehicles
#add new vehicles


class Admin:

    def __init__(self, vehicles):
        self.vehicles = vehicles


    def add_new_vehicles(self, vehicle_id, model, type, rent):
        try:
            self.vehicles[vehicle_id] = {
                "id": vehicle_id,
                "model": model,
                "type": type,
                "rent": rent,
                "status": "available"
            }
            print(f"Added a Vehicle Successfully {vehicle_id}")
        except Exception as error:
            print(error)


    def view_inventory(self):
        try:
            for value in self.vehicles.values():
                message = f"Id: {value["id"]} | rent: {value["rent"]} | model: {value["model"]}"
                print(message)
        except Exception as error:
            print(error)

        #return self.vehicles

if __name__ == '__main__':
    vehicles = {}

    prem_admin = Admin(vehicles)
    prem_admin.add_new_vehicles("V-101", "Toyota", "Corolla" "Car", "₹1,500")
    prem_admin.add_new_vehicles("V1002", "Toyota Fortuner", "Car", "₹4,500")

    print(vehicles)
    prem_admin.view_inventory()