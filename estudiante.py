# Estudiante hereda los datos comunes de Persona y agrega los datos estudiantiles.

from math import isfinite  # Importa una función estándar para rechazar promedios infinitos o indefinidos.
from persona import Persona  # Importa la clase base desde el archivo persona.py.

class Estudiante(Persona):  # Indica que un estudiante también es una persona.
    def __init__(self, identificacion, nombre, correo, codigo_estudiantil, programa, semestre, promedio_acumulado):  # Inicializa un estudiante.
        super().__init__(identificacion, nombre, correo)  # Reutiliza la inicialización de los datos comunes.
        if type(semestre) != int or semestre <= 0:  # Comprueba que el semestre sea un entero positivo.
            raise ValueError("El semestre debe ser un entero mayor que cero.")  # Impide crear el estudiante con ese dato.
        if promedio_acumulado < 0 or not isfinite(promedio_acumulado):  # Rechaza promedios negativos, infinitos o indefinidos.
            raise ValueError("El promedio debe ser un número finito mayor o igual que cero.")  # Explica el error.
        self.__codigo_estudiantil = codigo_estudiantil  # Guarda el código estudiantil como atributo encapsulado.
        self.__programa = programa  # Guarda una referencia al programa que cursa el estudiante.
        self.__semestre = semestre  # Guarda el semestre que cursa el estudiante.
        self.__promedio_acumulado = promedio_acumulado  # Guarda el promedio acumulado del estudiante.

    def get_codigo_estudiantil(self):  # Permite consultar el código estudiantil sin acceder directamente al atributo.
        return self.__codigo_estudiantil  # Devuelve el valor guardado en este objeto.

    def get_programa(self):  # Permite consultar el programa asociado sin acceder directamente al atributo.
        return self.__programa  # Devuelve el valor guardado en este objeto.

    def get_semestre(self):  # Permite consultar el semestre actual sin acceder directamente al atributo.
        return self.__semestre  # Devuelve el valor guardado en este objeto.

    def get_promedio_acumulado(self):  # Permite consultar el promedio acumulado sin acceder directamente al atributo.
        return self.__promedio_acumulado  # Devuelve el valor guardado en este objeto.


    def mostrar_informacion(self):  # Sobrescribe el método de Persona para incluir los datos estudiantiles.
        print("\nESTUDIANTE")  # Identifica el registro que se va a mostrar.
        super().mostrar_informacion()  # Muestra identificación, nombre y correo sin repetir ese código.
        print("Código estudiantil:", self.__codigo_estudiantil)  # Muestra el código del estudiante.
        print("Programa:", self.__programa.get_nombre())  # Obtiene el nombre desde el programa asociado.
        print("Semestre:", self.__semestre)  # Muestra el semestre actual.
        print("Promedio acumulado:", self.__promedio_acumulado)  # Muestra el promedio registrado.

    def realizar_actividad_principal(self):  # Sobrescribe la actividad general de Persona.
        print("Actividad: cursa", self.__programa.get_nombre(), "en el semestre", self.__semestre)  # Describe la actividad estudiantil.
