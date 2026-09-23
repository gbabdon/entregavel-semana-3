from calculadora import somar, subtrair, multiplicar, dividir
from utilidades import (
    celsius_para_fahrenheit,
    validar_senha,
    calcular_total,
    criar_ficha_aluno,
    adicionar_item,
)


def main():
    """Executa exemplos de uso dos módulos da atividade."""
    print(f"Soma: {somar(10, 5)}")
    print(f"Subtração: {subtrair(10, 5)}")
    print(f"Multiplicação: {multiplicar(10, 5)}")

    resultado_divisao = dividir(10, 5)

    if resultado_divisao is not None:
        print(f"Divisão: {resultado_divisao}")
    else:
        print("Não é possível dividir por zero.")

    temperatura = celsius_para_fahrenheit(25)
    print(f"Temperatura em Fahrenheit: {temperatura:.2f}")

    senha_valida = validar_senha("12345678")
    print(f"Senha válida: {senha_valida}")

    total = calcular_total(10, 20, 30)
    print(f"Total da caixa: R$ {total:.2f}")

    criar_ficha_aluno(
        nome="Aluno",
        idade=18,
        curso="Engenharia de Software",
    )

    lista_original = ["Python", "Java"]
    nova_lista = adicionar_item(lista_original, "C++")

    print(f"Lista original: {lista_original}")
    print(f"Nova lista: {nova_lista}")


if __name__ == "__main__":
    main()
