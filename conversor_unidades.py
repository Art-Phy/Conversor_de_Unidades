### Conversor de Unidades ###

# Importamos la librería locale para que los números se muestren en el formato regional del usuario (dependiendo de su configuración local)
import locale
locale.setlocale(locale.LC_ALL, '')



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
    while True: # añadimos un bucle para preguntar al final al usuario qué quiere hacer

        print("Elige qué tipo de conversión quieres hacer")
        print(" 1. Euros a US Dólares")
        print(" 2. US Dólares a Euros")
        print(" 3. Grados Celsius a Grados Farenheit")
        print(" 4. Grados Farenheit a Grados Celsius")
        print(" 5. Kilómetros a Millas")
        print(" 6. Millas a Kilómetros")
        print(" 7. Centímetros a Pulgadas")
        print(" 8. Pulgadas a Centímentros")
        print(" 9. Salir")

        # le decimos al usuario que ingrese el número a convertir y añadimos las funciones de la librería  locale.
        try:    
            opcion = int(input("Introduce el número de la conversión deseada: "))
        except ValueError:
            print("X Entrada no válida. Por favor introduce un número del 1 al 9.")
            
        if opcion == 1:
            euros =float(input("Introduce la cantidad en Euros: "))
            print(f"{euros} € son {euros_a_usdolares(euros)} $.")

        elif opcion == 2:
            usdólares =float(input("Introduce la cantidad en US Dólares: "))
            print(f"{usdólares} $ son {usdolares_a_euros(usdólares)} €.")

        elif opcion == 3:
            celsius =float(input("Introduce la temperatura en grados Celsius: "))
            print(f"{celsius} grados Celsius son {celsius_a_farenheit(celsius)} grados Farenheit.")

        elif opcion == 4:
            farenheit =float(input("Introduce la temperatura en grados Farenheit: "))
            print(f"{farenheit} grados Farenheit son {farenheit_a_celsius(farenheit)} grados Celsius.")

        elif opcion == 5:
            km =float(input("Introduce la distancia en Kilómetros: "))
            print(f"{km} km son {km_a_millas(km)} millas.")

        elif opcion == 6:
            millas =float(input("Introduce la distancia en millas: "))
            print(f"{millas} millas son {millas_a_km(millas)} km.")

        elif opcion == 7:
            cm =float(input("Introduce la longitud en Centímetros: "))
            print(f"{cm} cm son {cm_a_pulgadas(cm)} pulgadas.")

        elif opcion == 8:
            pulgadas =float(input("introduce la longitud en Pulgadas: "))
            print(f"{pulgadas} pulgadas son {pulgadas_a_cm(pulgadas)} cm.")

        else:
            print("Opción no válida")

        # preguntamos qué quiere hacer el usuario a continuación
        continuar = input("\n¿Quieres hacer otra conversión? (s/n): ").strip().lower()
        if continuar != 's':
            print("Gracias por usar el conversor. ¡Hasta otra!")
            break

# ejecutar programa
conversor()
