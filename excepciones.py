# Excepciones de matrícula: las clases del dominio las lanzan y main.py las captura.

class EstudianteYaMatriculadoError(Exception):  # Distingue el intento de repetir un código en el mismo grupo.
    pass  # Hereda de Exception el almacenamiento del mensaje del error.

class GrupoLlenoError(Exception):  # Indica que no hay cupos disponibles para otra matrícula.
    pass  # El método que detecta el problema proporciona un mensaje comprensible.

class EstudianteNoMatriculadoError(Exception):  # Indica que el código solicitado no pertenece al grupo.
    pass  # Permite capturar este rechazo sin finalizar el programa.
