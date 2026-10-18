# Asignatura guarda una referencia a un objeto ProgramaAcademico, no solo a su nombre.

class Asignatura:  # Representa una asignatura vinculada a un programa.
    def __init__(self, codigo, nombre, numero_creditos, programa):  # Inicializa una nueva asignatura.
        self.__codigo = codigo  # Guarda el código de la asignatura como atributo encapsulado.
        self.__nombre = nombre  # Guarda el nombre de la asignatura como atributo encapsulado.
        self.__programa = programa  # Conserva el objeto del programa al que pertenece la asignatura.
        self.set_numero_creditos(numero_creditos)  # Valida los créditos antes de guardarlos.

    def get_codigo(self):  # Permite consultar el código sin acceder directamente al atributo.
        return self.__codigo  # Devuelve el valor guardado en este objeto.

    def get_nombre(self):  # Permite consultar el nombre sin acceder directamente al atributo.
        return self.__nombre  # Devuelve el valor guardado en este objeto.

    def get_numero_creditos(self):  # Permite consultar el número de créditos sin acceder directamente al atributo.
        return self.__numero_creditos  # Devuelve el valor guardado en este objeto.

    def get_programa(self):  # Permite consultar el programa asociado sin acceder directamente al atributo.
        return self.__programa  # Devuelve el valor guardado en este objeto.


    def set_numero_creditos(self, numero_creditos):  # Permite modificar los créditos con una validación.
        if type(numero_creditos) != int or numero_creditos <= 0:  # Exige un entero mayor que cero.
            raise ValueError("Los créditos deben ser un entero mayor que cero.")  # Rechaza el dato inválido.
        self.__numero_creditos = numero_creditos  # Guarda los créditos solo después de validarlos.

    def mostrar_informacion(self):  # Presenta los datos de la asignatura y su programa.
        print("\nASIGNATURA")  # Separa visualmente esta asignatura del registro anterior.
        print("Código:", self.__codigo)  # Muestra el código de la asignatura.
        print("Nombre:", self.__nombre)  # Muestra el nombre de la asignatura.
        print("Número de créditos:", self.__numero_creditos)  # Muestra los créditos actuales.
        print("Programa:", self.__programa.get_nombre())  # Consulta el nombre en el objeto ProgramaAcademico.
