#!/usr/bin/python
# -*- coding: utf-8 -*-
from decimal import Decimal
from copy import deepcopy
from typing import Dict

class Product:
    def __init__(self, id_: str, name: str, price: float) -> None:
        self.id = id_
        self.name = name
        self.price = price
    def __str__(self) -> str:
        return f"{self.name} [{self.id}] : ${self.price:.2f}"
    def __eq__(self, other) -> bool:
        if self.id == other.id and self.name == other.name and self.price == other.price:
            return True
        else:
            return False


class Catalogue:
    def Inventory(Dict[product.id, product])
        
    def __init__(self, inventory=None) -> None:
        self.inventory = deepcopy(inventory)
    def add_product(self, product: Product) -> None:
        pass
    def __contains__(self, id: str) -> bool:
        pass


produkt = Product("A1", "Karta", 5.6767)
print(produkt.__str__())
produkt2 = Product("A1", "Karta", 5.6767)
produkt3 = Product("B1", "Karta", 5.6767)
print(produkt.__eq__(produkt2))
print(produkt.__eq__(produkt3))