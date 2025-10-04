class car:
    def __init__(self, brand, year, clour, for_sale):
        self.brand = brand
        self.year = year
        self.clour = clour
        self.for_sale = for_sale

    def drive(self):
        print(f"Driving...{self.brand}")

    def stop(self):
        print(f"Stopping...{self.brand}")

    def describe(self):
        print(f"{self.brand} {self.year} {self.clour}")