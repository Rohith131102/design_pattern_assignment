# Creator (Vehicle Factory)
from abc import ABC, abstractmethod

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, max_speed):
        pass
