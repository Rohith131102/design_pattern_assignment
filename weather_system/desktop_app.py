from latest_data import updateData

class desktopAppUpdate(updateData):
    def update(self, weather_data):
        print("Desktop App Display:")
        print(f"Temperature: {weather_data[0]}")
        print(f"Humidity: {weather_data[1]}")
        print(f"Pressure: {weather_data[2]}")
        print()
ˀ.¸