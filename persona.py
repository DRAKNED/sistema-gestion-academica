# Persona contiene la información común de estudiantes, docentes y administrativos.

class Persona:  # Define la clase base que reutilizarán los tres tipos de personas.
    def __init__(self, identificacion, nombre, correo):  # Inicializa los datos de una nueva persona.
        self.__identificacion = identificacion  # Guarda la identificación como atributo encapsulado.
        self.__nombre = nombre  # Guarda el nombre como atributo encapsulado.
        self.set_correo(correo)  # Utiliza la misma validación del correo al crear y al modificar.

    def get_identificacion(self):  # Permite consultar la identificación sin acceder directamente al atributo.
        return self.__identificacion  # Devuelve el valor guardado en este objeto.

    def get_nombre(self):  # Permite consultar el nombre sin acceder directamente al atributo.
        return self.__nombre  # Devuelve el valor guardado en este objeto.

    def get_correo(self):  # Permite consultar el correo sin acceder directamente al atributo.
        return self.__correo  # Devuelve el valor guardado en este objeto.


    def set_correo(self, correo):  # Permite cambiar el correo de manera controlada.
        if correo.strip() == "":  # Rechaza un correo vacío o formado solamente por espacios.
            raise ValueError("El correo no puede estar vacío.")  # Informa del error antes de modificar el dato.
        self.__correo = correo.strip()  # Guarda el nuevo correo solo cuando supera la validación.

    def mostrar_informacion(self):  # Presenta los datos comunes que heredan las clases hijas.
        print("Identificación:", self.__identificacion)  # Muestra la identificación de esta persona.
        print("Nombre:", self.__nombre)  # Muestra el nombre de esta persona.
        print("Correo:", self.__correo)  # Muestra el correo actual de esta persona.

    def realizar_actividad_principal(self):  # Define un comportamiento general que las clases hijas sobrescriben.
        print("Actividad: participa en la comunidad académica.")  # Muestra la actividad general de una persona.
