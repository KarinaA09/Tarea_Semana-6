# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  # atributo público
        self.modelo = modelo  # atributo público
        self._kilometraje = 0  # atributo protegido

    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando.")

    def _actualizar_kilometraje(self, km):
        self._kilometraje += km

    def obtener_kilometraje(self):
        return self._kilometraje


# Definición de la clase derivada Automovil que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color  # atributo público

    def acelerar(self):  # sobrescritura del método acelerar
        print(f"{self.marca} {self.modelo} ({self.color}) acelerando.")


# Crear instancias de las clases
vehiculo_generico = Vehiculo("MarcaX", "ModeloY")
auto = Automovil("Ford", "Fiesta", "Rojo")

# Ejemplo de uso de métodos y atributos
print("Vehículo:", vehiculo_generico.marca, vehiculo_generico.modelo)
vehiculo_generico.acelerar()

print("\nAutomóvil:", auto.marca, auto.modelo, auto.color)
auto.acelerar()
