# Horario representa el día, las horas y el salón de un grupo académico.

from datetime import datetime  # Convierte las horas de texto para poder validarlas y compararlas.

class Horario:  # Es un componente del grupo; no hereda de GrupoAcademico.
    def __init__(self, dia, hora_inicio, hora_finalizacion, salon):  # Recibe horas en formato HH:MM de 24 horas.
        if not isinstance(dia, str) or not dia.strip():  # Exige un día informado como texto.
            raise ValueError("El día del horario no puede estar vacío.")  # Explica el dato rechazado.
        if not isinstance(salon, str) or not salon.strip():  # Exige un salón informado como texto.
            raise ValueError("El salón no puede estar vacío.")  # Impide crear un horario incompleto.
        try:  # Controla horas imposibles o con un formato distinto del solicitado.
            inicio = datetime.strptime(hora_inicio, "%H:%M").time()  # Obtiene una hora comparable.
            fin = datetime.strptime(hora_finalizacion, "%H:%M").time()  # Convierte la hora de finalización.
        except (ValueError, TypeError) as error:  # Identifica entradas que no representan horas válidas.
            raise ValueError("Las horas deben ser textos en formato HH:MM de 24 horas.") from error  # Explica el formato.
        if fin <= inicio:  # Este modelo representa una sesión que comienza y termina el mismo día.
            raise ValueError("La hora de finalización debe ser posterior a la hora de inicio.")  # Rechaza intervalos inválidos.
        self.__dia = dia.strip()  # Conserva el día sin espacios exteriores.
        self.__hora_inicio = inicio  # Almacena la hora validada como un objeto time.
        self.__hora_finalizacion = fin  # Almacena la hora final validada.
        self.__salon = salon.strip()  # Conserva el salón asignado.

    def get_dia(self):  # Permite consultar el día de la sesión.
        return self.__dia  # Devuelve el dato encapsulado.

    def get_hora_inicio(self):  # Presenta la hora de inicio en un formato uniforme.
        return self.__hora_inicio.strftime("%H:%M")  # Devuelve el texto con horas y minutos.

    def get_hora_finalizacion(self):  # Presenta la hora de finalización en un formato uniforme.
        return self.__hora_finalizacion.strftime("%H:%M")  # Devuelve el texto con horas y minutos.

    def get_salon(self):  # Permite consultar el salón.
        return self.__salon  # Devuelve el dato encapsulado.

    def mostrar_informacion(self):  # Muestra los datos del horario que contiene el grupo.
        print("Día:", self.__dia)  # Identifica el día de clase.
        print("Hora de inicio:", self.get_hora_inicio())  # Presenta la hora normalizada.
        print("Hora de finalización:", self.get_hora_finalizacion())  # Presenta la hora final normalizada.
        print("Salón:", self.__salon)  # Identifica el lugar de la sesión.
