"""
Funciones para los diferentes tipos de mensajes.
    - Error
    - Warning
    - Success
    - Info
    - Bold
"""

# Importar los datos de los diferentes tipos de mensajes y las funciones.
from outputstyles import apply_styles, error_data, info_data, success_data, warning_data


def error(text: str, msg_format: str = "", message_data: dict = error_data) -> str:
    """
    Mensaje de tipo de Error.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    message_data (dict): Datos del tipo de mensaje (error_data).

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """
    return apply_styles(text, msg_format, message_data)


def warning(text: str, msg_format: str = "", message_data: dict = warning_data) -> str:
    """
    Mensaje de tipo de Warning.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    message_data (dict): Datos del tipo de mensaje (warning_data).

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """
    return apply_styles(text, msg_format, message_data)


def success(text: str, msg_format: str = "", message_data: dict = success_data) -> str:
    """
    Mensaje de tipo de Success.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    message_data (dict): Datos del tipo de mensaje (success_data).

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """
    return apply_styles(text, msg_format, message_data)


def info(text: str, msg_format: str = "", message_data: dict = info_data):
    """
    Mensaje de tipo de Info.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    message_data (dict): Datos del tipo de mensaje (info_data).

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """
    return apply_styles(text, msg_format, message_data)


def bold(text: str) -> str:
    """
    Mensaje de tipo de Bold.

    Parameters:
    text (str): Texto que se va a poner en Negrita.

    Returns:
    srt: Devuelve el texto en Negrita.
    """
    return apply_styles(text)
