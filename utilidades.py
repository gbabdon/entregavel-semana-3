def celsius_para_fahrenheit(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32


def validar_senha(senha):
    """Verifica se uma senha possui pelo menos 8 caracteres."""
    if len(senha) >= 8:
        return True
    return False


def calcular_total(*precos):
    """Soma todos os preços recebidos."""
    total = 0

    for preco in precos:
        total += preco

    return total


def criar_ficha_aluno(**dados):
    """Exibe uma ficha textual com os dados do aluno."""
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


def adicionar_item(lista_original, item):
    """Adiciona um item a uma cópia da lista sem alterar a original."""
    nova_lista = lista_original.copy()
    nova_lista.append(item)

    return nova_lista
