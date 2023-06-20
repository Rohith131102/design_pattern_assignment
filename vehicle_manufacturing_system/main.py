
from vehicle_factories import CarFactory
from vehicle_factories import MotorcycleFactory
from vehicle_factories import TruckFactory


if __name__ == '__main__':

    # User input for the desired vehicle type
    vehicle_type = "car"
    # User input for the maximum speed
    max_speed = 100

    # Vehicle factory based on user input
    if vehicle_type == "car":
        factory = CarFactory()
    elif vehicle_type == "motorcycle":
        factory = MotorcycleFactory()
    elif vehicle_type == "truck":
        factory = TruckFactory()
    else:
        print("Invalid vehicle type.")
        exit()

    # Create the desired vehicle object using the factory
    vehicle = factory.create_vehicle(max_speed)

    # Display the vehicle details
    print(vehicle.get_details())
