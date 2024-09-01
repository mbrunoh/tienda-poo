from datetime import datetime
import pandas as pd
from time import sleep
from random import randint


class Producto:
    objetos = []
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__stock = stock
        self.__precio = precio
        Producto.objetos.append(self)
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def precio(self) -> float:
        return self.__precio

    @classmethod
    def consultar_objetos(cls):
        return cls.objetos
    
    def __str__(self):
        return f'{self.nombre} | Precio: $ {self.precio:.2f} | Stock: {self.stock}'

class VentaProducto():
    def __init__(self, producto, cantidad_venta):
        self.__cantidad_venta = cantidad_venta
        
        if self.__cantidad_venta > producto.stock:
            print(f'No hay productos disponible. Stock: {producto.stock}')
        else:
            producto.stock -= self.__cantidad_venta
            Histórico.registro(producto, 'Venta', cantidad_venta)

class CompraProducto:
    def __init__(self, producto, cantidad_compra):
        producto.stock += cantidad_compra
        Histórico.registro(producto, 'Compra', cantidad_compra)

class Histórico():
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

def BuscarProducto(prod):
    produtos = Producto.consultar_objetos()
    for producto in produtos:
        print(producto.nombre)
        if producto.nombre.lower() == prod.lower():
            return producto
    else:
        return False

def RegistrarProducto():
    global lista_productos
    print('Registrando nuevo producto')
    print()
    nombre = input('Nombre del producto: ')
    precio = float(input('Precio: $ '))
    stock = int(input('Stock: '))
    Producto(nombre, precio, stock)

def MostrarProductos():
    produtos = Producto.consultar_objetos()
    for producto in produtos:
        print(producto)

###  Mostrar listado de productos
# for producto in lista_productos:
#     print(producto)

### Generar DataFrame y guardar en excel
# datos = Histórico.consultar()
# df = pd.DataFrame(datos)
# print(df)
# df.to_excel('base.xlsx')