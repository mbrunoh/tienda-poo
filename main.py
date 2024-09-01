from datetime import datetime
import pandas as pd
from time import sleep
from random import randint


class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__stock = stock
        self.__precio = precio
        
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def stock(self) -> int:
        return self.__stock
    @stock.setter
    def stock(self, stock):
        self.__stock = stock

    @property
    def precio(self) -> float:
        return self.__precio
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
    def __str__(self):
        return f'{self.nombre} | Precio: $ {self.precio:.2f} | Stock: {self.stock}'

class VentaProducto:
    def __init__(self, producto, cantidad_venta):
        self.__cantidad_venta = cantidad_venta
        
        if self.__cantidad_venta > producto.stock:
            print(f'No hay productos disponible. Stock: {producto.stock}')
        else:
            producto.stock -= self.__cantidad_venta
            Inventário.registro(producto, 'Venta', cantidad_venta)

class CompraProducto:
    def __init__(self, producto, cantidad_compra):
        producto.stock += cantidad_compra
        Inventário.registro(producto, 'Compra', cantidad_compra)

class Inventário():
    __histórico = dict()
    __id = 0
    
    @classmethod
    def registro(cls, producto, operación, cantidad):
        instancia = {
            'producto': producto.nombre,
            'operación': operación,
            'cantidad': cantidad,
            'total': f'$ {cantidad*producto.precio:.2f}',
            'fecha': datetime.now().date()
        }
        cls.__histórico[cls.__id] = instancia
        cls.__id += 1
    
    @classmethod
    def consultar(self) -> dict:
        registros = []
        for k, registro in self.__histórico.items():
            registros.append(registro)
        return registros

banana = Producto('Banana', 300, 100)
maca = Producto('Maça', 600, 10)
uva = Producto('Uva', 1300, 5)
huevo = Producto('Huevo', 4400, 10)

VentaProducto(banana, 80)
VentaProducto(huevo, 2)
VentaProducto(maca, 4)
CompraProducto(maca, 3)
CompraProducto(huevo, 15)
VentaProducto(banana, 13)

a = Inventário.consultar()

df = pd.DataFrame(a)
# df.to_excel('base.xlsx')
print(df.loc[:,'total'].to_string())