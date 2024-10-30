import logging
from abc import abstractmethod, ABC


logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car():
        pass

    @abstractmethod
    def create_motorcycle():
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (EU Spec)")


if __name__ == "__main__":
    # vehicle1 = Car("Toyota", "Corolla")
    # vehicle1.start_engine()

    # vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
    # vehicle2.start_engine()

    us_vehicle_factory = USVehicleFactory()
    eu_vehicle_factory = EUVehicleFactory()

    vehicle1 = us_vehicle_factory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = eu_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    vehicle3 = us_vehicle_factory.create_car("Ford", "Mustang")
    vehicle3.start_engine()
