class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def __str__(self): #metodo que define como su muestra el objeto al usar print()
        return f"Nombre: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años"

nombre = input("Ingrese el nombre del animal: ") #permite pedir datos al usuario
especie = input("Ingrese la especie: ") #input () devuelve string
edad = int(input("Ingrese la edad: ")) #int (input()) se convierte a entero

a = Animal (nombre, especie, edad) #creamos objeto con los datos ingresados por usuario
print(a) #cuando imprime objeto se ejecuta el metodo __str__() automaticamente
