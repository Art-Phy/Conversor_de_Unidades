### Conversor de Unidades ###

# creamos las funciones para las distintas posibles conversiones
def euros_a_dolares(euros):
    return euros * 1.11

def dolares_a_euros(dólares):
    return dólares * 0.90

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