print("Hola Mundo!! soy Melvin")
print("Hello World!!")
print(".__.")

# este es un comentario

"""
Texto de prueba
Texto de prueba
Texto de prueba
"""

# Variables
texto = "Variables basicas"
nombre = "Melvin Pineda"
edad = "27 años"
year = 2022

print(f"{texto} - {nombre} -{edad} - {str(year)}")

# Entrada de datos
digimon = input("¿Cual es tu digimon favorito?: ")
print("Tu digimon favorito es: " + digimon)

"""
# Condiciones
altura= int(input("¿Cual es tu altura?: "))

if altura >= 180:
    print("Estas altisimo")
else:
    print("Estas chaparro")    
"""

# Funciones
altura= int(input("¿Cual es tu altura?: "))

def Mostraraltura(altura):
    resultado = ""
    if altura >= 180:
        resultado = "Estas altisimo"
    else:
        resultado = "Estas chaparro"
    return resultado

print(Mostraraltura(altura))    

# Listas
pokemones = ["Starmie", "Staryu", "Psyduck", "Dragonair"]

# print(pokemones[3]) listas cuentan desde el 0
for pokemon in pokemones:
    print("-" + pokemon)

#Dictionaries almacena objetos en una lista de keys(llaves) y values valores
dictevo = {
    "Bebe": "Nyaromon",
    "Niño": "Salamon",
    "Adulto": "Gatomon",
    "Perfeccionado": "Angewomon",
    "Mega": "Magnadramon",
}

print(dictevo)

#Se pueden tener varios diccionarios en uno