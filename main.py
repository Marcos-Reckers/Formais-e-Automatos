class pedido:
    def __init__(self , usuario, senha, recheio, recheio_adicional, salada, molho, molho_adicional , bebida, forma_entrega, numero_cartao, senha_cartao):
        self.usuario = usuario
        self.senha = senha
        self.recheio = recheio
        self.recheio_adicional = recheio_adicional
        self.salada = salada
        self.molho = molho
        self.molho_adicional = molho_adicional
        self.bebida = bebida
        self.forma_entrega = forma_entrega
        self.numero_cartao = numero_cartao
        self.senha_cartao = senha_cartao


def estado_inicial():
    print("Bem vindo ao sistema de pedidos")
    pedido.usuario = input("Digite seu nome de usuário: ")
    if pedido.usuario != ["admin", "user1", "user2", "user3", "user4", "user5"]:
        print("Usuário inválido")
        return estado_inicial()
    else:
        return senha_inicial(pedido)

def senha_inicial(pedido):
    senha = input("Digite sua senha: ")
    if senha == pedido.senha:
        return None
    else:
        print("Senha inválida")
        return estado_inicial()

def qual_recheio(pedido):
    print("Escolha o recheio do seu sanduíche:")
    print("Frango")
    print("Carne")
    print("vegetariano")
    print("Voltar")

    recheio = input("Digite o recheio: ")

    if recheio == "Voltar":
        return estado_inicial()
    
    elif recheio != ["Frango", "Carne", "vegetariano"]:
        print("Recheio inválido")
        return estado_inicial()
    
    else :
        pedido.recheio = recheio
        return pedido.recheio

def adicional_recheio(pedido):
    print("Escolha o recheio adicional do seu sanduíche:")
    print("Frango")
    print("Carne")
    print("vegetariano")
    print("Cancelar")

    recheio_adicional = input("Digite o recheio: ")

    if recheio_adicional == "Cancelar":
        return qual_salada(pedido)
    
    elif recheio_adicional != ["Frango", "Carne", "vegetariano"]:
        print("Recheio adicional inválido")
        return estado_inicial()
    
    else :
        pedido.recheio_adicional = recheio_adicional
        return pedido.recheio_adicional

def qual_salada(pedido):
    print("Escolha a salada do seu sanduíche:")
    print("Alface")
    print("Tomate")
    print("Cenoura")
    print("Sem salada")
    print("Voltar")

    salada = input("Digite a salada: ")

    if salada == "Voltar":
        return qual_recheio(pedido)
    
    elif salada != ["Alface", "Tomate", "Cenoura", "Sem salada"]:
        print("Salada inválida")
        return estado_inicial()
    
    else :
        pedido.salada = salada
        return pedido.salada

def qual_molho(pedido):
    print("Escolha o molho do seu sanduíche:")
    print("Maionese")
    print("Ketchup")
    print("Mostarda")
    print("Sem molho")
    print("Voltar")

    molho = input("Digite o molho: ")

    if molho == "Voltar":
        return qual_salada(pedido)
    
    elif molho != ["Maionese", "Ketchup", "Mostarda", "Sem molho"]:
        print("Molho inválido")
        return estado_inicial()
    
    else :
        pedido.molho = molho
        return pedido.molho

def adicional_molho(pedido):
    print("Escolha o molho adicional do seu sanduíche:")
    print("Maionese")
    print("Ketchup")
    print("Mostarda")
    print("Cancelar")

    molho_adicional = input("Digite o molho: ")

    if molho_adicional == "Cancelar":
        return qual_bebida(pedido)
    
    elif molho_adicional != ["Maionese", "Ketchup", "Mostarda"]:
        print("Molho adicional inválido")
        return estado_inicial()
    
    else :
        pedido.molho_adicional = molho_adicional
        return pedido.molho_adicional

def qual_bebida(pedido):
    print("Escolha a bebida do seu sanduíche:")
    print("Refrigerante")
    print("Suco")
    print("Água")
    print("Voltar")

    bebida = input("Digite a bebida: ")

    if bebida == "Voltar":
        return qual_molho(pedido)
    
    elif bebida != ["Refrigerante", "Suco", "Água"]:
        print("Bebida inválida")
        return estado_inicial()
    
    else :
        return bebida

def confirmacao_pedido(pedido):
    print("Seu pedido foi realizado com sucesso")
    # print("Fazer outro pedido") #todo
    print("Qual a forma de entrega?")
    print("Retirar no balcão")
    print("Entrega")
    print("Voltar a editar o pedido")

    entrega = input("Digite a opção: ")

    if entrega == "Voltar a editar o pedido":
        return qual_bebida(pedido)
    
    elif entrega != ["Retirar no balcão", "Entrega"]:
        print("Opção de entrega inválida")
        return estado_inicial()
    
    else :
        pedido.forma_entrega = entrega
        return pedido.forma_entrega

def pagamento(pedido):
    cartão = input("Digite o número do cartão: ")
    if cartão != pedido.numero_cartao:
        print("Número de cartão inválido")
        return pagamento(pedido)
    else:
        return None

def senha_cartao(pedido):
    senha = input("Digite a senha do cartão: ")
    if senha == pedido.senha_cartao:
        return None
    else:
        while (senha != pedido.senha_cartao or tentativas < 3):
            print("Senha inválida")
            senha = input("Digite a senha do cartão: ")
            if senha == pedido.senha_cartao:
                return None
            tentativas += 1
        print("Número de tentativas excedido")
        return estado_inicial()

def main():
    
    pedido.numero_cartao = 123456789
    pedido.senha_cartao = 1234

    estado_inicial(pedido)
    qual_recheio(pedido)
    adicional_recheio(pedido)
    qual_salada(pedido)
    qual_molho(pedido)
    adicional_molho(pedido)
    qual_bebida(pedido)
    confirmacao_pedido(pedido)
    pagamento(pedido)
    senha_cartao(pedido)

    print("Obrigado por utilizar o sistema de pedidos")
    print("Seu pedido é:")
    print("Recheio: ", pedido.recheio)
    print("Recheio adicional: ", pedido.recheio_adicional)
    print("Salada: ", pedido.salada)
    print("Molho: ", pedido.molho)
    print("Molho adicional: ", pedido.molho_adicional)
    print("Bebida: ", pedido.bebida)
    print("Forma de entrega: ", pedido.forma_entrega)    
# def main():
#     usuario = estado_inicial()
#     senha = senha_inicial()
    
#     if usuario != "admin":
#         print("Usuário inválido")
#         return estado_inicial()
    
#     if senha != "1234":
#         print("Senha inválida")
#         return estado_inicial()
    
#     else:
#         recheio()
#         salada()
#         molho()
#         bebida()
#         pedido()
#         pagamento()
#         senha_cartao()

#         print("Obrigado por utilizar o sistema de pedidos")
#         print("Seu pedido é:")
#         print("Recheio: ", recheio)
#         print("Salada: ", salada)
#         print("Molho: ", molho)
#         print("Bebida: ", bebida)
#         print("Entrega: ", pedido)


#         return estado_inicial()
    
# main()
