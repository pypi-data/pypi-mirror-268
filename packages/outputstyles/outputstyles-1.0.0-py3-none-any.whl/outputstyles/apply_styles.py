"""
Funciones para aplicar los estilos al texto.
"""

# Importar todos los estilos que se le pueden aplicar al texto.
from outputstyles import all_styles


def add_text_styles(text: str, styles: list = [], all_styles: dict = all_styles) -> str:
    """
    Aplicarles los estilos al texto.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    styles (list) [Opcional]: Lista de estilos que se le van a aplicar al texto.
    all_styles (dict): Diccionario con todos los estilos posibles.

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """

    # Comprobar que existan estilos en los argumentos y que sea una lista.
    if not styles or type(styles) != list:
        return text

    # Lista resultante de los estilos que se van a aplicar.
    list_styles = []

    # Resetear estilos al final del texto.
    style_reset = all_styles["reset"]

    # Aplicar los estilos.
    for style in styles:

        # Asignar el estilo de turno.
        try:

            # Agregar el valor del estilo a la lista resultante.
            list_styles.append(all_styles[style])

        # En caso de que no exista el estilo (key), imprimimos un error.
        except KeyError:

            # Definir los diferentes estilos del mensaje de error.
            text_bold = all_styles["bold"]
            text_error = all_styles["fg_red"]

            # Imprimir mensaje de error.
            print(
                f'\033[{text_bold}mEstilo no válido:{style_reset}',
                f'\033[{text_bold};{text_error}m{style}{style_reset}'
            )

    # Concatenamos los estilos separados por ";" con el texto,
    # además de agregarle "\033[" y "m" para que sea válido el código ANSI.
    # Ej: \033[01;91mTexto
    text_with_styles = f'\033[{";".join(list_styles)}m{text}'

    # Retornamos el texto con los estilos aplicados,
    # al inicio y al final reseteamos los estilos.
    return f'{style_reset}{text_with_styles}{style_reset}'


def create_arg(color: str = "", msg_format: str = "") -> list:
    """
    Crear una Lista de los estilos que se le van a aplicar al texto
    en dependencia del tipo de mensaje.

    Parameters:
    color (str) [Opcional]: Color del texto.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico')

    Returns:
    list: Devuelve una lista con los estilos a aplicar.
    - Si no tiene ningún color o el formato no es válido, devuelve el estilo en Negrita [bold]
    - Si es de tipo Botón, con Icono o no, devuelve Negrita, color del Texto y del Fondo [bold, fg_color, bg_color]
    - Por defecto, devuelve Negrita y el color del Texto [bold, fg_color]
    """

    # Comprobar si tiene color el texto y es un formato válido.
    if not color or not msg_format in ["", "ico", "btn", "btn_ico"]:

        # Texto en Negrita.
        return ["bold"]

    # Mensaje de tipo Botón, ya sea con icono o no.
    if msg_format in ["btn", "btn_ico"]:

        # Texto en Negrita, color en blanco y fondo según el color del argumento.
        return ['bold', 'fg_light_white', f'bg_{color}']

    # Retornamos por defecto el texto en Negrita y con el color del argumento.
    return ['bold', f'fg_{color}']


def add_icono(text: str, msg_format: str = "", ico_code: str = "") -> str:
    """
    Agregarle un icono delante del texto del mensaje.

    Parameters:
    text (str): Texto al que se le va a agregar el icono.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    ico_code (str) [Opcional]: Código del icono que se va a agregar.

    Returns:
    srt: Devuelve el texto con icono o no según corresponda.
    """

    # Comprobar si tiene icono el texto y es un formato válido.
    if not ico_code or not msg_format in ["ico", "btn_ico"]:
        return text

    # Si es de tipo Botón con Icono el mensaje.
    if msg_format == "btn_ico":

        # Concatenamos el icono al inicio del texto, dejando un espacio al inicio y final.
        return f' {ico_code} {text} '

    # Concatenamos el icono al inicio del texto.
    return f'{ico_code} {text}'


def apply_styles(text: str, msg_format: str = "", message_data: dict = {}) -> str:
    """
    Retornar el texto con los estilos aplicados, según el tipo de mensaje.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    message_data (dict) [Opcional]: Datos del tipo de mensaje (error_data, warning_data, success_data, info_data).

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """

    # Obtener los valores de los datos del mensaje.
    ico_code = message_data.get("ico_code", "")
    color = message_data.get("color", "")

    # Agregar el icono en caso de que lo lleve.
    text = add_icono(text, msg_format, ico_code)

    # Obtener la Lista de los estilos que se le van a aplicar al texto.
    list_styles = create_arg(color, msg_format)

    # Retornamos el código del texto con los estilos aplicados.
    return add_text_styles(text, list_styles)
