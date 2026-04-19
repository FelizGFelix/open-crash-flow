import os

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

lista_receita = []
lista_despesa = []

def inserir_receita():
    descricao = input("Insira a descrição da receita: ")
    valor = float(input("Insira o valor da receita: "))
    item_receita = {
        "Descricao" : descricao,
        "Valor" : valor
    }
    lista_receita.append(item_receita)

def inserir_despesa():
    descricao = input("Insira a descrição da despesa: ")
    valor = float(input("Insira o valor da despesa: "))
    item_despesa = {
        "Descricao" : descricao,
        "Valor" : valor
    }
    lista_despesa.append(item_despesa)
    #retorno()

def imprimir_receitas():
    for i in lista_receita:
        print("-----------------------------")
        print("Descrição: ", i['Descricao'])
        print("Valor: ", i["Valor"])

def imprimir_despesas():
    for i in lista_despesa:
        print("------------------------------")
        print("Descrição: ", i["Descricao"])
        print("Valor: ", i["Valor"])


def main():
    resposta = ""
    
    while resposta != 5:
        resposta = int(input("Selecione uma das opções:\n 1 - Cadastrar receita\n 2 - Cadastrar despesa\n 3 - Imprimir receitas\n 4 - Imprimir despesas\n 5 - Sair\n-> "))

        if resposta == 1:
            inserir_receita()

        elif resposta == 2:
            inserir_despesa()

        elif resposta == 3:
            imprimir_receitas()

        elif resposta == 4:
            imprimir_despesas()

        elif resposta == 5:
            limpar()
            print("Fechando o programa!")
            break

        else:
            print("Escreva uma opção válida")

        input("Digite qualquer valor para voltar: ")
        limpar()


if __name__ == "__main__":
    main()