### Conversor de Unidades ###

# Importamos la librería locale para que los números se muestren en el formato regional del usuario (dependiendo de su configuración local)
import locale
locale.setlocale(locale.LC_ALL, '')

# Función para formatear números según la config local + dos decimales
def formatear(valor):
    return locale.format_string('%.2f', valor, grouping=True)

# Tipos de conversiones
def euros_a_usdolares(euros):
    return euros * 1.11

def usdolares_a_euros(usdólares):
    return usdólares * 0.90

def celsius_a_farenheit(celsius):
    return (celsius * 9/5) + 32

def farenheit_a_celsius(farenheit):
    return (farenheit - 32) * 5/9

def km_a_millas(km):
    return km / 1.609

def millas_a_km(millas):
    return millas * 1.609

def cm_a_pulgadas(cm):
    return cm / 2.54

def pulgadas_a_cm(pulgadas):
    return pulgadas * 2.54

# Menú de opciones en terminal
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

# Función principal 
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


        # Manejo de las opciones
        if opcion == 1:
            print(f"{formatear(cantidad)} € son {formatear(euros_a_usdolares(cantidad))} $.")
        elif opcion == 2:
            print(f"{formatear(cantidad)} $ son {formatear(usdolares_a_euros(cantidad))} €.")
        elif opcion == 3:
            print(f"{formatear(cantidad)} °C son {formatear(celsius_a_farenheit(cantidad))} °F.")
        elif opcion == 4:
            farenheit =float(input("Introduce la temperatura en grados Farenheit: "))
            print(f"{farenheit} grados Farenheit son {farenheit_a_celsius(farenheit)} grados Celsius.")

        elif opcion == 5:
            print(f"{formatear(cantidad)} km son {formatear(km_a_millas(cantidad))} millas.")
        elif opcion == 6:
            print(f"{formatear(cantidad)} millas son {formatear(millas_a_km(cantidad))} km.")
        elif opcion == 7:
            print(f"{formatear(cantidad)} cm son {formatear(cm_a_pulgadas(cantidad))} pulgadas.")
        elif opcion == 8:
            print(f"{formatear(cantidad)} pulgadas son {formatear(pulgadas_a_cm(cantidad))} cm.")
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