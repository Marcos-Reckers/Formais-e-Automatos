import os
from lib.pedido import Pedido

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

def estado_inicial(pedido):
    if pedido.interacao == "Automatico":
        pedido.usuario = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Bem vindo ao sistema de pedidos")
        pedido.usuario = input("Digite seu nome de usuário: ")
    
    return senha_inicial(pedido)

def senha_inicial(pedido):
    if pedido.interacao == "Automatico":
        pedido.senha = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    else:
        pedido.senha = input("Digite sua senha: ")
        clear()
    return qual_recheio(pedido)

def qual_recheio(pedido):
    if pedido.interacao == "Automatico":
        pedido.recheio = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Escolha o recheio do seu sanduíche:\n")
        print("Frango")
        print("Carne")
        print("Vegetariano")
        print("\nVoltar")
        pedido.recheio = input("\nDigite o recheio: ")
    
    if pedido.recheio == "Voltar":
        clear()
        return estado_inicial(pedido)
    
    elif not pedido.recheio in ["Frango", "Carne", "Vegetariano"]:
        clear()
        print("Recheio inválido\n\n")
        return escolher_interacao(pedido)
    
    else :
        clear()
        return adicional1(pedido)

def adicional1(pedido): 
    if pedido.interacao == "Automatico":
        pedido.adicional1 = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print('Deseja adicional de recheio?\n')
        print('Sim')
        print('Nao')
        pedido.adicional1 = input('\nSelecione uma opção: ')
    
    if pedido.adicional1 == 'Sim':
        clear()
        return adicional_recheio(pedido)
    
    elif pedido.adicional1 == 'Nao':
        clear()
        return qual_salada(pedido)
    
    else:
        clear()
        print('Opção inválida')
        return escolher_interacao(pedido)

def adicional_recheio(pedido):
    if pedido.interacao == "Automatico":
        pedido.recheio_adicional = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Escolha o recheio adicional do seu sanduíche:\n")
        print("Frango")
        print("Carne")
        print("Vegetariano")
        print("Cancelar adicional")
        pedido.recheio_adicional = input("\nDigite o recheio: ")
    
    if pedido.recheio_adicional == "Cancelar adicional":
        clear()
        return qual_salada(pedido)
    
    elif not pedido.recheio_adicional in ["Frango", "Carne", "Vegetariano"]:
        clear()
        print("Recheio adicional inválido\n\n")
        return escolher_interacao(pedido)
    
    else :
        clear()
        return qual_salada(pedido)

def qual_salada(pedido):
    if pedido.interacao == "Automatico":
        pedido.salada = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Escolha a salada do seu sanduíche:\n")
        print("Alface")
        print("Tomate")
        print("Cenoura")
        print("Sem salada")
        print("\nVoltar")
        pedido.salada = input("Digite a salada: ")
    
    if pedido.salada == "Voltar":
        clear()
        return qual_recheio(pedido)
    
    elif not pedido.salada in ["Alface", "Tomate", "Cenoura", "Sem salada"]:
        clear()
        print("Salada inválida")
        return escolher_interacao(pedido)
    
    else :
        clear()
        return qual_molho(pedido)

def qual_molho(pedido):
    if pedido.interacao == "Automatico":
        pedido.molho = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Escolha o molho do seu sanduíche:\n")
        print("Maionese")
        print("Ketchup")
        print("Mostarda")
        print("Sem molho")
        print("\nVoltar")
        pedido.molho = input("Digite o molho: ")
    
    if pedido.molho == "Voltar":
        clear()
        return qual_salada(pedido)
    
    elif not pedido.molho in ["Maionese", "Ketchup", "Mostarda", "Sem molho"]:
        clear()
        print("Molho inválido\n\n")
        return escolher_interacao(pedido)
    
    else :
        clear()
        return adicional2(pedido)

def adicional2(pedido):
    if pedido.interacao == "Automatico":
        pedido.adicional2 = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print('Deseja adicional de molho?\n')
        print('Sim')
        print('Nao')
        pedido.adicional2 = input('Selecione uma opção: ')
    
    if pedido.adicional2 == 'Sim':
        clear()
        return adicional_molho(pedido)
    
    elif pedido.adicional2 == 'Nao':
        clear()
        return qual_bebida(pedido)
    
    else:
        clear()
        print('Opção inválida')
        return escolher_interacao(pedido)

def adicional_molho(pedido):
    if pedido.interacao == "Automatico":
        pedido.molho_adicional = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Escolha o molho adicional do seu sanduíche:\n")
        print("Maionese")
        print("Ketchup")
        print("Mostarda")
        print("Cancelar adicional")
        pedido.molho_adicional = input("Digite o molho: ")
    
    if pedido.molho_adicional == "Cancelar adicional":
        clear()
        return qual_bebida(pedido)
    
    elif not pedido.molho_adicional in ["Maionese", "Ketchup", "Mostarda"]:
        clear()
        print("Molho adicional inválido\n\n")
        return escolher_interacao(pedido)
    
    else :
        clear()
        return qual_bebida(pedido)

def qual_bebida(pedido):
    if pedido.interacao == "Automatico":
        pedido.bebida = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Escolha a bebida do seu sanduíche:\n")
        print("Refrigerante")
        print("Suco")
        print("Água")
        print("\nVoltar")
        pedido.bebida = input("Digite a bebida: ")
    
    if pedido.bebida == "Voltar":
        clear()
        return qual_molho(pedido)
    
    elif not pedido.bebida in ["Refrigerante", "Suco", "Água"]:
        clear()
        print("Bebida inválida")
        return escolher_interacao(pedido)
    
    else:
        clear()
        return confirmacao_pedido(pedido)

def confirmacao_pedido(pedido):
    if pedido.interacao == "Automatico":
        novo_pedido = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Seu pedido foi registrado com sucesso\n\n")
        print("Deseja adicionar mais um pedido?\n")
        print("Sim")
        print("Nao")
        print("\nVoltar a editar o pedido")
        novo_pedido = input("\nDigite a opção: ")
    
    if novo_pedido == "Voltar a editar o pedido":
        clear()
        return qual_bebida(pedido)
    
    elif novo_pedido == "Sim":
        clear()
        return qual_recheio(pedido)    
    
    elif novo_pedido == "Nao":
        clear()
        return entrega(pedido)
    
    else:
        clear()
        print("Opção inválida\n\n")
        return escolher_interacao(pedido)

def entrega(pedido):
    if pedido.interacao == "Automatico":
        pedido.forma_entrega = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Qual a forma de entrega?\n")
        print("Retirar no balcão")
        print("Entrega")
        print("\nVoltar a editar o pedido")
        pedido.forma_entrega = input("\nDigite a opção: ")
    
    if pedido.forma_entrega == "Voltar a editar o pedido":
        clear()
        return confirmacao_pedido(pedido)    
    
    if not pedido.forma_entrega in ["Retirar no balcão", "Entrega"]:
        clear()
        print("Opção inválida\n\n")
        return escolher_interacao(pedido)
    
    else:
        clear()
        return pagamento(pedido)

def pagamento(pedido):
    if pedido.interacao == "Automatico":
        pedido.cartao = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.cartao = input("Digite o número do cartão: ")
        
    
    if len(pedido.cartao) != 16:
        clear()
        print("Número de cartão inválido\n\n")
        return pagamento(pedido)
    
    else:
        clear()
        pedido.senha_cartao = pedido.cartao[-4:]
        return senha_cartao(pedido)

def senha_cartao(pedido):
    
    if pedido.interacao == "Automatico":
        senha = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        senha = input("Digite a senha do cartão: ")
        
    
    if senha == pedido.senha_cartao:
        clear()
        return imprime(pedido)
    
    else:
        tentativas = 0
        while (senha != pedido.senha_cartao or tentativas < 3):
            print("Senha inválida")
            senha = input("Digite a senha do cartão: ")
            if senha == pedido.senha_cartao:
                return imprime(pedido)
            tentativas += 1
        clear()
        print("Número de tentativas excedido")
        return escolher_interacao(pedido)

def imprime(pedido):
    print("==========================================")
    print("Obrigado por utilizar o sistema de pedidos")
    print("==========================================\n")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    
    meupedido = Pedido()
    clear()
    escolher_interacao(meupedido)
    print(meupedido)

if __name__ == "__main__":
    main()
