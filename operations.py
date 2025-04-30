class CarOperations:
    def __init__(self):
        self.cars = {}  
        
    def addCar(self, newCar):
        if newCar.id in self.cars:
            print(" Car ID already exists.")
        else:
            self.cars[newCar.id] = newCar
            print(" Car added successfully.")

    def updateCar(self, updatedCar):
        if updatedCar.id in self.cars:
            self.cars[updatedCar.id] = updatedCar
            print(" Car updated successfully.")
        else:
            print(" Car ID not found.")

    def deleteCar(self, carId):
        if carId in self.cars:
            self.cars.pop(carId)
            print(" Car deleted.")
        else:
            print(" Invalid Car ID.")

    def getCarById(self, carId):
        car = self.cars.get(carId)
        if car:
            print(car)
        else:
            print(" Car not found.")

    def getAllCars(self):
        if not self.cars:
            print(" No cars available.")
        else:
            for car in self.cars.values():
                print(car)