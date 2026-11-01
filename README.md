# Sistema de Gestión Académica

Actividad colaborativa n.º 1 - Programación Orientada a Objetos en Python.

Versión inicial funcional para estudiar, revisar y adaptar en equipo. Primero se ejecuta una demostración automática y después se abre un menú interactivo. Ambos trabajan con los mismos objetos: no son dos programas separados.

## Integrantes

Completar con los nombres reales antes de entregar. El equipo puede tener hasta cinco integrantes; eliminar los espacios que no se utilicen.

1. Pendiente.
2. Pendiente.
3. Pendiente.
4. Pendiente.
5. Pendiente.

## Descripción general

El sistema representa personas de una universidad, programas académicos y asignaturas. Distingue estudiantes, docentes y administrativos mediante herencia, permite modificaciones controladas y genera un reporte conjunto usando polimorfismo.

Funciona en consola. Los datos se conservan en listas y objetos durante la ejecución. No utiliza base de datos ni guarda registros en archivos. Al salir, se pierden las altas y modificaciones realizadas; al ejecutarlo nuevamente, se recrean los datos de ejemplo.

Los nombres y registros iniciales son ficticios. Las duraciones, créditos y demás valores no representan una oferta académica real.

## Estructura de archivos

```text
sistema_gestion_academica/
    main.py
    persona.py
    programa_academico.py
    asignatura.py
    estudiante.py
    docente.py
    administrativo.py
    entradas.py
    README.md
    PRUEBAS_MANUALES.md
    EJEMPLO_EJECUCION.txt
    .gitignore
```

| Archivo | Responsabilidad |
| --- | --- |
| `main.py` | Crea los objetos de ejemplo, realiza las pruebas, genera consultas y administra el menú. |
| `persona.py` | Define Persona con identificación, nombre, correo y comportamientos comunes. |
| `programa_academico.py` | Define ProgramaAcademico con código, nombre, facultad y número de semestres. |
| `asignatura.py` | Define Asignatura con código, nombre, créditos y una referencia a su programa. |
| `estudiante.py` | Define Estudiante, que hereda de Persona y agrega código estudiantil, programa, semestre y promedio acumulado. |
| `docente.py` | Define Docente, que hereda de Persona y agrega número de empleado, facultad, contratación y horas semanales. |
| `administrativo.py` | Define Administrativo, que hereda de Persona y agrega número de empleado, dependencia, cargo y jornada. |
| `entradas.py` | Contiene funciones de lectura de teclado y validación de entradas. No contiene otra aplicación ni otro menú. |
| `PRUEBAS_MANUALES.md` | Explica cómo comprobar el sistema desde el menú. |
| `EJEMPLO_EJECUCION.txt` | Contiene una salida real de la demostración seguida de la opción de salir. No es código ejecutable. |
| `.gitignore` | Indica qué archivos temporales y configuraciones locales no deben subirse al repositorio. |

Cada clase incluye su propio método `__init__()`. Los inicializadores no se guardan en archivos separados de sus clases. Todas las líneas con código Python tienen un comentario explicativo; las líneas vacías se utilizan para separar secciones.

## Requisitos y ejecución

Se necesita Python 3. El proyecto fue probado con Python 3.13.5. No requiere instalar paquetes externos; `math` pertenece a la biblioteca estándar de Python.

Extraer toda la carpeta del ZIP. Abrir una terminal dentro de `sistema_gestion_academica`, donde se encuentra `main.py`, y ejecutar:

```bash
python main.py
```

En Windows, cuando Python esté disponible mediante el lanzador `py`, también puede ejecutarse:

```bash
py main.py
```

No ejecutar solamente un archivo de clase esperando que aparezca el menú. El punto de entrada del proyecto es `main.py` y los demás archivos deben permanecer junto a él. Para usar el menú se necesita una terminal que acepte entrada de teclado.

## Funcionamiento

### Demostración automática

Al iniciar, el programa crea dos programas académicos, dos asignaturas y seis personas: dos estudiantes, dos docentes y dos administrativos.

Luego consulta los programas y asignaturas, modifica correctamente un correo, una duración y una cantidad de créditos, y ejecuta tres intentos inválidos: correo vacío, cero semestres y créditos negativos. Finalmente, presenta los datos y actividades de las seis personas con el recorrido polimórfico.

Los mensajes **Rechazo esperado** son parte de las pruebas, no fallos inesperados. El resultado **True** en las verificaciones de conservación indica que el dato válido anterior no cambió.

Los cambios válidos de la demostración permanecen al entrar al menú: Ana queda con `ana.actualizada@example.com`, el programa `SIS` con 9 semestres y `PROG1` con 4 créditos.

### Menú interactivo

```text
1. Consultar programas académicos
2. Consultar asignaturas
3. Reporte general de personas y actividades
4. Registrar programa académico
5. Registrar asignatura
6. Registrar estudiante, docente o administrativo
7. Modificar datos
0. Salir
```

La opción 6 abre una selección entre estudiante, docente y administrativo. Las personas nuevas se agregan a la misma lista de las seis personas iniciales y aparecen al consultar la opción 3.

Para registrar una asignatura o un estudiante se debe seleccionar un programa existente por su código. Puede registrarse primero un nuevo programa mediante la opción 4 y utilizarlo enseguida. Un código inexistente cancela ese registro y devuelve el control al menú.

La opción 7 permite modificar **correo de una persona, número de semestres de un programa y créditos de una asignatura**. No incluye la edición de todos los atributos ni la eliminación de registros. Los demás datos se ingresan al crear el objeto y se consultan mediante sus métodos.

## Conceptos de POO aplicados

### Clases, objetos e inicializadores

Una clase describe los datos y comportamientos de un tipo de elemento. Un objeto es un ejemplar concreto: `programa_1` es un objeto de ProgramaAcademico y `estudiante_1` es un objeto de Estudiante.

En la actividad se denomina constructor al método `__init__()`, cuya tarea es inicializar los atributos de cada objeto. `self` permite referirse al objeto que está ejecutando el método.

### Encapsulamiento

Los atributos se definen con dos guiones bajos iniciales, como `__correo`. Los métodos de consulta tienen nombres como `get_correo()` y los de modificación como `set_correo()`.

El programa principal consulta y modifica estos datos mediante los métodos de las clases. Los métodos de modificación comprueban el dato antes de asignarlo; si es inválido, conservan el anterior. Los inicializadores de Persona, ProgramaAcademico y Asignatura reutilizan estas validaciones.

En Python, los dos guiones bajos dificultan el acceso accidental mediante un cambio interno del nombre; no constituyen una barrera de seguridad absoluta. El proyecto respeta el acceso controlado mediante sus métodos.

### Herencia

Estudiante, Docente y Administrativo heredan de Persona. `super().__init__()` permite reutilizar la inicialización de identificación, nombre y correo. Cada clase hija agrega solamente sus datos particulares.

### Sobreescritura

Las tres clases hijas tienen sus propias versiones de `mostrar_informacion()` y `realizar_actividad_principal()`. En la presentación, `super().mostrar_informacion()` reutiliza los datos comunes; después se muestran los particulares.

### Polimorfismo

La lista `personas`, creada en `main()`, contiene los tres tipos de personas intercalados. La función `mostrar_reporte_personas()` la recorre con un único `for` e invoca ambos métodos en cada recorrido. No utiliza condicionales para determinar si el objeto es estudiante, docente o administrativo.

Los condicionales del menú seleccionan una operación o una clase que se va a crear; no clasifican los objetos para ejecutar el reporte. Las comprobaciones de tipo de ciertos datos numéricos tampoco forman parte del recorrido polimórfico.

### Relaciones entre objetos

El estudiante y la asignatura guardan el objeto ProgramaAcademico que les corresponde, no una copia de sus datos. Consultan su nombre mediante `get_nombre()`. Esta relación no es herencia: un estudiante cursa un programa, pero no es un programa.

## Validaciones y alcance

La actividad exige impedir correos vacíos, duraciones no positivas y créditos no positivos. Estas comprobaciones están en las clases, no solamente en el menú.

Como decisiones adicionales de esta propuesta, el registro por teclado pide textos no vacíos, evita identificaciones de personas repetidas y evita códigos repetidos de programas o asignaturas. Se utilizan enteros positivos para semestres, créditos y horas semanales. El promedio debe ser un número finito no negativo y puede escribirse con punto o coma decimal.

El documento no establece una escala para el promedio ni exige relacionar el semestre actual con el número total de semestres del programa. Por eso no se agrega un tope de promedio ni una comprobación de ese tipo. Tampoco se valida la sintaxis completa de una dirección de correo: en este ejercicio se comprueba que no esté vacía.

Los códigos estudiantiles y números de empleado se almacenan, pero no se comprueba su unicidad en esta versión. No se implementan matrículas, notas por asignatura, cálculo automático del promedio, autenticación ni almacenamiento permanente.

## Manejo de errores y entradas

`input()` lee texto. `int()` lo convierte a entero y `float()` a decimal. `try` y `except ValueError` permiten avisar de una entrada o modificación incorrecta sin cerrar el programa. `raise ValueError(...)` comunica el rechazo desde una clase.

Las funciones de lectura repiten la pregunta cuando el formato es incorrecto. Una modificación rechazada por la clase regresa al menú principal sin alterar el dato anterior. La opción 0 finaliza el programa; Ctrl+C también permite interrumpirlo.

## Pruebas y relación con la actividad

| Fase | Dónde se evidencia |
| --- | --- |
| 1. Modelado inicial | Persona, ProgramaAcademico y Asignatura; creación y consulta de objetos en main. |
| 2. Protección y modificación | Atributos encapsulados, métodos de consulta y modificación, función demostrar_modificaciones. |
| 3. Diferenciación de personas | Estudiante, Docente y Administrativo heredan de Persona. |
| 4. Comportamientos particulares | Las clases hijas sobrescriben los dos métodos solicitados. |
| 5. Procesamiento conjunto | Una lista con seis personas y un único ciclo en mostrar_reporte_personas. |

Las pruebas mínimas se ejecutan al iniciar `main.py`; no hace falta ejecutar otro programa. `PRUEBAS_MANUALES.md` contiene ejercicios adicionales para probar las entradas del menú.

La versión preparada fue verificada en un entorno de Python 3.13.5 mediante ejecución de la demostración, registro manual simulado de los tres tipos de personas, consultas, modificaciones válidas e inválidas, rechazo de duplicados y reinicio sin persistencia. El equipo debe repetir las pruebas en su propio entorno y registrar su revisión real.

## Entrega y trabajo en equipo

Subir la carpeta del proyecto a un único repositorio de GitHub y compartir el enlace real de ese repositorio. No entregar solamente el ZIP en lugar del enlace exigido por la actividad.

Cada integrante debe aportar como mínimo un commit relacionado con un trabajo real de desarrollo. Los nombres, aportes y revisiones del equipo no se han completado ni simulado en este material.

Identificar la versión entregada con una etiqueta, por ejemplo `entrega-actividad-1`. Conservar esa versión sin cambios y realizar la evolución posterior del mismo proyecto en commits posteriores a la etiqueta, según las condiciones de la actividad. El historial de desarrollo no se crea automáticamente al recibir estos archivos.

## Declaración de uso de inteligencia artificial

Se utilizó ChatGPT como apoyo para interpretar los requisitos, proponer la organización del sistema y generar, comentar y verificar esta versión inicial del código y su documentación.

Antes de entregar, el equipo debe revisar el material, comprenderlo, adaptarlo cuando corresponda y documentar sus propias contribuciones. Esta declaración debe mantenerse y actualizarse para reflejar el uso real de la herramienta. No debe afirmarse una revisión humana ni una participación que no se haya realizado.

## Documento base

Requisitos tomados de **Actividad colaborativa N°1. Construcción de un Sistema de Gestión Académica utilizando Programación Orientada a Objetos**, Universidad de Manizales, documento proporcionado para esta actividad: fases 1 a 5, pruebas mínimas, entregables y uso de herramientas de inteligencia artificial.

El menú, la entrada de datos y los comentarios en cada línea se incorporaron por solicitud adicional del estudiante. No se presentan como exigencias literales del documento universitario.


## Actividad Colaborativa 2 — avance de grupos y horarios

Este apartado actualiza el estado del proyecto y conserva arriba el documento anterior como referencia. Las menciones anteriores a una demostración automática, a `demostrar_modificaciones` y a pruebas que se ejecutan al iniciar no describen el código actual: `main.py` carga los ejemplos y abre el menú. Las búsquedas de códigos inexistentes repiten la solicitud; no cancelan automáticamente el registro. Los nombres de integrantes siguen pendientes de completar por el equipo.

### Alcance de este avance

Se conserva la abstracción de Persona incorporada en el primer avance de AC2. Se agregan Horario y GrupoAcademico, dos grupos iniciales y la opción 8 para consultarlos. Las opciones 1 a 7 y 0 conservan sus funciones. Matrícula, retiro y excepciones personalizadas quedan pendientes del siguiente avance; esta no es todavía la entrega final AC2.

`Horario` contiene día, hora inicial, hora final y salón. Recibe las horas como texto HH:MM de 24 horas y las guarda como objetos `time`. Valida los datos y exige que el final sea posterior al inicio dentro del mismo día. No contempla sesiones que atraviesen medianoche ni verifica cruces de horarios.

`GrupoAcademico` recibe objetos Asignatura y Docente ya creados y conserva esas referencias. Valida código y capacidad positiva, inicia una lista propia de estudiantes y crea internamente su Horario. Los getters permiten consultar sus datos; `get_estudiantes()` devuelve una copia de la lista para evitar modificaciones externas de la colección.

El grupo contiene un horario como componente de su organización: esta relación es composición. El constructor del grupo crea ese objeto y lo conserva como atributo; el grupo no hereda de Horario porque un grupo no es un horario. Las referencias de Asignatura y Docente se reciben desde fuera y pueden utilizarse en otros grupos. Esta decisión de diseño no implica que Python destruya un horario mientras otra referencia externa todavía lo conserve.

### Integración en el código original y líneas

Las líneas corresponden a los archivos de este avance; futuras adiciones pueden desplazarlas. No se eliminaron funciones, opciones, datos iniciales ni validaciones del código original. Se ampliaron dos líneas existentes: la firma de `ejecutar_menu` y su llamada en `main`. El argumento opcional `grupos=None` conserva la compatibilidad con llamadas de tres argumentos.

| Archivo | Líneas actuales | Cambio |
| --- | --- | --- |
| `main.py` | 7–7 | Adición |
| `main.py` | 210–222 | Ampliación de línea existente |
| `main.py` | 232–232 | Adición |
| `main.py` | 250–251 | Adición |
| `main.py` | 333–343 | Ampliación de línea existente |
| `horario.py` | 1–39 | Archivo nuevo, con comentarios explicativos |
| `grupo_academico.py` | 1–56 | Archivo nuevo, con comentarios explicativos |

Las adiciones de `main.py` incorporan la importación de GrupoAcademico, la función `mostrar_grupos`, el argumento de grupos, la opción 8 y su atención, y la creación de G001 y G002 con horarios propios. Se conservan los comentarios originales y se documenta la ampliación con comentarios AC2.

### Comprobación manual

Ejecutar `python main.py` desde la carpeta del proyecto. Elegir 8: deben aparecer G001 (Programación I, Laura Gómez, lunes 08:00–10:00, A101, capacidad 30) y G002 (Fundamentos de Administración, Carlos Rojas, martes 10:00–12:00, B202, capacidad 25). Ambos deben indicar cero estudiantes. Elegir 0 para volver; elegir 3 para consultar el reporte polimórfico y 0 para regresar. Finalmente, elegir 0 para salir.

### Uso de inteligencia artificial en este avance

Se utilizó Codex como apoyo para añadir y comentar las clases, integrar la consulta en el menú y preparar verificaciones. El equipo debe revisar y comprender estos cambios. Esta nota también deberá incorporarse al Documento de Decisiones de Diseño cuando se elabore.

### Verificación realizada en este avance

Se comprobó la consulta de los dos grupos y sus listas vacías, las referencias a los objetos originales, los horarios independientes, la protección de la lista interna y el rechazo de horas, capacidades y referencias inválidas. También se ejecutaron consultas anteriores, el reporte de seis personas, la navegación por los submenús de registro y modificación, y la salida. Las funciones originales distintas de main y ejecutar_menu se compararon estructuralmente y permanecen iguales.

