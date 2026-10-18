# Estas funciones leen datos del teclado y evitan repetir las mismas validaciones en main.py.

from math import isfinite  # Usa una función de Python estándar; no requiere instalar paquetes.

def leer_texto(mensaje):  # Solicita un texto que no puede quedar vacío.
    while True:  # Repite la solicitud hasta recibir un texto válido.
        texto = input(mensaje + ": ").strip()  # Lee el texto y elimina espacios al principio y al final.
        if texto != "":  # Comprueba que exista contenido después de quitar los espacios.
            return texto  # Devuelve el texto válido y termina esta función.
        print("Este dato no puede quedar vacío.")  # Informa por qué se volverá a solicitar el dato.

def leer_entero(mensaje):  # Solicita un entero; permite cero y negativos para probar los métodos de modificación.
    while True:  # Repite la lectura cuando el usuario escribe algo que no es un entero.
        try:  # Intenta realizar una conversión que podría fallar.
            numero = int(input(mensaje + ": "))  # Convierte el texto ingresado en un número entero.
            return numero  # Devuelve el entero cuando la conversión resulta correcta.
        except ValueError:  # Captura el error producido por entradas como letras o decimales.
            print("Ingresa un número entero, por ejemplo 3.")  # Explica el formato esperado.

def leer_entero_positivo(mensaje):  # Solicita un entero mayor que cero para los nuevos registros.
    while True:  # Repite la solicitud hasta recibir un entero positivo.
        numero = leer_entero(mensaje)  # Reutiliza la función que comprueba el formato del entero.
        if numero > 0:  # Comprueba que el número sea positivo.
            return numero  # Devuelve el valor aceptado.
        print("El número debe ser mayor que cero.")  # Informa que cero y negativos no son válidos.

def leer_promedio(mensaje):  # Solicita un promedio sin imponer una escala máxima que la actividad no define.
    while True:  # Repite la solicitud mientras no se reciba un número aceptable.
        try:  # Protege la conversión de texto a decimal frente a entradas incorrectas.
            texto = input(mensaje + ": ").replace(",", ".")  # Acepta tanto coma como punto para separar decimales.
            promedio = float(texto)  # Convierte el texto en un número decimal.
            if promedio >= 0 and isfinite(promedio):  # Rechaza negativos, infinito y valores indefinidos.
                return promedio  # Devuelve el promedio aceptado.
            print("El promedio debe ser un número finito mayor o igual que cero.")  # Explica la regla.
        except ValueError:  # Captura entradas que no pueden convertirse en un decimal.
            print("Ingresa un promedio numérico, por ejemplo 4.2.")  # Orienta al usuario sobre el formato.

def esperar_volver():  # Mantiene visible el resultado hasta que el usuario decida regresar.
    print("\n0. Volver al menú anterior")  # Presenta la opción para regresar sin cerrar el sistema.
    while True:  # Espera una opción válida antes de abandonar esta pantalla.
        opcion = input("Selecciona una opción: ").strip()  # Lee la decisión y elimina espacios sobrantes.
        if opcion == "0":  # Reconoce la opción de volver al menú que abrió esta pantalla.
            return  # Termina la espera y permite regresar al menú anterior.
        print("Opción no válida. Escribe 0 para volver.")  # Mantiene la pantalla ante una opción incorrecta.
