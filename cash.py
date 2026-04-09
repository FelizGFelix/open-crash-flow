import os

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

lista_receita = []
lista_despesa = []

def receita():
    valor1 = float(input("Insira o valor da receita: "))
    valor2 = input("Insira o tipo da receita: ")
    valor_receita = (valor1, valor2)
    lista_receita.append(valor_receita)
    retorno()

def despesa():
    valor1 = float(input("Insira o valor da despesa: "))
    valor2 = input("Insira o tipo da despesa: ")
    valor_despesa = (valor1, valor2)
    lista_despesa.append(valor_despesa)
    retorno()

def retorno():
    input("Digite qualquer valor para voltar: ")
    limpar()
    main()

def main():
    resposta = ""
    
    while resposta != 5:
        resposta = int(input("Selecione uma das opções:\n 1 - Cadastrar receita\n 2 - Cadastrar despesa\n 3 - Abrir receitas\n 4 - Abrir despesas\n 5 - Sair\n-> "))

        if resposta == 1:
            receita()

        elif resposta == 2:
            despesa()

        elif resposta == 3:
            print(lista_receita)
            retorno()

        elif resposta == 4:
            print(lista_despesa)
            retorno()

        elif resposta == 5:
            limpar()
            print("Fechando o programa!")
            break

        else:
            print("Escreva uma opção válida")
            retorno()


if __name__ == "__main__":
    main()