#Check all vehicles
#add new vehicles


class Admin:

    def __init__(self, vehicles):
        self.vehicles = vehicles


    def add_new_vehicles(self, vehicle_id, model, type, rent):
        self.vehicles[vehicle_id] = {
            "id": vehicle_id,
            "model": model,
            "type": type,
            "rent": rent,
            "status": "available"
        }
        print(f"Added a Vehicle Successfully {vehicle_id}")



    def view_inventory(self):
        for value in self.vehicles.values():
            message = f"Id: {value["id"]} | rent: {value["rent"]} | model: {value["model"]}"
            print(value)


        #return self.vehicles


vehicles = {}