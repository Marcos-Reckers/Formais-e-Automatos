from lib.auxiliar import *

def estado_inicial(pedido):
    print("Bem vindo ao sistema de pedidos")
    pedido.usuario = input("Digite seu nome de usuário: ")
    return senha_inicial(pedido)

def senha_inicial(pedido):
    pedido.senha = input("Digite sua senha: ")
    clear()
    return qual_recheio(pedido)


def qual_recheio(pedido):
    print("Escolha o recheio do seu sanduíche:\n")
    print("Frango")
    print("Carne")
    print("Vegetariano")
    print("\nVoltar")

    recheio = input("\nDigite o recheio: ")

    if recheio == "Voltar":
        clear()
        return estado_inicial(pedido)
    
    elif not recheio in ["Frango", "Carne", "Vegetariano"]:
        clear()
        print("Recheio inválido\n\n")
        return estado_inicial(pedido)
    
    else :
        clear()
        pedido.recheio = recheio
        return adicional1(pedido)

def adicional1(pedido):
    print('Deseja adicional de recheio?\n')
    print('Sim')
    print('Não')

    esolha = input('\nSelecione uma opção: ')

    if esolha == 'Sim':
        clear()
        return adicional_recheio(pedido)
    elif esolha == 'Não':
        clear()
        return qual_salada(pedido)
    else:
        clear()
        print('Opção inválida')
        return estado_inicial(pedido)

def adicional_recheio(pedido):
    print("Escolha o recheio adicional do seu sanduíche:\n")
    print("Frango")
    print("Carne")
    print("Vegetariano")
    print("Cancelar adicional")

    recheio_adicional = input("\nDigite o recheio: ")

    if recheio_adicional == "Cancelar adicional":
        clear()
        return qual_salada(pedido)
    
    elif not recheio_adicional in ["Frango", "Carne", "Vegetariano"]:
        clear()
        print("Recheio adicional inválido\n\n")
        return estado_inicial(pedido)
    
    else :
        clear()
        pedido.recheio_adicional = recheio_adicional
        return qual_salada(pedido)

def qual_salada(pedido):
    print("Escolha a salada do seu sanduíche:\n")
    print("Alface")
    print("Tomate")
    print("Cenoura")
    print("Sem salada")
    print("\nVoltar")

    salada = input("Digite a salada: ")

    if salada == "Voltar":
        clear()
        return qual_recheio(pedido)
    
    elif not salada in ["Alface", "Tomate", "Cenoura", "Sem salada"]:
        clear()
        print("Salada inválida")
        return estado_inicial(pedido)
    
    else :
        clear()
        pedido.salada = salada
        return qual_molho(pedido)

def qual_molho(pedido):
    print("Escolha o molho do seu sanduíche:\n")
    print("Maionese")
    print("Ketchup")
    print("Mostarda")
    print("Sem molho")
    print("\nVoltar")

    molho = input("Digite o molho: ")

    if molho == "Voltar":
        clear()
        return qual_salada(pedido)
    
    elif not molho in ["Maionese", "Ketchup", "Mostarda", "Sem molho"]:
        clear()
        print("Molho inválido\n\n")
        return estado_inicial(pedido)
    
    else :
        clear()
        pedido.molho = molho
        return adicional2(pedido)

def adicional2(pedido):
    print('Deseja adicional de molho?\n')
    print('Sim')
    print('Não')

    opção = input('Selecione uma opção: ')

    if opção == 'Sim':
        clear()
        return adicional_molho(pedido)
    elif opção == 'Não':
        clear()
        return qual_bebida(pedido)
    else:
        clear()
        print('Opção inválida')
        return estado_inicial(pedido)

def adicional_molho(pedido):
    print("Escolha o molho adicional do seu sanduíche:\n")
    print("Maionese")
    print("Ketchup")
    print("Mostarda")
    print("Cancelar adicional")

    molho_adicional = input("Digite o molho: ")

    if molho_adicional == "Cancelar adicional":
        clear()
        return qual_bebida(pedido)
    
    elif not molho_adicional in ["Maionese", "Ketchup", "Mostarda"]:
        clear()
        print("Molho adicional inválido\n\n")
        return estado_inicial(pedido)
    
    else :
        clear()
        pedido.molho_adicional = molho_adicional
        return pedido.molho_adicional

def qual_bebida(pedido):
    print("Escolha a bebida do seu sanduíche:\n")
    print("Refrigerante")
    print("Suco")
    print("Água")
    print("\nVoltar")

    bebida = input("Digite a bebida: ")

    if bebida == "Voltar":
        clear()
        return qual_molho(pedido)
    
    elif not bebida in ["Refrigerante", "Suco", "Água"]:
        clear()
        print("Bebida inválida")
        return estado_inicial(pedido)
    
    else :
        clear()
        pedido.bebida = bebida
        return confirmacao_pedido(pedido)

def confirmacao_pedido(pedido):
    print("Seu pedido foi registrado com sucesso\n\n")
    print("Deseja adicionar mais um pedido?\n")
    print("Sim")
    print("Não")
    print("\nVoltar a editar o pedido")

    novo_pedido = input("\nDigite a opção: ")

    if novo_pedido == "Voltar a editar o pedido":
        clear()
        return qual_bebida(pedido)

    elif novo_pedido == "Sim":
        clear()
        return qual_recheio(pedido)
    
    elif novo_pedido == "Não":
        clear()
        return entrega(pedido)
    
    else:
        clear()
        print("Opção inválida\n\n")
        return estado_inicial(pedido)

def entrega(pedido):
    print("Qual a forma de entrega?\n")
    print("Retirar no balcão")
    print("Entrega")
    print("\nVoltar a editar o pedido")

    entrega = input("\nDigite a opção: ")

    if entrega == "Voltar a editar o pedido":
        clear()
        return confirmacao_pedido(pedido)
    
    if not entrega in ["Retirar no balcão", "Entrega"]:
        clear()
        print("Opção inválida\n\n")
        return estado_inicial(pedido)
    
    else:
        clear()
        pedido.entrega = entrega
        return pagamento(pedido)

def pagamento(pedido):
    pedido.cartão = input("Digite o número do cartão: ")
    if len(pedido.cartão) != 16:
        clear()
        print("Número de cartão inválido\n\n")
        return pagamento(pedido)
    else:
        clear()
        pedido.senha_cartao = pedido.cartão[-4:]
        return senha_cartao(pedido)

def senha_cartao(pedido):
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
        return estado_inicial(pedido)
