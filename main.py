import os
from lib.pedido import Pedido
from lib.GUI import *

def escolher_interacao(pedido):
    pedido.interacao = popup("Qual o modo de interação?", ["Manual", "Automatico"])
    
    if pedido.interacao == "Automatico":
        with open(seleciona_arquivo(), "r") as arquivo:
            for line in arquivo.readlines():
                pedido.entradas_arquivo.append(line.strip())
        return estado_inicial(pedido)
    
    elif pedido.interacao == "Manual":
        return estado_inicial(pedido)

def estado_inicial(pedido):
    if pedido.interacao == "Automatico":
        pedido.usuario = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.usuario = popup_text("Bem vindo ao Sanduicheiro", "Digite seu nome de usuário: ")
    
    return senha_inicial(pedido)

def senha_inicial(pedido):
    if pedido.interacao == "Automatico":
        pedido.senha = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.senha = (popup_text("Bem vindo ao Sanduicheiro", "Digite sua senha: "))
    return qual_recheio(pedido)

def qual_recheio(pedido):
    if pedido.interacao == "Automatico":
        pedido.recheio = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.recheio = popup("Escolha o recheio do seu sanduíche:", ["Frango", "Carne", "Vegetariano", "Voltar"])

    
    if pedido.recheio == "Voltar":
        return estado_inicial(pedido)
    
    elif not pedido.recheio in ["Frango", "Carne", "Vegetariano"]:
        popup_error("Recheio", "Recheio inválido!!!")
        return escolher_interacao(pedido)
    
    else :
        return adicional1(pedido)

def adicional1(pedido): 
    if pedido.interacao == "Automatico":
        pedido.adicional1 = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.adicional1 = popup("Deseja adicionar um recheio adicional?", ["Sim", "Nao"])
    
    if pedido.adicional1 == 'Sim':
        return adicional_recheio(pedido)
    
    elif pedido.adicional1 == 'Nao':
        return qual_salada(pedido)
    
    else:
        popup_error("Adicional1", "Adicional1 escolha inválida!!!")
        return escolher_interacao(pedido)

def adicional_recheio(pedido):
    if pedido.interacao == "Automatico":
        pedido.recheio_adicional = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.recheio_adicional = popup("Escolha o recheio adicional do seu sanduíche:", ["Frango", "Carne", "Vegetariano", "Cancelar adicional"])
    
    if pedido.recheio_adicional == "Cancelar adicional":
        return qual_salada(pedido)
    
    elif not pedido.recheio_adicional in ["Frango", "Carne", "Vegetariano"]:
        popup_error("Recheio Adicional", "Recheio adicional inválido!!!")
        return escolher_interacao(pedido)
    
    else :
        return qual_salada(pedido)

def qual_salada(pedido):
    if pedido.interacao == "Automatico":
        pedido.salada = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.salada = popup("Escolha a salada do seu sanduíche:", ["Alface", "Tomate", "Cenoura", "Sem salada", "Voltar"])
    
    if pedido.salada == "Voltar":
        return qual_recheio(pedido)
    
    elif not pedido.salada in ["Alface", "Tomate", "Cenoura", "Sem salada"]:
        popup_error("Salada", "Salada inválida!!!")
        return escolher_interacao(pedido)
    
    else :
        return qual_molho(pedido)

def qual_molho(pedido):
    if pedido.interacao == "Automatico":
        pedido.molho = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.molho = popup("Escolha o molho do seu sanduíche:", ["Maionese", "Ketchup", "Mostarda", "Sem molho", "Voltar"])
    
    if pedido.molho == "Voltar":
        return qual_salada(pedido)
    
    elif not pedido.molho in ["Maionese", "Ketchup", "Mostarda", "Sem molho"]:
        popup_error("Molho", "Molho inválido!!!")
        return escolher_interacao(pedido)
    
    else :
        return adicional2(pedido)

def adicional2(pedido):
    if pedido.interacao == "Automatico":
        pedido.adicional2 = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.adicional2 = popup("Deseja adicionar um molho adicional?", ["Sim", "Nao"])
    
    if pedido.adicional2 == 'Sim':
        return adicional_molho(pedido)
    
    elif pedido.adicional2 == 'Nao':
        return qual_bebida(pedido)
    
    else:
        popup_error("Adicional", "Adicional2 escolha inválida!!!")
        return escolher_interacao(pedido)

def adicional_molho(pedido):
    if pedido.interacao == "Automatico":
        pedido.molho_adicional = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.molho_adicional = popup("Escolha o molho adicional do seu sanduíche:", ["Maionese", "Ketchup", "Mostarda", "Cancelar adicional"])
    
    if pedido.molho_adicional == "Cancelar adicional":
        return qual_bebida(pedido)
    
    elif not pedido.molho_adicional in ["Maionese", "Ketchup", "Mostarda"]:
        popup_error("Molho Adicional", "Molho adicional inválido!!!")
        return escolher_interacao(pedido)
    
    else :
        return qual_bebida(pedido)

def qual_bebida(pedido):
    if pedido.interacao == "Automatico":
        pedido.bebida = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.bebida = popup("Escolha a bebida do seu sanduíche:", ["Refrigerante", "Suco", "Agua", "Voltar"])
    
    if pedido.bebida == "Voltar":
        return qual_molho(pedido)
    
    elif not pedido.bebida in ["Refrigerante", "Suco", "Agua"]:
        popup_error("Bebida", "Bebida inválida!!!")
        return escolher_interacao(pedido)
    
    else:
        return confirmacao_pedido(pedido)

def confirmacao_pedido(pedido):
    if pedido.interacao == "Automatico":
        novo_pedido = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        novo_pedido = popup("Deseja adicionar mais algum item ao seu pedido?", ["Sim", "Nao", "Voltar a editar o pedido"])
    
    if novo_pedido == "Voltar a editar o pedido":
        return qual_bebida(pedido)
    
    elif novo_pedido == "Sim":
        return qual_recheio(pedido)    
    
    elif novo_pedido == "Nao":
        return entrega(pedido)
    
    else:
        popup_error("Novo Pedido", "Escolha de confirmação de pedido inválida!!!")
        return escolher_interacao(pedido)

def entrega(pedido):
    if pedido.interacao == "Automatico":
        pedido.forma_entrega = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.forma_entrega = popup("Escolha a forma de entrega do seu pedido:", ["Retirar no balcao", "Entrega", "Voltar a editar o pedido"])
    
    if pedido.forma_entrega == "Voltar a editar o pedido":
        return confirmacao_pedido(pedido)    
    
    if not pedido.forma_entrega in ["Retirar no balcao", "Entrega"]:
        popup_error("Forma de Entrega", "Forma de entrega inválida!!!")
        return escolher_interacao(pedido)
    
    else:
        clear()
        return pagamento(pedido)

def pagamento(pedido):
    if pedido.interacao == "Automatico":
        if pedido.indice < len(pedido.entradas_arquivo):
            pedido.cartao = pedido.entradas_arquivo[pedido.indice]
            pedido.indice = pedido.indice + 1
        
        else :
            popup_error("Cartão", "Número de cartão inválido!!!")
            return escolher_interacao(pedido)
    
    else:
        pedido.cartao = popup_text('Cartão de Crédito' ,"Digite o número do cartão: ")
    
    if len(pedido.cartao) != 16:
        popup_error("Cartão", "Quantidade de dígitos inválida!!!")
        return pagamento(pedido)
    
    else:
        pedido.senha_cartao = pedido.cartao[-4:]
        return senha_cartao(pedido)

def senha_cartao(pedido):
    
    if pedido.interacao == "Automatico":
        senha = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        senha = popup_text('Senha do Cartão' ,"Digite a senha do cartão: ")
    
    if senha == pedido.senha_cartao:
        return imprime(pedido)
    
    else:
        tentativas = 0
        while (senha != pedido.senha_cartao and tentativas < 4):
            if pedido.interacao == "Automatico":
                if pedido.indice < len(pedido.entradas_arquivo):
                    pedido.cartao = pedido.entradas_arquivo[pedido.indice]
                    pedido.indice = pedido.indice + 1
            
            else:
                popup_error("Senha do Cartão", "Senha do cartão inválida!!!")
                senha = popup_text('Senha do Cartão' ,"Digite a senha do cartão: ")
            
            if senha == pedido.senha_cartao:
                return imprime(pedido)
            tentativas += 1
        popup_error("Senha do Cartão", "Numero de tentativas esgotadas!!!")
        return escolher_interacao(pedido)

def imprime(pedido):
    popup_error("Pedido", "Pedido realizado com sucesso!!!")
    
    return main()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    meupedido = Pedido()
    escolher_interacao(meupedido)
    print(meupedido)

if __name__ == "__main__":
    main()
