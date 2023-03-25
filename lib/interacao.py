from lib.estados import estado_inicial
def escolher_interacao(pedido):
    print("Escolha o modo de interacao:")
    print("Real")
    print("Automatica")
    interacao = input("Digite o modo de interacao: ")
    pedido.interacao = interacao

    if interacao == "Automatica":
        nome_arquivo = input("Digite o nome do arquivo: ")
        arquivo = open(nome_arquivo, 'r')
        for line in arquivo.readlines():
            pedido.entradas_arquivo.append(line.strip())
        arquivo.close()

    return estado_inicial(pedido)