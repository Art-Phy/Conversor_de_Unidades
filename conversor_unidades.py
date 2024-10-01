### Conversor de Unidades ###

# creamos las funciones para las distintas posibles conversiones
def euros_a_usdolares(euros):
    return euros * 1.11

def usdolares_a_euros(usdólares):
    return usdólares * 0.90

def celsius_a_farenheit(celsius):
    return (celsius * 9/5) + 32

def farenheit_a_celsius(farenheit):
    return (farenheit - 32) * 5/9

def km_a_millas(km):
    return km / 0.621371

def millas_a_km(millas):
    return millas * 1.609

def cm_a_pulgadas(cm):
    return cm / 2.54

def pulgadas_a_cm(pulgadas):
    return pulgadas * 2.54

# hacemos una función para que muestre un menú de opciones para el usuario
def conversor():
    print("Indica qué tipo de conversión quieres hacer")
    print(" 1. Euros a US Dólares")
    print(" 2. US Dólares a Euros")
    print(" 3. Grados Celsius a Grados Farenheit")
    print(" 4. Grados Farenheit a Grados Celsius")
    print(" 5. Kilómetros a Millas")
    print(" 6. Millas a Kilómetros")
    print(" 7. Centímetros a Pulgadas")
    print(" 8. Pulgadas a Centímentros")

    # le decimos al usuario que ingrese el número a convertir
    opcion = int(input("Introduce la cantidad a convertir: "))

    if opcion == 1:
        euros =float(input("Introduce la cantidad en Euros: "))
        print(f"{euros} € son {euros_a_usdolares} $.")

    elif opcion == 2:
        usdólares =float(input("Introduce la cantidad en US Dólares: "))
        print(f"{usdólares} $ son {usdolares_a_euros} €.")

    elif opcion == 3:
        celsius =float(input("Introduce la temperatura en grados Celsius: "))
        print(f"{celsius} grados Celsius son {celsius_a_farenheit} grados Farenheit.")

    elif opcion == 4:
        farenheit =float(input("Introduce la temperatura en grados Farenheit: "))
        print(f"{farenheit} grados Farenheit son {farenheit_a_celsius} grados Celsius.")

    elif opcion == 5:
        km =float(input("Introduce la distancia en Kilómetros: "))
        print(f"{km} km son {km_a_millas} millas.")

    elif opcion == 6:
        millas =float(input("Introduce la distancia en millas: "))
        print(f"{millas} millas son {millas_a_km} km.")

    elif opcion == 7:
        cm =float(input("Introduce la longitud en Centímetros: "))
        print(f"{cm} cm son {cm_a_pulgadas} pulgadas.")

    elif opcion == 8:
        pulgadas =float(input("introduce la longitud en Pulgadas: "))
        print(f"{pulgadas} pulgadas son {pulgadas_a_cm} cm.")


