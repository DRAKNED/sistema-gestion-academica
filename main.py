# Archivo principal: carga los objetos iniciales y permite operar el sistema mediante menús.

from programa_academico import ProgramaAcademico  # Importa la clase que representa los programas.
from asignatura import Asignatura  # Importa la clase que representa las asignaturas.
from estudiante import Estudiante  # Importa la clase hija que representa los estudiantes.
from docente import Docente  # Importa la clase hija que representa los docentes.
from excepciones import EstudianteYaMatriculadoError, GrupoLlenoError, EstudianteNoMatriculadoError  # AC2: rechazos de matrícula y retiro.
from grupo_academico import GrupoAcademico  # AC2: incorpora los grupos que crean su propio horario.
from administrativo import Administrativo  # Importa la clase hija que representa los administrativos.
from entradas import leer_texto, leer_entero, leer_entero_positivo, leer_promedio  # Importa las lecturas de teclado.
from entradas import esperar_volver  # Importa la espera para volver al menú anterior.

def mostrar_programas(programas):  # Consulta todos los programas registrados durante esta ejecución.
    print("\n--- PROGRAMAS REGISTRADOS ---")  # Presenta el encabezado de la consulta.
    for programa in programas:  # Recorre los objetos de la lista de programas.
        programa.mostrar_informacion()  # Solicita a cada programa que presente sus datos.
    esperar_volver()  # Conserva el resultado visible hasta elegir 0 para regresar.

def mostrar_asignaturas(asignaturas):  # Consulta todas las asignaturas registradas.
    print("\n--- ASIGNATURAS REGISTRADAS ---")  # Presenta el encabezado de la consulta.
    for asignatura in asignaturas:  # Recorre los objetos de la lista de asignaturas.
        asignatura.mostrar_informacion()  # Solicita a cada asignatura que presente sus datos.
    esperar_volver()  # Conserva el resultado visible hasta elegir 0 para regresar.

def mostrar_reporte_personas(personas):  # Genera el reporte polimórfico de la única lista de personas.
    print("\n--- REPORTE GENERAL DE PERSONAS ---")  # Presenta el encabezado del reporte.
    print("Personas registradas:", len(personas))  # Informa cuántas personas contiene la lista compartida.
    for persona in personas:  # Un único ciclo procesa estudiantes, docentes y administrativos juntos.
        persona.mostrar_informacion()  # Python ejecuta la versión propia del objeto sin preguntar su tipo.
        persona.realizar_actividad_principal()  # Ejecuta la actividad propia del mismo objeto.
    esperar_volver()  # Conserva el resultado visible hasta elegir 0 para regresar.

def seleccionar_programa(programas):  # Busca un registro existente por su identificador.
    if len(programas) == 0:  # Comprueba si existen registros antes de solicitar una selección.
        print("No hay registros disponibles para seleccionar.")  # Informa que no puede completarse esta operación.
        esperar_volver()  # Espera la decisión de regresar al menú anterior.
        return None  # Indica que no se seleccionó ningún objeto.
    print("\n--- PROGRAMAS DISPONIBLES ---")  # Identifica los registros que pueden elegirse.
    for programa in programas:  # Recorre los objetos para presentar sus identificadores.
        print(programa.get_codigo(), "-", programa.get_nombre())  # Consulta los datos mediante métodos.
    while True:  # Mantiene la selección cuando el identificador ingresado no existe.
        dato = leer_texto("Código del programa")  # Solicita el identificador del registro que se desea seleccionar.
        dato = dato.upper()  # Convierte el código a mayúsculas para buscarlo.
        for programa in programas:  # Busca la coincidencia dentro de los registros existentes.
            if programa.get_codigo() == dato:  # Compara identificadores, no tipos de objetos.
                return programa  # Devuelve el objeto existente en lugar de crear una copia.
        print("No se encontró ese registro. Intenta de nuevo.")  # Conserva la selección actual.

def seleccionar_asignatura(asignaturas):  # Busca un registro existente por su identificador.
    if len(asignaturas) == 0:  # Comprueba si existen registros antes de solicitar una selección.
        print("No hay registros disponibles para seleccionar.")  # Informa que no puede completarse esta operación.
        esperar_volver()  # Espera la decisión de regresar al menú anterior.
        return None  # Indica que no se seleccionó ningún objeto.
    print("\n--- ASIGNATURAS DISPONIBLES ---")  # Identifica los registros que pueden elegirse.
    for asignatura in asignaturas:  # Recorre los objetos para presentar sus identificadores.
        print(asignatura.get_codigo(), "-", asignatura.get_nombre())  # Consulta los datos mediante métodos.
    while True:  # Mantiene la selección cuando el identificador ingresado no existe.
        dato = leer_texto("Código de la asignatura")  # Solicita el identificador del registro que se desea seleccionar.
        dato = dato.upper()  # Convierte el código a mayúsculas para buscarlo.
        for asignatura in asignaturas:  # Busca la coincidencia dentro de los registros existentes.
            if asignatura.get_codigo() == dato:  # Compara identificadores, no tipos de objetos.
                return asignatura  # Devuelve el objeto existente en lugar de crear una copia.
        print("No se encontró ese registro. Intenta de nuevo.")  # Conserva la selección actual.

def seleccionar_persona(personas):  # Busca un registro existente por su identificador.
    if len(personas) == 0:  # Comprueba si existen registros antes de solicitar una selección.
        print("No hay registros disponibles para seleccionar.")  # Informa que no puede completarse esta operación.
        esperar_volver()  # Espera la decisión de regresar al menú anterior.
        return None  # Indica que no se seleccionó ningún objeto.
    print("\n--- PERSONAS DISPONIBLES ---")  # Identifica los registros que pueden elegirse.
    for persona in personas:  # Recorre los objetos para presentar sus identificadores.
        print(persona.get_identificacion(), "-", persona.get_nombre())  # Consulta los datos mediante métodos.
    while True:  # Mantiene la selección cuando el identificador ingresado no existe.
        dato = leer_texto("Identificación de la persona")  # Solicita el identificador del registro que se desea seleccionar.
        for persona in personas:  # Busca la coincidencia dentro de los registros existentes.
            if persona.get_identificacion() == dato:  # Compara identificadores, no tipos de objetos.
                return persona  # Devuelve el objeto existente en lugar de crear una copia.
        print("No se encontró ese registro. Intenta de nuevo.")  # Conserva la selección actual.

def registrar_programa(programas):  # Agrega un nuevo programa a la lista utilizada por todo el sistema.
    print("\n--- REGISTRAR PROGRAMA ---")  # Identifica la operación que se va a realizar.
    codigo = leer_texto("Código")  # Solicita un código no vacío.
    codigo = codigo.upper()  # Convierte el código a mayúsculas antes de guardarlo.
    for programa in programas:  # Comprueba que el código no esté registrado.
        if programa.get_codigo() == codigo:  # Detecta un código de programa repetido.
            print("Ese código de programa ya existe.")  # Explica por qué no se creará el registro.
            esperar_volver()  # Permite leer el motivo del rechazo antes de regresar.
            return  # Regresa al menú sin agregar un programa duplicado.
    nombre = leer_texto("Nombre")  # Solicita el nombre del programa.
    facultad = leer_texto("Facultad")  # Solicita la facultad del programa.
    semestres = leer_entero_positivo("Número de semestres")  # Solicita una duración positiva.
    programa = ProgramaAcademico(codigo, nombre, facultad, semestres)  # Crea el objeto usando su inicializador.
    programas.append(programa)  # Agrega el objeto a la lista que permanecerá en memoria.
    print("Programa registrado correctamente.")  # Confirma que la operación terminó.
    esperar_volver()  # Mantiene la confirmación hasta que el usuario decida regresar.

def registrar_asignatura(programas, asignaturas):  # Agrega una asignatura relacionada con un programa existente.
    print("\n--- REGISTRAR ASIGNATURA ---")  # Identifica la operación de registro.
    codigo = leer_texto("Código")  # Solicita el código de la asignatura.
    codigo = codigo.upper()  # Convierte el código a mayúsculas antes de guardarlo.
    for asignatura in asignaturas:  # Revisa los códigos de las asignaturas existentes.
        if asignatura.get_codigo() == codigo:  # Detecta si ya se utilizó el código ingresado.
            print("Ese código de asignatura ya existe.")  # Informa el motivo del rechazo.
            esperar_volver()  # Permite leer el motivo del rechazo antes de regresar.
            return  # Cancela el registro sin modificar la lista.
    nombre = leer_texto("Nombre")  # Solicita el nombre de la asignatura.
    creditos = leer_entero_positivo("Número de créditos")  # Solicita una cantidad positiva de créditos.
    programa = seleccionar_programa(programas)  # Obtiene el programa al que pertenecerá la asignatura.
    if programa is None:  # Comprueba si faltan programas para completar el registro.
        return  # Cancela el registro porque falta un programa válido.
    asignatura = Asignatura(codigo, nombre, creditos, programa)  # Relaciona la asignatura con el objeto programa.
    asignaturas.append(asignatura)  # Agrega la asignatura a la lista compartida.
    print("Asignatura registrada correctamente.")  # Confirma que el registro quedó disponible en memoria.
    esperar_volver()  # Mantiene la confirmación hasta que el usuario decida regresar.

def completar_registro_persona(opcion, programas, personas):  # Completa el tipo elegido sin guardar datos parciales.
    print("\n--- REGISTRAR PERSONA ---")  # Identifica el formulario de la persona que se va a crear.
    identificacion = leer_texto("Identificación")  # Lee la identificación como texto para conservar ceros iniciales.
    for persona in personas:  # Revisa la identificación en toda la comunidad académica.
        if persona.get_identificacion() == identificacion:  # Evita registrar dos personas con la misma identificación.
            print("Esa identificación ya está registrada.")  # Informa del registro repetido.
            esperar_volver()  # Permite leer el motivo del rechazo antes de regresar.
            return  # Cancela la operación sin afectar los registros existentes.
    nombre = leer_texto("Nombre")  # Solicita el dato común nombre una sola vez.
    correo = leer_texto("Correo")  # Solicita un correo no vacío para cualquiera de los tres tipos.
    if opcion == "1":  # Decide qué clase crear según la opción del menú, no según un objeto del reporte.
        codigo = leer_texto("Código estudiantil")  # Solicita el código particular del estudiante.
        programa = seleccionar_programa(programas)  # Selecciona un programa que ya existe en el sistema.
        if programa is None:  # Comprueba que el estudiante tenga un programa existente.
            return  # Cancela el registro cuando no se seleccionó un programa.
        semestre = leer_entero_positivo("Semestre")  # Solicita el semestre actual como entero positivo.
        promedio = leer_promedio("Promedio acumulado")  # Solicita un promedio numérico.
        persona = Estudiante(identificacion, nombre, correo, codigo, programa, semestre, promedio)  # Crea el estudiante.
    elif opcion == "2":  # Atiende la opción de crear un docente.
        numero_empleado = leer_texto("Número de empleado")  # Solicita el número de empleado como texto.
        facultad = leer_texto("Facultad")  # Solicita la facultad del docente.
        contratacion = leer_texto("Tipo de contratación")  # Solicita el tipo de contratación.
        horas = leer_entero_positivo("Horas semanales")  # Solicita las horas como entero positivo.
        persona = Docente(identificacion, nombre, correo, numero_empleado, facultad, contratacion, horas)  # Crea el docente.
    else:  # Atiende la opción 3, validada previamente, para crear un administrativo.
        numero_empleado = leer_texto("Número de empleado")  # Solicita el número de empleado como texto.
        dependencia = leer_texto("Dependencia")  # Solicita la dependencia donde trabaja.
        cargo = leer_texto("Cargo")  # Solicita el cargo que desempeña.
        jornada = leer_texto("Jornada")  # Solicita la jornada de trabajo.
        persona = Administrativo(identificacion, nombre, correo, numero_empleado, dependencia, cargo, jornada)  # Crea el administrativo.
    personas.append(persona)  # Agrega el nuevo objeto a la misma lista utilizada por el reporte.
    print("Persona registrada correctamente.")  # Confirma que el objeto se puede consultar desde el reporte.
    esperar_volver()  # Mantiene la confirmación hasta que el usuario decida regresar.

def registrar_persona(programas, personas):  # Mantiene abierto el submenú de tipos de persona.
    while True:  # Permite realizar varios registros o volver al menú principal por decisión del usuario.
        print("\n=== REGISTRAR PERSONA ===")  # Presenta el nombre del submenú actual.
        print("1. Estudiante")  # Presenta la opción de crear un estudiante.
        print("2. Docente")  # Presenta la opción de crear un docente.
        print("3. Administrativo")  # Presenta la opción de crear un administrativo.
        print("0. Volver al menú principal")  # Permite regresar sin entrar en un formulario.
        opcion = input("Selecciona una opción: ").strip()  # Solicita la opción de este submenú.
        if opcion == "0":  # Reconoce la decisión de abandonar el submenú.
            return  # Regresa al menú principal que abrió esta función.
        if opcion != "1" and opcion != "2" and opcion != "3":  # Comprueba que la opción de registro exista.
            print("Opción no válida. Selecciona una opción de este menú.")  # Informa del error.
            continue  # Repite este mismo submenú en lugar de regresar al principal.
        try:  # Controla los rechazos de las clases sin abandonar el submenú de personas.
            completar_registro_persona(opcion, programas, personas)  # Abre el formulario del tipo seleccionado.
        except ValueError as error:  # Recibe un error de validación sin cerrar el sistema.
            print("Operación rechazada:", error)  # Explica por qué no se completó el registro.
            esperar_volver()  # Espera la confirmación antes de presentar otra vez este submenú.

def modificar_datos(programas, asignaturas, personas):  # Mantiene disponibles las modificaciones permitidas.
    while True:  # Conserva este submenú hasta que se elija volver al menú principal.
        print("\n=== MODIFICAR DATOS ===")  # Identifica el submenú actual.
        print("1. Correo de una persona")  # Ofrece modificar el dato común de cualquier persona.
        print("2. Semestres de un programa")  # Ofrece modificar la duración de un programa.
        print("3. Créditos de una asignatura")  # Ofrece modificar los créditos de una asignatura.
        print("0. Volver al menú principal")  # Permite salir del submenú sin iniciar un cambio.
        opcion = input("Selecciona una opción: ").strip()  # Lee la operación elegida.
        if opcion == "0":  # Comprueba si se desea regresar al menú anterior.
            return  # Regresa al menú principal sin cambiar ningún dato.
        if opcion != "1" and opcion != "2" and opcion != "3":  # Rechaza opciones que no aparecen en este menú.
            print("Opción no válida. Selecciona una opción de este menú.")  # Explica el error.
            continue  # Repite este mismo submenú y no salta al principal.
        try:  # Permite que los métodos de las clases rechacen datos sin abandonar el submenú.
            if opcion == "1":  # Atiende la modificación del correo.
                persona = seleccionar_persona(personas)  # Busca la persona por su identificación.
                if persona is None:  # Comprueba si faltan registros para completar la operación.
                    continue  # Vuelve al submenú de modificaciones sin solicitar el correo.
                print("Correo actual:", persona.get_correo())  # Consulta el valor previo al cambio.
                correo = input("Nuevo correo: ").strip()  # Lee el correo y permite probar el rechazo de un texto vacío.
                persona.set_correo(correo)  # Valida el correo antes de reemplazar el dato encapsulado.
                print("Correo actualizado:", persona.get_correo())  # Presenta el valor aceptado por la clase.
            elif opcion == "2":  # Atiende la modificación de la duración de un programa.
                programa = seleccionar_programa(programas)  # Busca el programa existente.
                if programa is None:  # Comprueba si faltan programas para completar la operación.
                    continue  # Conserva el submenú de modificaciones sin aplicar cambios.
                print("Semestres actuales:", programa.get_numero_semestres())  # Presenta la duración anterior.
                semestres = leer_entero("Nuevo número de semestres")  # Acepta cero y negativos para probar la clase.
                programa.set_numero_semestres(semestres)  # Deja que la clase acepte o rechace el nuevo valor.
                print("Semestres actualizados:", programa.get_numero_semestres())  # Informa el resultado aceptado.
            else:  # Atiende la opción 3, comprobada antes de iniciar la operación.
                asignatura = seleccionar_asignatura(asignaturas)  # Busca la asignatura existente por código.
                if asignatura is None:  # Comprueba si faltan asignaturas para completar la operación.
                    continue  # Mantiene abierto el submenú de modificaciones.
                print("Créditos actuales:", asignatura.get_numero_creditos())  # Consulta el valor previo al cambio.
                creditos = leer_entero("Nuevo número de créditos")  # Permite probar cero y números negativos.
                asignatura.set_numero_creditos(creditos)  # Valida el dato dentro de la clase correspondiente.
                print("Créditos actualizados:", asignatura.get_numero_creditos())  # Muestra los créditos aceptados.
        except ValueError as error:  # Captura un rechazo antes de que el programa abandone el submenú.
            print("Operación rechazada:", error)  # Explica que el dato anterior no fue reemplazado.
        esperar_volver()  # Mantiene visible el resultado o rechazo hasta elegir volver a este submenú.

# AC2: consulta agregada; conserva las funciones de consulta de la primera actividad.
def mostrar_grupos(grupos):  # Presenta los grupos, sus horarios y sus estudiantes.
    print("\n--- GRUPOS ACADÉMICOS ---")  # Identifica la nueva consulta.
    if not grupos:  # También permite consultar una colección sin grupos.
        print("No hay grupos académicos registrados.")  # Explica por qué no se muestran registros.
    for grupo in grupos:  # Recorre los objetos creados en main.
        grupo.mostrar_informacion_grupo()  # Muestra la asignatura, el docente, los cupos y el horario.
        grupo.mostrar_estudiantes()  # Informa el estado de las matrículas del grupo.
    esperar_volver()  # Conserva la misma navegación de las consultas anteriores.

def seleccionar_grupo(grupos):  # AC2: permite elegir un grupo existente o cancelar la operación.
    if not grupos:  # Evita solicitar códigos cuando la colección está vacía.
        print("No hay grupos académicos registrados.")  # Explica por qué no se puede continuar.
        return None  # Señala que no se seleccionó un grupo.
    for grupo in grupos:  # Presenta los identificadores disponibles.
        print(grupo.get_codigo(), "-", grupo.get_asignatura().get_nombre())  # Consulta los objetos existentes.
    while True:  # Permite corregir un código inexistente.
        codigo = leer_texto("Código del grupo (0 para cancelar)")  # Lee el identificador sin modificar los códigos registrados.
        if codigo == "0":  # Ofrece una salida del proceso de selección.
            return None  # Cancela sin modificar matrículas.
        for grupo in grupos:  # Busca una coincidencia exacta con el código mostrado.
            if grupo.get_codigo() == codigo:  # Identifica el grupo seleccionado.
                return grupo  # Devuelve el mismo objeto almacenado en la colección.
        print("No se encontró ese grupo. Intenta de nuevo.")  # Mantiene abierta la selección.

def seleccionar_estudiante(personas):  # AC2: obtiene un estudiante registrado sin alterar el reporte polimórfico.
    estudiantes = [persona for persona in personas if isinstance(persona, Estudiante)]  # Excluye docentes y administrativos de la matrícula.
    if not estudiantes:  # Comprueba que existan estudiantes disponibles.
        print("No hay estudiantes registrados.")  # Orienta al usuario a registrar uno desde el menú principal.
        return None  # Cancela la selección vacía.
    for estudiante in estudiantes:  # Muestra códigos e identificaciones para distinguir registros.
        print(estudiante.get_identificacion(), "-", estudiante.get_codigo_estudiantil(), "-", estudiante.get_nombre())  # Usa la identificación, que el registro ya exige única.
    while True:  # Permite corregir una identificación inválida.
        identificacion = leer_texto("Identificación del estudiante (0 para cancelar)")  # Selecciona por identificación para evitar ambigüedad entre códigos repetidos.
        if identificacion == "0":  # Permite abandonar la selección.
            return None  # Conserva las matrículas anteriores.
        for estudiante in estudiantes:  # Busca únicamente entre objetos Estudiante.
            if estudiante.get_identificacion() == identificacion:  # Localiza a la persona solicitada.
                return estudiante  # Devuelve el objeto existente, sin crear una copia.
        print("No se encontró ese estudiante. Intenta de nuevo.")  # Solicita otra identificación.

def gestionar_grupos(grupos, personas):  # AC2: reúne consultas, matrícula y retiro en el programa principal.
    while True:  # Conserva el submenú después de cada operación o rechazo.
        print("\n=== GESTIONAR GRUPOS ACADÉMICOS ===")  # Identifica el submenú actual.
        print("1. Consultar grupos y horarios")  # Conserva la consulta que antes abría directamente la opción 8.
        print("2. Matricular un estudiante")  # Ofrece agregar un estudiante existente.
        print("3. Retirar un estudiante")  # Ofrece liberar un cupo por código estudiantil.
        print("0. Volver al menú principal")  # Permite continuar usando las opciones anteriores.
        opcion = input("Selecciona una opción: ").strip()  # Lee la acción elegida.
        if opcion == "0":  # Reconoce la solicitud de volver.
            return  # Termina únicamente este submenú.
        if opcion == "1":  # Reutiliza la consulta existente.
            mostrar_grupos(grupos)  # Incluye las matrículas actualizadas y permite volver.
            continue  # Presenta nuevamente el submenú después de consultar.
        if opcion not in ("2", "3"):  # Rechaza opciones desconocidas antes de pedir datos.
            print("Opción no válida. Selecciona una opción de este menú.")  # Explica el error de navegación.
            continue  # Repite el submenú sin ejecutar operaciones.
        grupo = seleccionar_grupo(grupos)  # Obtiene el grupo sobre el que se operará.
        if grupo is None:  # Detecta una cancelación o la ausencia de grupos.
            continue  # Regresa al submenú sin modificar datos.
        try:  # Captura en main.py los errores lanzados por GrupoAcademico.
            if opcion == "2":  # Atiende una matrícula.
                estudiante = seleccionar_estudiante(personas)  # Obtiene un objeto de la lista actual de personas.
                if estudiante is None:  # Detecta cancelación o ausencia de estudiantes.
                    continue  # Regresa al submenú sin matricular.
                grupo.matricular_estudiante(estudiante)  # Delega las reglas de duplicados y cupos a la clase.
                print("Estudiante matriculado correctamente.")  # Confirma solo después de completar la matrícula.
            else:  # Atiende el retiro, pues la opción 3 ya fue validada.
                codigo = leer_texto("Código estudiantil que deseas retirar (0 para cancelar)")  # Solicita el identificador de la matrícula.
                if codigo == "0":  # Permite cancelar sin intentar un retiro.
                    continue  # Vuelve al submenú.
                grupo.retirar_estudiante(codigo)  # Delega la búsqueda y la eliminación al grupo.
                print("Estudiante retirado correctamente.")  # Confirma que el cupo quedó disponible.
        except (EstudianteYaMatriculadoError, GrupoLlenoError, EstudianteNoMatriculadoError) as error:  # Controla los tres rechazos esperados.
            print("Operación rechazada:", error)  # Muestra el mensaje y conserva la ejecución.
        except ValueError as error:  # Controla también el tipo inválido recibido por el método de matrícula.
            print("Operación rechazada:", error)  # Explica el dato inválido sin cerrar el submenú.
        esperar_volver()  # Permite leer el resultado antes de volver a gestionar grupos.


def ejecutar_menu(programas, asignaturas, personas, grupos=None):  # AC2: añade grupos como argumento opcional.
    if grupos is None:  # Mantiene compatibles las llamadas anteriores que solo pasan tres listas.
        grupos = []  # Usa una lista nueva por llamada cuando no se suministran grupos.
    while True:  # Mantiene el menú disponible hasta que el usuario seleccione salir.
        print("\n=== MENÚ PRINCIPAL ===")  # Separa cada presentación del menú.
        print("1. Consultar programas académicos")  # Muestra la opción de consultar programas.
        print("2. Consultar asignaturas")  # Muestra la opción de consultar asignaturas.
        print("3. Reporte general de personas y actividades")  # Muestra la opción del reporte polimórfico.
        print("4. Registrar programa académico")  # Muestra la opción de crear un programa.
        print("5. Registrar asignatura")  # Muestra la opción de crear una asignatura.
        print("6. Registrar estudiante, docente o administrativo")  # Muestra la opción de crear una persona.
        print("7. Modificar datos")  # Muestra la opción de modificar los datos permitidos.
        print("8. Gestionar grupos académicos")  # AC2: permite consultar, matricular y retirar conservando las demás opciones.
        print("0. Salir")  # Muestra la opción que finaliza la ejecución.
        opcion = input("Selecciona una opción: ").strip()  # Lee la opción del usuario como texto.
        try:  # Permite que las clases rechacen datos sin cerrar el programa.
            if opcion == "1":  # Identifica la consulta de programas.
                mostrar_programas(programas)  # Consulta la lista actual, incluidos los registros nuevos.
            elif opcion == "2":  # Identifica la consulta de asignaturas.
                mostrar_asignaturas(asignaturas)  # Consulta la lista actual de asignaturas.
            elif opcion == "3":  # Identifica la solicitud del reporte general.
                mostrar_reporte_personas(personas)  # Recorre también las personas agregadas manualmente.
            elif opcion == "4":  # Identifica el registro de programas.
                registrar_programa(programas)  # Agrega un programa a la lista compartida.
            elif opcion == "5":  # Identifica el registro de asignaturas.
                registrar_asignatura(programas, asignaturas)  # Permite elegir un programa existente.
            elif opcion == "6":  # Identifica el registro de personas.
                registrar_persona(programas, personas)  # Agrega el objeto al mismo conjunto de personas.
            elif opcion == "7":  # Identifica la modificación controlada de datos.
                modificar_datos(programas, asignaturas, personas)  # Actualiza datos mediante métodos de sus clases.
            elif opcion == "8":  # AC2: abre la gestión de los grupos de esta ejecución.
                gestionar_grupos(grupos, personas)  # Comparte los objetos existentes con el nuevo submenú.
            elif opcion == "0":  # Identifica la solicitud de terminar la sesión.
                print("Sistema cerrado. Los datos de esta ejecución no se guardan.")  # Advierte que no hay persistencia.
                break  # Termina el ciclo del menú y permite finalizar el programa.
            else:  # Atiende cualquier opción que no aparezca en el menú.
                print("Opción no válida. Intenta nuevamente.")  # Informa del error sin cerrar el programa.
        except ValueError as error:  # Recibe los errores de validación de constructores o métodos.
            print("Operación rechazada:", error)  # Explica el error sin cerrar el sistema.
            esperar_volver()  # Mantiene el mensaje visible antes de volver al menú principal.

def main():  # Coordina una única ejecución del sistema, cargando los objetos y abriendo el menú.
    print("=== SISTEMA DE GESTIÓN ACADÉMICA ===")  # Presenta el nombre del proyecto.
    print("Los datos son de ejemplo y solo permanecen durante esta ejecución.")  # Explica el alcance de la sesión.
    programa_1 = ProgramaAcademico("SIS", "Ingeniería de Sistemas", "Ingeniería", 10)  # Crea el primer programa.
    programa_2 = ProgramaAcademico("ADM", "Administración de Empresas", "Ciencias Económicas", 8)  # Crea el segundo programa.
    programas = [programa_1, programa_2]  # Mantiene juntos los dos programas de esta sesión.
    asignatura_1 = Asignatura("PROG1", "Programación I", 3, programa_1)  # Crea una asignatura del primer programa.
    asignatura_2 = Asignatura("ADMI1", "Fundamentos de Administración", 3, programa_2)  # Crea una asignatura del segundo programa.
    asignaturas = [asignatura_1, asignatura_2]  # Mantiene juntas las asignaturas de esta sesión.
    estudiante_1 = Estudiante(  # Inicia la creación de un objeto Estudiante.
        "1001",  # Proporciona la identificación al inicializador.
        "Ana Torres",  # Proporciona el nombre al inicializador.
        "ana@example.com",  # Proporciona el correo al inicializador.
        "E001",  # Proporciona el código estudiantil al inicializador.
        programa_1,  # Proporciona el programa que cursa al inicializador.
        2,  # Proporciona el semestre actual al inicializador.
        4.2,  # Proporciona el promedio acumulado al inicializador.
    )  # Termina la creación del objeto y lo guarda en la variable indicada.
    docente_1 = Docente(  # Inicia la creación de un objeto Docente.
        "2001",  # Proporciona la identificación al inicializador.
        "Laura Gómez",  # Proporciona el nombre al inicializador.
        "laura@example.com",  # Proporciona el correo al inicializador.
        "D001",  # Proporciona el número de empleado al inicializador.
        "Ingeniería",  # Proporciona la facultad al inicializador.
        "Tiempo completo",  # Proporciona el tipo de contratación al inicializador.
        40,  # Proporciona las horas semanales al inicializador.
    )  # Termina la creación del objeto y lo guarda en la variable indicada.
    administrativo_1 = Administrativo(  # Inicia la creación de un objeto Administrativo.
        "3001",  # Proporciona la identificación al inicializador.
        "Marta Ruiz",  # Proporciona el nombre al inicializador.
        "marta@example.com",  # Proporciona el correo al inicializador.
        "A001",  # Proporciona el número de empleado al inicializador.
        "Registro Académico",  # Proporciona la dependencia al inicializador.
        "Auxiliar",  # Proporciona el cargo al inicializador.
        "Diurna",  # Proporciona la jornada al inicializador.
    )  # Termina la creación del objeto y lo guarda en la variable indicada.
    estudiante_2 = Estudiante(  # Inicia la creación de un objeto Estudiante.
        "1002",  # Proporciona la identificación al inicializador.
        "Luis Rivera",  # Proporciona el nombre al inicializador.
        "luis@example.com",  # Proporciona el correo al inicializador.
        "E002",  # Proporciona el código estudiantil al inicializador.
        programa_2,  # Proporciona el programa que cursa al inicializador.
        4,  # Proporciona el semestre actual al inicializador.
        3.8,  # Proporciona el promedio acumulado al inicializador.
    )  # Termina la creación del objeto y lo guarda en la variable indicada.
    docente_2 = Docente(  # Inicia la creación de un objeto Docente.
        "2002",  # Proporciona la identificación al inicializador.
        "Carlos Rojas",  # Proporciona el nombre al inicializador.
        "carlos@example.com",  # Proporciona el correo al inicializador.
        "D002",  # Proporciona el número de empleado al inicializador.
        "Ciencias Económicas",  # Proporciona la facultad al inicializador.
        "Hora cátedra",  # Proporciona el tipo de contratación al inicializador.
        12,  # Proporciona las horas semanales al inicializador.
    )  # Termina la creación del objeto y lo guarda en la variable indicada.
    administrativo_2 = Administrativo(  # Inicia la creación de un objeto Administrativo.
        "3002",  # Proporciona la identificación al inicializador.
        "Jorge Vera",  # Proporciona el nombre al inicializador.
        "jorge@example.com",  # Proporciona el correo al inicializador.
        "A002",  # Proporciona el número de empleado al inicializador.
        "Biblioteca",  # Proporciona la dependencia al inicializador.
        "Asistente",  # Proporciona el cargo al inicializador.
        "Mixta",  # Proporciona la jornada al inicializador.
    )  # Termina la creación del objeto y lo guarda en la variable indicada.

    personas = [  # Crea una única lista con los tres tipos intercalados para demostrar polimorfismo.
        estudiante_1,  # Agrega el primer estudiante a la colección compartida.
        docente_1,  # Agrega el primer docente a la misma colección.
        administrativo_1,  # Agrega el primer administrativo a la misma colección.
        estudiante_2,  # Agrega el segundo estudiante a la misma colección.
        docente_2,  # Agrega el segundo docente a la misma colección.
        administrativo_2,  # Agrega el segundo administrativo a la misma colección.
    ]  # Completa la colección con las seis personas exigidas.
    # AC2: los grupos reutilizan asignaturas y docentes existentes y crean horarios propios.
    grupo_1 = GrupoAcademico(  # Construye el primer grupo de ejemplo.
        "G001", asignatura_1, docente_1, 30,  # Identificador, objetos relacionados y capacidad máxima.
        "Lunes", "08:00", "10:00", "A101",  # Datos con los que el grupo construye su Horario.
    )  # Finaliza la creación del primer grupo sin estudiantes matriculados.
    grupo_2 = GrupoAcademico(  # Construye el segundo grupo de ejemplo.
        "G002", asignatura_2, docente_2, 25,  # Reutiliza la segunda asignatura y el segundo docente.
        "Martes", "10:00", "12:00", "B202",  # Define un horario propio para el segundo grupo.
    )  # Finaliza la creación del segundo grupo sin estudiantes matriculados.
    grupos = [grupo_1, grupo_2]  # Conserva ambos grupos durante esta ejecución del sistema.
    ejecutar_menu(programas, asignaturas, personas, grupos)  # AC2: pasa los grupos y conserva las listas originales.

if __name__ == "__main__":  # Ejecuta main solo al iniciar este archivo y no cuando otro archivo lo importa.
    try:  # Permite terminar ordenadamente si se interrumpe la lectura de teclado.
        main()  # Inicia el sistema sin mostrar consultas ni ejecutar pruebas automáticas.
    except (KeyboardInterrupt, EOFError):  # Captura Ctrl+C o el cierre de la entrada de teclado.
        print("\nEjecución interrumpida. Los datos de esta sesión no se guardan.")  # Informa del cierre sin guardar.