from auxiliar import *

def estado_inicial(pedido):
    print("Bem vindo ao sistema de pedidos")
    pedido.usuario = input("Digite seu nome de usuário: ")

    if not pedido.usuario in ["admin", "user"]:
        clear()
        print("Usuário inválido")
        return estado_inicial(pedido)

    else:
        clear()
        return senha_inicial(pedido)

def senha_inicial(pedido):
    senha = input("Digite sua senha: ")

    if senha == pedido.senha:
        clear()
        return qual_recheio(pedido)

    else:
        clear()
        print("Senha inválida")
        return estado_inicial(pedido)

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
        print("Recheio inválido")
        return estado_inicial(pedido)
    
    else :
        clear()
        pedido.recheio = recheio
        return qual_salada(pedido)

def adicional_recheio(pedido):
    print("Escolha o recheio adicional do seu sanduíche:\n")
    print("Frango")
    print("Carne")
    print("Vegetariano")
    print("Sem adicional")

    recheio_adicional = input("\nDigite o recheio: ")

    if recheio_adicional == "Sem adicional":
        clear()
        return qual_salada(pedido)
    
    elif not recheio_adicional in ["Frango", "Carne", "Vegetariano"]:
        clear()
        print("Recheio adicional inválido")
        return estado_inicial(pedido)
    
    else :
        clear()
        pedido.recheio_adicional = recheio_adicional
        return pedido.recheio_adicional

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
        print("Molho inválido")
        return estado_inicial(pedido)
    
    else :
        clear()
        pedido.molho = molho
        return qual_bebida(pedido)

def adicional_molho(pedido):
    print("Escolha o molho adicional do seu sanduíche:\n")
    print("Maionese")
    print("Ketchup")
    print("Mostarda")
    print("Sem adicional")

    molho_adicional = input("Digite o molho: ")

    if molho_adicional == "Sem adicional":
        clear()
        return qual_bebida(pedido)
    
    elif not molho_adicional in ["Maionese", "Ketchup", "Mostarda"]:
        clear()
        print("Molho adicional inválido")
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
    # print("Fazer outro pedido") #todo
    print("Qual a forma de entrega?\n")
    print("Retirar no balcão")
    print("Entrega")
    print("\nVoltar a editar o pedido")

    entrega = input("\nDigite a opção: ")

    if entrega == "Voltar a editar o pedido":
        clear()
        return qual_bebida(pedido)
    
    elif not entrega in ["Retirar no balcão", "Entrega"]:
        clear()
        print("Opção de entrega inválida")
        return estado_inicial(pedido)
    
    else:
        clear()
        pedido.forma_entrega = entrega
        return pagamento(pedido)

def pagamento(pedido):
    cartão = input("Digite o número do cartão: ")
    if cartão != pedido.numero_cartao:
        clear()
        print("Número de cartão inválido")
        return pagamento(pedido)

    else:
        clear()
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
