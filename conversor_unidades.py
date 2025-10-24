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

def mostrar_menu():

        print("\n=== CONVERSOR DE UNIDADES ===")
        print(" 1. Euros a US Dólares")
        print(" 2. US Dólares a Euros")
        print(" 3. Grados Celsius a Grados Farenheit")
        print(" 4. Grados Farenheit a Grados Celsius")
        print(" 5. Kilómetros a Millas")
        print(" 6. Millas a Kilómetros")
        print(" 7. Centímetros a Pulgadas")
        print(" 8. Pulgadas a Centímentros")
        print(" 9. Salir")

# hacemos una función para que muestre un menú de opciones para el usuario
def conversor():
    while True:
        mostrar_menu() # añadimos un bucle para preguntar al final al usuario qué quiere hacer

        try:
            opcion = int(input("Introduce el número de la conversión deseada: "))
        except ValueError:
            print("X Opción no válida. Por favor introduce un número del 1 al 9.")
            continue

        if opcion == 9:
            print("Gracias por usar el conversor. ¡Nos vemos!")
            break
        
        try:
            cantidad = float(input("Introduce el valor a convertir: "))
        except ValueError:
            print("X Entrada no válida. Debes introducir un número.")
            continue


# Comienzamos a manejar las distintas opciones
        if opcion == 1:
            print(f"{cantidad} € son {euros_a_usdolares(cantidad):.2f} $.")
        elif opcion == 2:
            print(f"{cantidad} $ son {usdolares_a_euros(cantidad):.2f} €.")
        elif opcion == 3:
            print(f"{cantidad} °C son {celsius_a_farenheit(cantidad):.2f} °F.")
        elif opcion == 4:
            print(f"{cantidad} °F son {farenheit_a_celsius(cantidad):.2f} °C.")
        elif opcion == 5:
            print(f"{cantidad} km son {km_a_millas(cantidad):.2f} millas.")
        elif opcion == 6:
            print(f"{cantidad} millas son {millas_a_km(cantidad):.2f} km.")
        elif opcion == 7:
            print(f"{cantidad} cm son {cm_a_pulgadas(cantidad):.2f} pulgadas.")
        elif opcion == 8:
            print(f"{cantidad} pulgadas son {pulgadas_a_cm(cantidad):.2f} cm.")
        else:
            print(" X Opción no válida. Intenta de nuevo.")


        # preguntamos qué quiere hacer el usuario a continuación
        continuar = input("\n¿Quieres hacer otra conversión? (s/n): ").strip().lower()
        if continuar != 's':
            print("Gracias por usar el conversor. ¡Hasta otra!")
            break

# ejecutar programa
if __name__ == "__main__":
    conversor()
