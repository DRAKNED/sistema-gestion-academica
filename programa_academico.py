# ProgramaAcademico representa un programa de la universidad.

class ProgramaAcademico:  # Agrupa los datos y comportamientos de un programa académico.
    def __init__(self, codigo, nombre, facultad, numero_semestres):  # Inicializa un nuevo programa.
        self.__codigo = codigo  # Guarda el código del programa como atributo encapsulado.
        self.__nombre = nombre  # Guarda el nombre del programa como atributo encapsulado.
        self.__facultad = facultad  # Guarda la facultad a la que pertenece el programa.
        self.set_numero_semestres(numero_semestres)  # Valida la duración antes de guardarla.

    def get_codigo(self):  # Permite consultar el código sin acceder directamente al atributo.
        return self.__codigo  # Devuelve el valor guardado en este objeto.

    def get_nombre(self):  # Permite consultar el nombre sin acceder directamente al atributo.
        return self.__nombre  # Devuelve el valor guardado en este objeto.

    def get_facultad(self):  # Permite consultar la facultad sin acceder directamente al atributo.
        return self.__facultad  # Devuelve el valor guardado en este objeto.

    def get_numero_semestres(self):  # Permite consultar el número de semestres sin acceder directamente al atributo.
        return self.__numero_semestres  # Devuelve el valor guardado en este objeto.


    def set_numero_semestres(self, numero_semestres):  # Controla las modificaciones de la duración.
        if type(numero_semestres) != int or numero_semestres <= 0:  # Exige un entero mayor que cero.
            raise ValueError("Los semestres deben ser un entero mayor que cero.")  # Rechaza el dato inválido.
        self.__numero_semestres = numero_semestres  # Guarda la nueva duración una vez validada.

    def mostrar_informacion(self):  # Presenta todos los datos del programa.
        print("\nPROGRAMA ACADÉMICO")  # Separa visualmente este programa del registro anterior.
        print("Código:", self.__codigo)  # Muestra el código del programa.
        print("Nombre:", self.__nombre)  # Muestra el nombre del programa.
        print("Facultad:", self.__facultad)  # Muestra la facultad del programa.
        print("Número de semestres:", self.__numero_semestres)  # Muestra la duración actual.
