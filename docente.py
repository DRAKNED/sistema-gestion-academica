# Docente hereda los datos comunes de Persona y agrega la información docente.

from persona import Persona  # Importa la clase que contiene los datos comunes de las personas.

class Docente(Persona):  # Establece la herencia entre Docente y Persona.
    def __init__(self, identificacion, nombre, correo, numero_empleado, facultad, tipo_contratacion, horas_semanales):  # Inicializa un docente.
        super().__init__(identificacion, nombre, correo)  # Inicializa los datos comunes mediante Persona.
        if type(horas_semanales) != int or horas_semanales <= 0:  # Exige una cantidad entera y positiva de horas.
            raise ValueError("Las horas semanales deben ser un entero mayor que cero.")  # Explica el dato inválido.
        self.__numero_empleado = numero_empleado  # Guarda el número de empleado como atributo encapsulado.
        self.__facultad = facultad  # Guarda la facultad donde orienta clases.
        self.__tipo_contratacion = tipo_contratacion  # Guarda el tipo de contratación informado.
        self.__horas_semanales = horas_semanales  # Guarda las horas de trabajo semanales.

    def get_numero_empleado(self):  # Permite consultar el número de empleado sin acceder directamente al atributo.
        return self.__numero_empleado  # Devuelve el valor guardado en este objeto.

    def get_facultad(self):  # Permite consultar la facultad sin acceder directamente al atributo.
        return self.__facultad  # Devuelve el valor guardado en este objeto.

    def get_tipo_contratacion(self):  # Permite consultar el tipo de contratación sin acceder directamente al atributo.
        return self.__tipo_contratacion  # Devuelve el valor guardado en este objeto.

    def get_horas_semanales(self):  # Permite consultar las horas semanales sin acceder directamente al atributo.
        return self.__horas_semanales  # Devuelve el valor guardado en este objeto.


    def mostrar_informacion(self):  # Sobrescribe el método de Persona con la información docente.
        print("\nDOCENTE")  # Identifica el tipo de registro que se presenta.
        super().mostrar_informacion()  # Reutiliza la presentación de los datos comunes.
        print("Número de empleado:", self.__numero_empleado)  # Muestra el número de empleado.
        print("Facultad:", self.__facultad)  # Muestra la facultad del docente.
        print("Tipo de contratación:", self.__tipo_contratacion)  # Muestra la contratación registrada.
        print("Horas semanales:", self.__horas_semanales)  # Muestra las horas semanales registradas.

    def realizar_actividad_principal(self):  # Sobrescribe la actividad general de Persona.
        print("Actividad: orienta clases en la facultad de", self.__facultad)  # Describe la actividad docente.
