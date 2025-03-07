class prenda:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.disponible = True

    def mostrar(self):
        estado = "Disponible" if self.disponible else "Vendida"
        return f"{self.nombre} - ${self.precio} - {estado}"

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"Vendido: {self.nombre}")
        else:
            print(f"{self.nombre} ya fue vendida")

class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar(self, prenda):
        self.prendas.append(prenda)
        print(f"Agregado: {prenda.nombre}")

    def lista(self):
        print("INVENTARIO")
        if not self.prendas:
            print("No hay inventario")
            return

        for i, prenda in enumerate(self.prendas, 1):
            print(f"{i}. {prenda.mostrar()}")

inventario = Inventario()
camisa = prenda("Camisa", 20)
pantalon = prenda("Pantalón", 30)
inventario.agregar(camisa)
inventario.agregar(pantalon)
inventario.lista()
camisa.vender()
inventario.lista()
camisa.vender()