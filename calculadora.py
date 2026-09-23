def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a diferença entre dois números."""
    return a - b


def multiplicar(a, b):
    """Retorna o produto de dois números."""
    return a * b


def dividir(a, b):
    """Divide dois números e trata a divisão por zero."""
    if b == 0:
        return None
    return a / b
