class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def getFare(self):
        return self.capacity * 100


class Bus(Vehicle): 
    def __init__(self, capacity):
        super().__init__(capacity)

    def getFare(self):
        vehicleFare = super().getFare()
        maintenanceFare = 0.1 * vehicleFare
        totalFare = maintenanceFare + vehicleFare
        return totalFare


vehicle1 = Vehicle(50)
print("Vehicle fare: ", vehicle1.getFare())

bus1 = Bus(50)
print("Bus fare: ", bus1.getFare())
