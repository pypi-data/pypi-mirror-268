"""
Paquete para dar formato a la salida de la CLI.
"""

# Variables con los estilos para aplicar al texto y los datos de los diferentes tipos de mensajes.
from outputstyles.variables import all_styles, error_data, warning_data, success_data, info_data

# Funciones para aplicarles los estilos al texto.
from outputstyles.apply_styles import apply_styles, add_icono, create_arg, add_text_styles

# Funciones de los diferentes tipos de mensajes.
from outputstyles.msg_type import error, warning, success, info, bold
