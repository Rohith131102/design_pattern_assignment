from vehicle_details import vehicle

# Concrete Product (Car)
class Car(vehicle):
    def __init__(self, max_speed, seating_capacity):
        self.wheels = 4
        self.max_speed = max_speed
        self.seating_capacity = seating_capacity

    def get_details(self):
        return f"Car Details: Wheels={self.wheels}, Seating Capacity={self.seating_capacity}, Max Speed={self.max_speed}"
    
# Concrete Product (Motorcycle)
class Motorcycle(vehicle):
    def __init__(self, max_speed):
        self.wheels = 2
        self.max_speed = max_speed

    def get_details(self):
        return f"Motorcycle Details: Wheels={self.wheels}, Max Speed={self.max_speed}"

# Concrete Product (Truck)
class Truck(vehicle):
    def __init__(self, max_speed):
        self.wheels = 6
        self.max_speed = max_speed

    def get_details(self):
        return f"Truck Details: Wheels={self.wheels}, Max Speed={self.max_speed}"
    


    

