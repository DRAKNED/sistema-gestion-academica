# Sistema de Gestión Académica

Actividad Colaborativa 2 — Evolución del Sistema de Gestión Académica. Programación 1, Universidad de Manizales.

El proyecto amplía el sistema de la Actividad Colaborativa 1 con una clase Persona abstracta, grupos académicos, horarios mediante composición y matrícula con excepciones personalizadas. Funciona en consola y permite comprobar los casos de la actividad con datos precargados y las opciones del menú.

## Integrante

**Diego Andrés Echeverry Giraldo**.

## Ejecución

Se requiere Python 3. No es necesario instalar paquetes externos: `abc`, `datetime` y `math` pertenecen a la biblioteca estándar.

Desde una terminal situada en la carpeta que contiene todos los archivos `.py`, ejecutar:

```bash
python main.py
```

En Windows, si se utiliza el lanzador de Python, ejecutar `py main.py`. Se necesita una terminal con entrada de teclado. Al iniciar se muestra el rechazo controlado de una Persona genérica, se crean los datos de ejemplo y se abre el menú principal.

Los datos solo existen durante la ejecución: al cerrar se pierden las matrículas, retiros, registros y modificaciones realizados. Al reiniciar se recuperan los ejemplos iniciales. Los nombres y valores son ficticios.

## Archivos del proyecto

| Archivo | Responsabilidad |
| --- | --- |
| `main.py` | Carga los ejemplos, comprueba la abstracción, administra menús y búsquedas, y captura excepciones. |
| `persona.py` | Clase abstracta con identificación, nombre, correo y método abstracto de actividad. |
| `estudiante.py` | Especialización de Persona con código, programa, semestre y promedio. |
| `docente.py` | Especialización de Persona con información laboral y actividad docente. |
| `administrativo.py` | Especialización de Persona con dependencia, cargo y jornada. |
| `programa_academico.py` | Programa con código, nombre, facultad y duración en semestres. |
| `asignatura.py` | Asignatura con código, nombre, créditos y referencia a su programa. |
| `horario.py` | Día, hora de inicio, hora de finalización y salón. |
| `grupo_academico.py` | Oferta de asignatura, docente, capacidad, horario y estudiantes matriculados. |
| `excepciones.py` | Cinco clases de excepciones personalizadas. |
| `entradas.py` | Lecturas de teclado, validación de entradas y navegación de regreso. |
| `README.md` | Descripción, decisiones principales y guía de comprobación. |
| `.gitignore` | Exclusión de archivos temporales del repositorio. |

Los módulos Python deben permanecer juntos. En la entrega del repositorio, este README se ubica en la raíz, junto a `main.py`. Los scripts auxiliares de preparación y verificación usados durante el desarrollo no son necesarios para ejecutar ni comprobar el sistema.

## Datos iniciales

Se crean dos programas: SIS (Ingeniería de Sistemas, 10 semestres) y ADM (Administración de Empresas, 8 semestres). Las asignaturas son PROG1 (Programación I, 3 créditos, SIS) y ADMI1 (Fundamentos de Administración, 3 créditos, ADM).

| Tipo | Nombre | Identificación | Código estudiantil o número de empleado |
| --- | --- | --- | --- |
| Estudiante | Ana Torres | 1001 | E001 |
| Estudiante | Luis Rivera | 1002 | E002 |
| Docente | Laura Gómez | 2001 | D001 |
| Docente | Carlos Rojas | 2002 | D002 |
| Administrativo | Marta Ruiz | 3001 | A001 |
| Administrativo | Jorge Vera | 3002 | A002 |

Ana cursa SIS y Luis cursa ADM. Las seis personas se conservan en una misma lista para el reporte polimórfico.

| Grupo | Asignatura | Docente | Horario | Salón | Capacidad | Matrículas al iniciar |
| --- | --- | --- | --- | --- | --- | --- |
| G001 | PROG1 | Laura Gómez | Lunes 08:00–10:00 | A101 | 1 | Ana Torres, E001 |
| G002 | ADMI1 | Carlos Rojas | Martes 10:00–12:00 | B202 | 25 | Ninguna |

El único cupo de G001 es una decisión didáctica para comprobar el rechazo por capacidad con los datos existentes. La matrícula inicial de Ana se realiza mediante `matricular_estudiante()`, utilizando las mismas reglas que el menú. G002 permite demostrar una matrícula correcta sin liberar previamente un cupo.

## Menús y uso

```text
1. Consultar programas académicos
2. Consultar asignaturas
3. Reporte general de personas y actividades
4. Registrar programa académico
5. Registrar asignatura
6. Registrar estudiante, docente o administrativo
7. Modificar datos
8. Gestionar grupos académicos
0. Salir
```

La opción 7 permite modificar correo, semestres de un programa y créditos de una asignatura. La opción 8 abre:

```text
1. Consultar grupos y horarios
2. Matricular un estudiante
3. Retirar un estudiante
0. Volver al menú principal
```

Para matricular se elige el código del grupo y la **identificación** del estudiante (1001 o 1002). Para retirar se utiliza el **código estudiantil** (E001 o E002). El retiro elimina solo la matrícula del grupo: la persona permanece registrada. En esas selecciones, 0 permite cancelar. Después de un resultado, 0 regresa al menú que abrió la operación. Para consultar grupos desde el menú principal se elige 8 y luego 1.

Los grupos se precargan en `main.py`; el menú no permite crear grupos nuevos. Se pueden registrar personas, asignaturas y programas mediante las opciones existentes. Las selecciones de programa y asignatura convierten el código a mayúsculas; si no existe, muestran el error y repiten la solicitud. Los códigos de grupo y de retiro deben escribirse exactamente como aparecen.

## Diseño y cuatro fases de la actividad

### Abstracción y herencia

`Persona` hereda de `ABC` y declara `realizar_actividad_principal()` con `@abstractmethod`. No se pueden crear objetos Persona directamente. El intento de `main()` produce un TypeError controlado, distinto de las cinco excepciones personalizadas.

Estudiante, Docente y Administrativo reutilizan identificación, nombre y correo mediante `super().__init__()`. Cada clase implementa su actividad: cursar un programa, orientar clases o desempeñar el cargo administrativo. También amplía `mostrar_informacion()` para presentar sus datos particulares.

### Oferta académica y encapsulamiento

`GrupoAcademico` recibe objetos ya creados de Asignatura y Docente, conserva sus referencias y mantiene una lista de objetos Estudiante. Incluye `mostrar_informacion_grupo()`, `mostrar_estudiantes()`, `matricular_estudiante(estudiante)` y `retirar_estudiante(codigo_estudiantil)`.

Los atributos con doble guion bajo se consultan mediante getters. `get_estudiantes()` devuelve una copia de la lista para evitar cambios externos a la colección interna. El doble guion bajo dificulta el acceso accidental mediante el cambio interno de nombre; no constituye una barrera de seguridad absoluta.

### Composición del horario

El constructor del grupo crea su propio objeto Horario con día, horas y salón, y lo conserva como componente. Un grupo **tiene un horario**; no es un tipo de horario, por lo que esta relación corresponde a composición y no a herencia. Cada grupo crea un horario distinto. En cambio, Asignatura y Docente se reciben desde fuera y pueden relacionarse con varios grupos.

Las horas se reciben como texto, se convierten a objetos `time` y se presentan como HH:MM. El final debe ser posterior al inicio dentro del mismo día. La composición describe el diseño: Python no elimina un objeto mientras existan otras referencias a él.

### Excepciones y continuidad

| Excepción | Dónde se lanza | Condición | Dónde se captura |
| --- | --- | --- | --- |
| `EstudianteYaMatriculadoError` | `GrupoAcademico.matricular_estudiante()` | El código estudiantil ya está en el grupo. | `gestionar_grupos()` en main.py. |
| `GrupoLlenoError` | `GrupoAcademico.matricular_estudiante()` | La ocupación alcanzó la capacidad. | `gestionar_grupos()` en main.py. |
| `EstudianteNoMatriculadoError` | `GrupoAcademico.retirar_estudiante()` | El código no está matriculado en ese grupo. | `gestionar_grupos()` en main.py. |
| `AsignaturaNoEncontradaError` | `buscar_asignatura()` | No se encuentra el código solicitado. | `seleccionar_asignatura()` en main.py. |
| `ProgramaNoEncontradoError` | `buscar_programa()` | No se encuentra el código solicitado. | `seleccionar_programa()` en main.py. |

Cada excepción tiene una clase propia. Las operaciones lanzan el error con `raise`; las funciones de interacción lo capturan con `except`, muestran un mensaje y permiten continuar. Una operación rechazada conserva el estado anterior. La matrícula comprueba primero duplicados y después capacidad: intentar matricular de nuevo a Ana en G001 produce el error de duplicado aunque el grupo esté lleno.

Las búsquedas devuelven los objetos existentes; también lanzan sus excepciones si se busca en una colección vacía. La interfaz detecta previamente listas vacías y permite regresar sin solicitar una búsqueda.

### Polimorfismo conservado

`mostrar_reporte_personas()` recorre una sola lista y llama a `mostrar_informacion()` y `realizar_actividad_principal()` sin clasificar cada objeto. Python ejecuta la implementación de cada clase. El filtro de estudiantes para matricular usa `isinstance`, pero no altera ese reporte polimórfico.

## Guía de comprobación de los requisitos

Iniciar una ejecución nueva y seguir el orden indicado. Cada dato separado por una flecha se introduce por separado, confirmándolo con Enter. Los pasos se realizan desde el menú principal salvo que se indique otra cosa.

| Caso | Pasos | Resultado esperado |
| --- | --- | --- |
| Persona abstracta | Iniciar `main.py`. | Mensaje de que no se puede crear una Persona directamente; después aparece el menú. |
| Objetos y dos grupos con horarios | 1 → 0, después 2 → 0, después 3 → 0 y después 8 → 1 → 0 → 0. | Dos programas, dos asignaturas, seis personas y dos grupos con los horarios indicados. G001 tiene a Ana y G002 está vacío. |
| Matrícula duplicada | 8 → 2 → G001 → 1001 → 0 → 0. | Rechazo porque E001 ya está en G001; la ocupación sigue siendo 1. |
| Capacidad superada | 8 → 2 → G001 → 1002 → 0 → 0. | Rechazo porque G001 está lleno; Luis no se agrega. |
| Matrícula correcta | 8 → 2 → G002 → 1002 → 0 → 1 → 0 → 0. | Confirmación de matrícula; la consulta muestra a Luis en G002. |
| Retiro correcto | 8 → 3 → G001 → E001 → 0 → 1 → 0 → 0. | Confirmación de retiro; G001 queda vacío. Ana sigue en el reporte de personas. |
| Retiro inexistente | 8 → 3 → G001 → E001 → 0 → 0. | Rechazo porque Ana ya no está matriculada en G001; se mantiene vacío. |
| Asignatura inexistente | 7 → 3 → NOEXISTE → PROG1 → 3 → 0 → 0. | Error de asignatura, seguido de una nueva solicitud. Se elige PROG1 y se conservan sus 3 créditos. |
| Programa inexistente | 7 → 2 → NOEXISTE → SIS → 10 → 0 → 0. | Error de programa, seguido de una nueva solicitud. Se elige SIS y se conservan sus 10 semestres. |
| Continuidad y polimorfismo | 3 → 0 y finalmente 0 para salir. | Se muestran las seis personas y sus actividades; el programa termina por elección del usuario. |

Todos los casos se ejecutan desde el archivo principal y sus menús. Solo la comprobación de abstracción y la carga de ejemplos ocurren automáticamente; los cinco errores personalizados se provocan siguiendo esta guía. Para repetir desde el estado inicial, cerrar y volver a ejecutar.

## Validaciones y límites

- Se rechazan correos vacíos, créditos y semestres no positivos, y horas laborales no positivas. El promedio debe ser finito y no negativo; no se impone una escala máxima.
- El registro evita identificaciones de personas repetidas y códigos de programas y asignaturas repetidos. No comprueba la unicidad global de códigos estudiantiles o números de empleado; la matrícula sí evita repetir un código estudiantil dentro de un grupo.
- GrupoAcademico exige una asignatura y un docente del tipo correspondiente, capacidad entera positiva y código no vacío. Horario exige día y salón no vacíos y horas válidas ordenadas.
- No se comprueban cruces de horarios, nombres de días, pertenencia del estudiante al programa de la asignatura ni sesiones que atraviesen medianoche.
- No se incluyen notas por asignatura, cálculo de promedios, autenticación, base de datos ni almacenamiento permanente. Ctrl+C o el fin de entrada cierran la sesión con un aviso.

## Entrega y versiones

Repositorio: [DRAKNED/sistema-gestion-academica](https://github.com/DRAKNED/sistema-gestion-academica).

El repositorio contiene el proyecto ejecutable y este README. Conforme a la organización de entrega indicada por el estudiante, el Documento de Decisiones de Diseño y los soportes adicionales se presentan por separado en la plataforma de la universidad.

`Entrega_AC1` identifica la primera entrega y debe conservarse. `Entrega_AC2` identificará el commit final una vez publicado y revisado; este documento no afirma que esa etiqueta ya se haya creado. El desarrollo es individual y los commits deben reflejar los aportes de Diego Andrés Echeverry Giraldo.

## Uso de inteligencia artificial

Se utilizaron ChatGPT y Codex como apoyo para comprender los requisitos, proponer el diseño, generar y comentar código, revisar errores, preparar pruebas y consolidar la documentación. La comprensión y sustentación del trabajo corresponden al estudiante. Esta declaración también debe figurar en el Documento de Decisiones de Diseño entregado por separado.

## Registro de cambios y ubicación en el código

La versión conserva las funciones de la Actividad 1 y añade abstracción, grupos y horarios, cinco excepciones y gestión de matrícula. La opción 8 pasó de consulta directa a submenú, conservando la consulta dentro de su opción 1. Las búsquedas anteriores se ampliaron con captura de excepciones. Este README reemplaza las notas acumuladas de avances para describir un único estado actual del sistema.

| Archivo | Líneas actuales | Elemento añadido o ampliado para AC2 |
| --- | --- | --- |

| `main.py` | 35–39 | `buscar_programa()` |
| `main.py` | 41–45 | `buscar_asignatura()` |
| `main.py` | 47–62 | `seleccionar_programa()` |
| `main.py` | 64–79 | `seleccionar_asignatura()` |
| `main.py` | 228–235 | `mostrar_grupos()` |
| `main.py` | 237–250 | `seleccionar_grupo()` |
| `main.py` | 252–266 | `seleccionar_estudiante()` |
| `main.py` | 268–304 | `gestionar_grupos()` |
| `main.py` | 307–346 | `ejecutar_menu()` |
| `main.py` | 348–436 | `main()` |
| `persona.py` | 1–33 | Clase Persona abstracta y método abstracto. |
| `horario.py` | 1–39 | Clase o excepciones añadidas para AC2 |
| `grupo_academico.py` | 1–76 | Clase o excepciones añadidas para AC2 |
| `excepciones.py` | 1–17 | Clase o excepciones añadidas para AC2 |

En este último ajuste se añadió la importación de Persona, el intento controlado de instanciación al inicio y la matrícula inicial de Ana. Se cambió únicamente la capacidad de ejemplo de G001 de 30 a 1; G002 conserva 25 cupos. Las demás funciones y opciones del avance anterior se mantienen. Las líneas indicadas corresponden a esta versión y pueden desplazarse con futuras ediciones.

Las adiciones de este último avance en main.py se encuentran en la línea 3 (importación), 351–354 (intento controlado de crear Persona), 426 (capacidad de G001) y 434–435 (matrícula inicial y aviso).

La secuencia completa de la guía se verificó mediante entradas de teclado simuladas: se comprobaron los datos iniciales, las cinco excepciones, las operaciones correctas y la continuidad. Las funciones anteriores fuera de main se compararon estructuralmente y se conservaron.
