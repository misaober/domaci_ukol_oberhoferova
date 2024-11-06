import math
from abc import ABC, abstractmethod

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property(ABC):
    def __init__(self, locality):
        self.locality = locality
    @abstractmethod
    def __str__():
        pass
    @abstractmethod
    def calculate_tax():
        pass

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    def __str__(self): 
        if self.estate_type == "land":
            estate_type_cz = "Zemědělský pozemek"
        elif self.estate_type == "building_site":
            estate_type_cz = "Stavební pozemek"
        elif self.estate_type == "forrest":
            estate_type_cz = "Les"
        elif self.estate_type == "garden":
            estate_type_cz = "Zahrada"
        return f" {estate_type_cz}, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
    def calculate_tax(self):
        if self.estate_type == "land":
            estate_coefficient = 0.85
        elif self.estate_type == "building_site":
            estate_coefficient = 0.9
        elif self.estate_type == "forrest":
            estate_coefficient = 0.35
        elif self.estate_type == "garden":
            estate_coefficient = 2
        tax = math.ceil(self.area * estate_coefficient * self.locality.locality_coefficient)
        return tax
    
class Rezidence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        if self.commercial == True:
            commercial_coefficient = 2
        else:
            commercial_coefficient = 1
        tax = math.ceil(self.area * self.locality.locality_coefficient * 15 * commercial_coefficient)
        return tax
    def __str__(self): 
        if self.commercial == True:
            estate_type_cz = "Komerční"
        else:
            estate_type_cz = "Rezidenční"
        return f" {estate_type_cz} prostor, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."

# class TaxReport:
#     def __init__(self, name):
#         self.name = name
#         self.property_list = []
#     def add_property(self, property):
#         self.property_list.append(property)




manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)
pozemek_1 = Estate(manetin, "land", 900)
dum_1 = Rezidence(manetin, 120, False)
komerce_1 = Rezidence(brno, 90, True)
print(pozemek_1.calculate_tax())
print(dum_1.calculate_tax())
print(pozemek_1.locality.locality_coefficient)
print(pozemek_1)
print(dum_1)
print(komerce_1)
print(dum_1)

