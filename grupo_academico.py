# GrupoAcademico relaciona objetos existentes y crea su propio Horario mediante composición.

from asignatura import Asignatura  # Permite comprobar que se recibe una asignatura real.
from docente import Docente  # Permite comprobar que se recibe un docente real.
from excepciones import EstudianteYaMatriculadoError, GrupoLlenoError, EstudianteNoMatriculadoError  # AC2: rechazos de matrícula y retiro.
from estudiante import Estudiante  # AC2: comprueba que solo se matriculen objetos Estudiante.
from horario import Horario  # Define el componente que cada grupo crea y conserva.

class GrupoAcademico:  # Representa una oferta concreta de una asignatura.
    def __init__(self, codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_finalizacion, salon):  # Recibe objetos y datos del horario.
        if not isinstance(codigo, str) or not codigo.strip():  # Exige un código identificador no vacío.
            raise ValueError("El código del grupo no puede estar vacío.")  # Rechaza un grupo sin identificación.
        if not isinstance(asignatura, Asignatura):  # Evita guardar solamente un nombre o código aislado.
            raise ValueError("El grupo debe recibir un objeto Asignatura ya creado.")  # Explica la relación requerida.
        if not isinstance(docente, Docente):  # Exige un docente del sistema.
            raise ValueError("El grupo debe recibir un objeto Docente ya creado.")  # Explica el objeto esperado.
        if type(capacidad_maxima) != int or capacidad_maxima <= 0:  # Rechaza cupos nulos, negativos, decimales o booleanos.
            raise ValueError("La capacidad máxima debe ser un entero mayor que cero.")  # Informa el requisito.
        self.__codigo = codigo.strip()  # Conserva el identificador del grupo.
        self.__asignatura = asignatura  # Guarda la referencia al objeto existente, sin copiarlo.
        self.__docente = docente  # Guarda la referencia al docente responsable.
        self.__capacidad_maxima = capacidad_maxima  # Conserva el límite de estudiantes.
        self.__estudiantes = []  # Cada grupo comienza con su propia lista vacía.
        self.__horario = Horario(dia, hora_inicio, hora_finalizacion, salon)  # Crea el componente propio del grupo.

    def get_codigo(self):  # Permite consultar el identificador.
        return self.__codigo  # Devuelve el código encapsulado.

    def get_asignatura(self):  # Permite consultar la asignatura relacionada.
        return self.__asignatura  # Devuelve el mismo objeto recibido al construir el grupo.

    def get_docente(self):  # Permite consultar el docente responsable.
        return self.__docente  # Devuelve el mismo objeto recibido al construir el grupo.

    def get_capacidad_maxima(self):  # Permite consultar el límite de cupos.
        return self.__capacidad_maxima  # Devuelve el dato encapsulado.

    def get_estudiantes(self):  # Permite consultar estudiantes sin exponer la lista interna a cambios externos.
        return self.__estudiantes.copy()  # Devuelve una copia de la lista, conservando las referencias a sus objetos.

    def get_horario(self):  # Permite consultar el componente del grupo.
        return self.__horario  # Devuelve el objeto Horario creado por este grupo.

    def mostrar_informacion_grupo(self):  # Presenta la oferta y utiliza métodos de los objetos relacionados.
        print("\nGRUPO ACADÉMICO")  # Identifica el registro mostrado.
        print("Código del grupo:", self.__codigo)  # Muestra el identificador del grupo.
        print("Asignatura:", self.__asignatura.get_codigo(), "-", self.__asignatura.get_nombre())  # Consulta la asignatura.
        print("Docente:", self.__docente.get_nombre())  # Consulta el nombre en el objeto docente.
        print("Capacidad máxima:", self.__capacidad_maxima)  # Presenta el límite de cupos.
        print("Estudiantes matriculados:", len(self.__estudiantes))  # Informa la ocupación actual.
        self.__horario.mostrar_informacion()  # Delega la presentación del horario a su propio componente.

    def mostrar_estudiantes(self):  # Lista los objetos matriculados o informa que el grupo está vacío.
        print("Estudiantes del grupo", self.__codigo)  # Identifica a qué grupo corresponde la consulta.
        if not self.__estudiantes:  # Detecta la lista vacía con la que se crean los grupos.
            print("No hay estudiantes matriculados en este grupo.")  # Explica el estado inicial.
        for estudiante in self.__estudiantes:  # Recorre los estudiantes cuando existan matrículas.
            print(estudiante.get_codigo_estudiantil(), "-", estudiante.get_nombre())  # Consulta los datos de cada objeto.

    def matricular_estudiante(self, estudiante):  # Agrega un objeto Estudiante solo después de validar la operación.
        if not isinstance(estudiante, Estudiante):  # Rechaza nombres aislados y otros tipos de personas.
            raise ValueError("La matrícula requiere un objeto Estudiante.")  # Explica el tipo de dato esperado.
        codigo = estudiante.get_codigo_estudiantil()  # Identifica al estudiante por su código, no por identidad del objeto.
        for matriculado in self.__estudiantes:  # Comprueba duplicados antes de revisar la capacidad.
            if matriculado.get_codigo_estudiantil() == codigo:  # Detecta incluso otro objeto con el mismo código.
                raise EstudianteYaMatriculadoError(f"El estudiante {codigo} ya está matriculado en el grupo {self.__codigo}.")  # Cancela sin modificar la lista.
        if len(self.__estudiantes) >= self.__capacidad_maxima:  # Comprueba si todos los cupos están ocupados.
            raise GrupoLlenoError(f"El grupo {self.__codigo} alcanzó su capacidad máxima de {self.__capacidad_maxima} estudiantes.")  # Informa el límite.
        self.__estudiantes.append(estudiante)  # Conserva el objeto existente una vez aprobada la matrícula.

    def retirar_estudiante(self, codigo_estudiantil):  # Retira únicamente al estudiante identificado dentro de este grupo.
        for estudiante in self.__estudiantes:  # Busca el código entre las matrículas actuales.
            if estudiante.get_codigo_estudiantil() == codigo_estudiantil:  # Comprueba si es el registro solicitado.
                self.__estudiantes.remove(estudiante)  # Libera el cupo sin eliminar a la persona del sistema.
                return  # Termina inmediatamente para no continuar recorriendo la lista modificada.
        raise EstudianteNoMatriculadoError(f"El estudiante {codigo_estudiantil} no está matriculado en el grupo {self.__codigo}.")  # Conserva la lista cuando el código no existe.
