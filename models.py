class Car:
    def __init__(self, id, brand, model, year, price):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return (f'Car Details -> ID: {self.id} | Brand: {self.brand} | Model: {self.model} | '
                f'Year: {self.year} | Price: ${self.price}')