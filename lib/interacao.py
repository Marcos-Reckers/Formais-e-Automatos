from lib.estados import *
from lib.auxiliar import *

def escolher_interacao(pedido):
    print("Escolha o modo de interacao:\n")
    print("Real")
    print("Automatico")
    pedido.interacao = input("\nDigite o modo de interacao: ")

    if pedido.interacao == "Automatico":
        nome_arquivo = input("Digite o nome do arquivo: ")
        with open(nome_arquivo, "r") as arquivo:
            for line in arquivo.readlines():
                pedido.entradas_arquivo.append(line.strip())
        print(pedido.entradas_arquivo)
        print(len(pedido.entradas_arquivo))
        print(pedido.indice)
        clear()
        return estado_inicial(pedido)

    elif pedido.interacao == "Real":
        clear()
        return estado_inicial(pedido)

    else:
        clear()
        print("Interacao invalida\n\n")
        return escolher_interacao(pedido)