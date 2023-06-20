from observer import updateData

class mobileAppUpdate(updateData):
    def update(self, weather_data):
        print("Mobile App Display:")
        print(f"Temperature: {weather_data[0]}")
        print(f"Humidity: {weather_data[1]}")
        print(f"Pressure: {weather_data[2]}")
        print()

