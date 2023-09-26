""" Ejercicio Palindromo"""


# Crear una funcion para eliminar los espacios
def eliminar_espacios(texto):
    """Crear variable para guardar el texto sin espacios"""
    texto_sin_espacios = ""
    # iterar todo el texto
    for caracter in texto:
        # verificando si encuentra espacios
        if caracter != " ":
            # Concatenando los caracteres
            texto_sin_espacios += caracter
    # retornando el resultado
    return texto_sin_espacios


# Creando la funcion que verifique si es palindromo o no
def es_palindromo(texto):
    """Pasando el texto sin espacios"""
    texto_sin_espacios = eliminar_espacios(texto)
    # Pasando el texto a miniscula
    texto_sin_espacios = texto_sin_espacios.lower()
    # Dandole la vuelta al texto y retordandolo
    return texto_sin_espacios == texto_sin_espacios[::-1]


# Haciendo pruebas
print("Abba", es_palindromo("Abba"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Reconocer", es_palindromo("reconocer"))
