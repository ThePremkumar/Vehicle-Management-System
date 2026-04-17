class CustomerPanel:
    
    def __init__(self, customers, vehicles):
        self.customers = customers
        self.vehicles = vehicles



    def register_customer(self, customer_id, name, age):
        self.customers[customer_id] = {
            "id": customer_id,
            "name" : name,
            "age" : age,
            "rented_status" : False
        }

        print(f"Customer : {name} is register")


    def check_available_vehicles(self):
        for values in self.vehicles.values():
            if values["status"] == "available":
                message = f"\nId : {values["id"]} | rent : {values["rent"]} | model : {values["model"]}"
                print(message)


    def rent_vehicle(self, cid, vid):
        if cid not in self.customers.keys():
            print("Customer does not exist, Please register")
            return
        
        if vid not in self.vehicles.keys():
            print("Vehicle does not exist, Please choose an availabe vehicle")
            return

        if self.vehicles[vid]["status"] == "available":
            self.customers[cid]["rented_status"] = vid
            self.vehicles[vid]["status"] = "unavailable"
            print(f"Vehicle {vid} rented to Customer : {cid}")
        else:
            print("Vehicle is not available.")


    def return_vehicle(self, cid, vid):
        #vehicle is status is need to update 
        #print it
        if self.customers[cid]["rented_status"] != vid:
                print("This customer did not rent this vehicle.")
                return
        
        if self.vehicles[vid]["status"] == "unavailable":
            self.customers[cid]["rented_status"] = False
            self.vehicles[vid]["status"] = "available"
            print(f"Vehicle {vid} returned to garage for customer id {cid}")
        else:
            print("Vehicle is already available; cannot return.")



if __name__ == "__main__":
    customers = {}
    vehicles = {'V1001': 
                    {'id': 'V1001', 'model': 'Toyota', 'type': 'CorollaCar', 'rent': '₹1,500', 'status': 'available'}, 
               'V1002': 
                    {'id': 'V1002', 'model': 'Toyota Fortuner', 'type': 'Car', 'rent': '₹4,500', 'status': 'unavailable'}
                }
    customer = CustomerPanel(customers, vehicles)

    customer.register_customer(240, "Prem", 21)

    customer.check_available_vehicles()

    customer.rent_vehicle(240, "V1001")

    customer.return_vehicle(240, "V1002")