from vehicle_factory_details import VehicleFactory
from vehicles import Car
from vehicles import Motorcycle
from vehicles import Truck
# Concrete Creator (Car Factory)
class CarFactory(VehicleFactory):
    def create_vehicle(self, max_speed):
        seating_capacity = self.get_seating_capacity()
        return Car(max_speed, seating_capacity)

    def get_seating_capacity(self):
        return 5
    

# Concrete Creator (Motorcycle Factory)
class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self, max_speed):
        return Motorcycle(max_speed)
    

# Concrete Creator (Truck Factory)
class TruckFactory(VehicleFactory):
    def create_vehicle(self, max_speed):
        return Truck(max_speed)