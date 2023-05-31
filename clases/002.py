class Animal:
    def __init__(self, nombre, edad, especie) -> None:
        self.nombre=nombre
        self.edad = edad
        self.especie = especie
    
animal  = Animal("John", 10, "Perro")

print(f"Hola, mi nombre es {animal.nombre} y tengo {animal.edad} y soy un {animal.especie} ", animal)