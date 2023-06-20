from abc import ABC, abstractmethod

# Product (Vehicle)
class vehicle(ABC):
    @abstractmethod
    def get_details(self):
        pass
