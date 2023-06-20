import time


class weatherStation:
    def __init__(self):
        self.observers = []
        self.previous_weather_data = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, weather_data):
        for observer in self.observers:
            observer.update(weather_data)

    def get_weather_data(self):
        temperature = 34.5
        humidity = 79.0
        pressure = 1010.0
        return [temperature,humidity,pressure]

    def start_monitoring(self):
        while True:
            weather_data = self.get_weather_data()
            if weather_data != self.previous_weather_data:
                self.notify_observers(weather_data)
                self.previous_weather_data = weather_data

            time.sleep(5)
