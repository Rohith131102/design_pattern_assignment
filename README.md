# Question

<img width="544" alt="Screenshot 2023-06-20 at 7 21 57 PM" src="https://github.com/Rohith131102/design_pattern_assignment/assets/123619674/fd0d832c-935a-420d-a8a4-ac65db5c1597">

<img width="570" alt="Screenshot 2023-06-20 at 7 23 54 PM" src="https://github.com/Rohith131102/design_pattern_assignment/assets/123619674/6d51c162-6f6a-4955-8773-69c597f8ac6e">

# Weather Monitoring System Explanation

This code demonstrates the implementation of a weather monitoring system in Python. The system consists of a weather station (subject) and multiple display devices (observers) that subscribe to the weather station for real-time updates.

## WeatherStation Class

The `WeatherStation` class represents the weather station. It has the following methods:

- `__init__()`: Initializes the weather station with an empty list of observers.
- `register_observer(observer)`: Adds an observer to the list of registered observers.
- `unregister_observer(observer)`: Removes an observer from the list of registered observers.
- `notify_observers(weather_data)`: Notifies all registered observers by calling their `update()` method with the weather data.
- `get_weather_data()`: Simulated method to fetch the current weather data.
- `start_monitoring()`: Starts monitoring the weather data by repeatedly fetching the data and notifying the observers when the data changes.

## Observer Class

The `Observer` class is an abstract base class that represents the observers. It has a single abstract method `update(weather_data)` that needs to be implemented by its subclasses.

## DisplayDevice Subclasses

The code includes three subclasses of the `DisplayDevice` class representing different display devices:

- `MobileAppDisplay`: This subclass displays the weather data on a mobile app.
- `WebInterfaceDisplay`: This subclass displays the weather data on a web interface.
- `DesktopApplicationDisplay`: This subclass displays the weather data on a desktop application.

Each subclass implements the `update(weather_data)` method to update its user interface and display the received weather data.

## Usage

In the `main.py` file, an instance of the `WeatherStation` class is created. Then, instances of the display device subclasses (`MobileAppDisplay`, `WebInterfaceDisplay`, and `DesktopApplicationDisplay`) are created. The display devices are registered as observers of the weather station using the `register_observer()` method. Finally, the weather station's `start_monitoring()` method is called to start monitoring the weather data.

When the weather data changes, the weather station notifies all registered observers, and each observer updates its user interface and displays the received weather data.

This code demonstrates the Observer design pattern, allowing for a one-to-many relationship between the weather station and the display devices. It enables real-time updates and flexibility in adding new display devices without modifying the existing code of the weather station or other display devices.

## output:
<img width="166" alt="Screenshot 2023-06-20 at 7 27 08 PM" src="https://github.com/Rohith131102/design_pattern_assignment/assets/123619674/73c85d9f-b6d2-4319-8a01-76a6c8d47b85">


# Vehicle manufactoring system

This code demonstrates the implementation of a simple vehicle factory using the **Factory Method** design pattern. The code consists of several classes representing vehicles and their corresponding factories.

## Vehicle Classes

### Car

The `Car` class represents a car and inherits from the abstract `Vehicle` class. It has attributes for the number of wheels, maximum speed, and seating capacity. The `get_details()` method returns a string representation of the car's details.

### Motorcycle

The `Motorcycle` class represents a motorcycle and also inherits from the `Vehicle` class. It has attributes for the number of wheels and maximum speed. The `get_details()` method returns a string representation of the motorcycle's details.

### Truck

The `Truck` class represents a truck and also inherits from the `Vehicle` class. It has attributes for the number of wheels and maximum speed. The `get_details()` method returns a string representation of the truck's details.

## Vehicle Factory Classes

### VehicleFactory

The `VehicleFactory` class is the abstract base class for all vehicle factories. It defines an abstract method `create_vehicle()` that needs to be implemented by its concrete subclasses.

### CarFactory

The `CarFactory` class is a concrete subclass of `VehicleFactory`. It implements the `create_vehicle()` method to create a `Car` object. It also includes a helper method `get_seating_capacity()` to get the seating capacity of the car from user input.

### MotorcycleFactory

The `MotorcycleFactory` class is another concrete subclass of `VehicleFactory`. It implements the `create_vehicle()` method to create a `Motorcycle` object.

### TruckFactory

The `TruckFactory` class is the third concrete subclass of `VehicleFactory`. It implements the `create_vehicle()` method to create a `Truck` object.

## Usage

In the `main.py` file, the user is prompted to enter the desired vehicle type (car/motorcycle/truck) and the maximum speed. Based on the user's input, the corresponding factory is selected, and the `create_vehicle()` method is called to create the desired vehicle object. Finally, the details of the vehicle are displayed using the `get_details()` method.

This code demonstrates the Factory Method design pattern, allowing for the creation of different types of vehicles using a common interface and separate factories. It promotes loose coupling and extensibility, allowing new vehicle types and factories to be added without modifying existing code.

## output
<img width="406" alt="Screenshot 2023-06-20 at 7 28 11 PM" src="https://github.com/Rohith131102/design_pattern_assignment/assets/123619674/0f14b24f-d384-48fb-83f9-8e056feaa93e">
