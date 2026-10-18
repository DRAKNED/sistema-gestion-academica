# Administrativo hereda los datos comunes de Persona y agrega los datos de su trabajo.

from persona import Persona  # Importa la clase base para reutilizar sus atributos y métodos.

class Administrativo(Persona):  # Establece que un administrativo es un tipo de persona.
    def __init__(self, identificacion, nombre, correo, numero_empleado, dependencia, cargo, jornada):  # Inicializa un administrativo.
        super().__init__(identificacion, nombre, correo)  # Inicializa los datos comunes mediante Persona.
        self.__numero_empleado = numero_empleado  # Guarda el número de empleado como atributo encapsulado.
        self.__dependencia = dependencia  # Guarda la dependencia donde trabaja.
        self.__cargo = cargo  # Guarda el cargo que desempeña.
        self.__jornada = jornada  # Guarda la jornada de trabajo informada.

    def get_numero_empleado(self):  # Permite consultar el número de empleado sin acceder directamente al atributo.
        return self.__numero_empleado  # Devuelve el valor guardado en este objeto.

    def get_dependencia(self):  # Permite consultar la dependencia sin acceder directamente al atributo.
        return self.__dependencia  # Devuelve el valor guardado en este objeto.

    def get_cargo(self):  # Permite consultar el cargo sin acceder directamente al atributo.
        return self.__cargo  # Devuelve el valor guardado en este objeto.

    def get_jornada(self):  # Permite consultar la jornada sin acceder directamente al atributo.
        return self.__jornada  # Devuelve el valor guardado en este objeto.


    def mostrar_informacion(self):  # Sobrescribe el método de Persona con los datos administrativos.
        print("\nADMINISTRATIVO")  # Identifica el tipo de registro que se presenta.
        super().mostrar_informacion()  # Muestra los datos comunes mediante el método heredado.
        print("Número de empleado:", self.__numero_empleado)  # Muestra el número de empleado.
        print("Dependencia:", self.__dependencia)  # Muestra la dependencia de trabajo.
        print("Cargo:", self.__cargo)  # Muestra el cargo registrado.
        print("Jornada:", self.__jornada)  # Muestra la jornada registrada.

    def realizar_actividad_principal(self):  # Sobrescribe la actividad general de Persona.
        print("Actividad: trabaja como", self.__cargo, "en", self.__dependencia)  # Describe su actividad administrativa.
