from operations import CarOperations
from models import Car
import sys

opr = CarOperations()

choice = 0
while choice != 6:
    print('''
        1. Add Car
        2. Update Car
        3. Delete Car
        4. Get Car by ID
        5. Show All Cars
        6. Exit
    ''')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        i = int(input("Enter Car ID: "))
        b = input("Enter Brand: ")
        m = input("Enter Model: ")
        y = int(input("Enter Year: "))
        p = float(input("Enter Price: "))
        car = Car(i, b, m, y, p)
        opr.addCar(car)

    elif choice == 2:
        i = int(input("Enter ID to update: "))
        b = input("Enter New Brand: ")
        m = input("Enter New Model: ")
        y = int(input("Enter New Year: "))
        p = float(input("Enter New Price: "))
        car = Car(i, b, m, y, p)
        opr.updateCar(car)

    elif choice == 3:
        i = int(input("Enter Car ID to delete: "))
        opr.deleteCar(i)

    elif choice == 4:
        i = int(input("Enter Car ID: "))
        opr.getCarById(i)

    elif choice == 5:
        opr.getAllCars()

    elif choice == 6:
        print(" Exiting the application.")
        sys.exit()

    else:
        print(" Invalid choice.")