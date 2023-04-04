import os
from lib.pedido import Pedido
from lib.GUI import *


# Função para escolher o tipo de interação:
# Manual: O usuário digita os dados
# Automatico: O usuário escolhe um arquivo de entrada
def escolher_interacao(pedido):
    pedido.interacao = popup("Qual o modo de interação?", ["Manual", "Automatico"]) 
    
    if pedido.interacao == "Automatico":
        with open(seleciona_arquivo(), "r") as arquivo:
            for line in arquivo.readlines():
                pedido.entradas_arquivo.append(line.strip())
        return estado_inicial(pedido)
    
    elif pedido.interacao == "Manual":
        return estado_inicial(pedido)


# Função equivalente ao estado inicial do automato (q0)
# Neste estado, o usuário deve digitar seu nome de usuário
# Qualquer conjunto de caracteres é aceito como nome de usuário exeto valores vazios
# Caso o usuário digite um nome de usuário inválido, uma mensagem de erro é exibida
def estado_inicial(pedido):
    if pedido.interacao == "Automatico":
        pedido.usuario = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.usuario = popup_text("Bem vindo ao Sanduicheiro", "Digite seu nome de usuário: ")
        if pedido.usuario == None or pedido.usuario == "":
            popup_notification("Erro", "Nome de usuário inválido")
            return main()
    
    return senha_inicial(pedido)


# Função equivalente ao segundo estado do automato (q1)
# Neste estado, o usuário deve digitar sua senha
# Qualquer conjunto de caracteres é aceito como senha exeto valores vazios
# Caso o usuário digite uma senha inválida, uma mensagem de erro é exibida
def senha_inicial(pedido):
    if pedido.interacao == "Automatico":
        pedido.senha = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.senha = (popup_text("Bem vindo ao Sanduicheiro", "Digite sua senha: "))
        if pedido.senha == None or pedido.senha == "":
            popup_notification("Erro", "Senha inválida")
            return main()
    
    return qual_recheio(pedido)


# Função equivalente ao terceiro estado do automato (q2)
# Neste estado, o usuário deve escolher o recheio do sanduíche
# Os recheios disponíveis são: Frango, Carne, Vegetariano
# Caso o usuário escolha um recheio inválido, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado inicial é chamado novamente
# Como o o usuario apenas pode escolher entre os recheios disponíveis, para testar o estado de erro, basta tentar fechar a janela de seleção de recheio
def qual_recheio(pedido):
    if pedido.interacao == "Automatico":
        pedido.recheio = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.recheio = popup("Escolha o recheio do seu sanduíche:", ["Frango", "Carne", "Vegetariano", "Voltar"], True)

    
    if pedido.recheio == "Voltar":
        return estado_inicial(pedido)
    
    elif not pedido.recheio in ["Frango", "Carne", "Vegetariano"]:
        popup_notification("Recheio", "Recheio inválido!!!")
        return main()
    
    else :
        return adicional1(pedido)


# Função equivalente ao quarto estado do automato (q3)
# Neste estado, o usuário deve escolher se deseja adicionar um recheio adicional
# Caso o usuário escolha sim, o estado de adicionar recheio adicional (q4) é chamado
# Caso o usuário escolha não, o estado de escolher salada (q5) é chamado
# Caso o usuário escolha uma opção inválida, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado de escolher recheio (q2) é chamado
# Como o o usuario apenas pode escolher entre as opções disponíveis, para testar o estado de erro, basta tentar fechar a janela de seleção de adicional
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
        popup_notification("Adicional1", "Adicional1 escolha inválida!!!")
        return main()


# Função equivalente ao quinto estado do automato (q4)
# Neste estado, o usuário deve escolher o recheio adicional do sanduíche
# Os recheios disponíveis são: Frango, Carne, Vegetariano
# Caso o usuário escolha um recheio inválido, uma mensagem de erro é exibida
# Caso o usuário escolha "Cancelar adicional", o estado de escolher salada (q5) é chamado
# Como o o usuario apenas pode escolher entre os recheios disponíveis, para testar o estado de erro, basta tentar fechar a janela de seleção de recheio adicional
def adicional_recheio(pedido):
    if pedido.interacao == "Automatico":
        pedido.recheio_adicional = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.recheio_adicional = popup("Escolha o recheio adicional do seu sanduíche:", ["Frango", "Carne", "Vegetariano", "Cancelar adicional"], True)
    
    if pedido.recheio_adicional == "Cancelar adicional":
        return qual_salada(pedido)
    
    elif not pedido.recheio_adicional in ["Frango", "Carne", "Vegetariano"]:
        popup_notification("Recheio Adicional", "Recheio adicional inválido!!!")
        return main()
    
    else :
        return qual_salada(pedido)


# Função equivalente ao sexto estado do automato (q5)
# Neste estado, o usuário deve escolher a salada do sanduíche
# As saladas disponíveis são: Alface, Tomate, Cenoura, Sem salada
# Caso o usuário escolha uma salada inválida, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado de escolher recheio (q2) é chamado
# Como o o usuario apenas pode escolher entre as saladas disponíveis, para testar o estado de erro, basta tentar fechar a janela de seleção de salada
def qual_salada(pedido):
    if pedido.interacao == "Automatico":
        pedido.salada = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.salada = popup("Escolha a salada do seu sanduíche:", ["Alface", "Tomate", "Cenoura", "Sem salada", "Voltar"], True)
    
    if pedido.salada == "Voltar":
        return qual_recheio(pedido)
    
    elif not pedido.salada in ["Alface", "Tomate", "Cenoura", "Sem salada"]:
        popup_notification("Salada", "Salada inválida!!!")
        return main()
    
    else :
        return qual_molho(pedido)


# Função equivalente ao sétimo estado do automato (q6)
# Neste estado, o usuário deve escolher o molho do sanduíche
# Os molhos disponíveis são: Maionese, Ketchup, Mostarda, Sem molho
# Caso o usuário escolha um molho inválido, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado de escolher salada (q5) é chamado
# Como o o usuario apenas pode escolher entre os molhos disponíveis, para testar o estado de erro, basta tentar fechar a janela de seleção de molho
def qual_molho(pedido):
    if pedido.interacao == "Automatico":
        pedido.molho = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.molho = popup("Escolha o molho do seu sanduíche:", ["Maionese", "Ketchup", "Mostarda", "Sem molho", "Voltar"], True)
    
    if pedido.molho == "Voltar":
        return qual_salada(pedido)
    
    elif not pedido.molho in ["Maionese", "Ketchup", "Mostarda", "Sem molho"]:
        popup_notification("Molho", "Molho inválido!!!")
        return main()
    
    else :
        return adicional2(pedido)


# Função equivalente ao oitavo estado do automato (q7)
# Neste estado, o usuário deve escolher se deseja adicionar um molho adicional ao sanduíche
# As opções disponíveis são: Sim, Não
# Caso escolha "Sim", o estado de escolher molho adicional (q8) é chamado
# Caso escolha "Não", o estado de escolher bebida (q9) é chamado
# Caso o usuário escolha uma opção inválida, uma mensagem de erro é exibida
# Como o o usuario apenas pode escolher entre as opções disponíveis, para testar o estado de erro, basta tentar fechar a janela de seleção de adicional
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
        popup_notification("Adicional", "Adicional2 escolha inválida!!!")
        return main()


# Função equivalente ao nono estado do automato (q8)
# Neste estado, o usuário deve escolher o molho adicional do sanduíche
# Os molhos disponíveis são: Maionese, Ketchup, Mostarda
# Caso o usuário escolha um molho adicional inválido, uma mensagem de erro é exibida
# Caso o usuário escolha "Cancelar adicional", o estado de escolher bebida (q9) é chamado
# Como o o usuario apenas pode escolher entre os molhos disponíveis, para testar o estado de erro, basta tentar fechar a janela de seleção de molho adicional
def adicional_molho(pedido):
    if pedido.interacao == "Automatico":
        pedido.molho_adicional = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.molho_adicional = popup("Escolha o molho adicional do seu sanduíche:", ["Maionese", "Ketchup", "Mostarda", "Cancelar adicional"], True)
    
    if pedido.molho_adicional == "Cancelar adicional":
        return qual_bebida(pedido)
    
    elif not pedido.molho_adicional in ["Maionese", "Ketchup", "Mostarda"]:
        popup_notification("Molho Adicional", "Molho adicional inválido!!!")
        return main()
    
    else :
        return qual_bebida(pedido)


# Função equivalente ao décimo estado do automato (q9)
# Neste estado, o usuário deve escolher a bebida que acompanha sanduíche
# As bebidas disponíveis são: Refrigerante, Suco, Água
# Caso o usuário escolha uma bebida inválida, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado de escolher molho adicional (q8) é chamado
# Como o o usuario apenas pode escolher entre as bebidas disponíveis, para testar o estado de erro, basta tentar fechar a janela de seleção de bebida
def qual_bebida(pedido):
    if pedido.interacao == "Automatico":
        pedido.bebida = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.bebida = popup("Escolha a bebida do seu sanduíche:", ["Refrigerante", "Suco", "Agua", "Voltar"], True)
    
    if pedido.bebida == "Voltar":
        return qual_molho(pedido)
    
    elif not pedido.bebida in ["Refrigerante", "Suco", "Agua"]:
        popup_notification("Bebida", "Bebida inválida!!!")
        return main()
    
    else:
        return confirmacao_pedido(pedido)


# Função equivalente ao décimo primeiro estado do automato (q10)
# Neste estado, o usuário deve escolher se deseja adicionar mais algum lanche ao seu pedido
# As opções disponíveis são: Sim, Não, Voltar a editar o pedido
# Caso escolha "Sim", o estado de escolher recheio (q2) é chamado
# Caso escolha "Não", o estado de escolher forma de entrega (q11) é chamado
# Caso escolha "Voltar a editar o pedido", o estado de escolher molho (q7) é chamado
# Caso o usuário escolha uma opção inválida, uma mensagem de erro é exibida
# Como o o usuario apenas pode escolher entre as opções disponíveis, para testar o estado de erro, basta tentar fechar a janela de seleção de confirmação de pedido
def confirmacao_pedido(pedido):
    if pedido.interacao == "Automatico":
        novo_pedido = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        novo_pedido = popup("Deseja adicionar mais algum lanche ao seu pedido?", ["Sim", "Nao", "Voltar a editar o pedido"], True)
    
    if novo_pedido == "Voltar a editar o pedido":
        return qual_bebida(pedido)
    
    elif novo_pedido == "Sim":
        return qual_recheio(pedido)    
    
    elif novo_pedido == "Nao":
        return entrega(pedido)
    
    else:
        popup_notification("Novo Pedido", "Escolha de confirmação de pedido inválida!!!")
        return main()


# Função equivalente ao décimo segundo estado do automato (q11)
# Neste estado, o usuário deve escolher a forma de entrega do seu pedido
# As formas de entrega disponíveis são: Retirar no balcão, Entrega
# Caso o usuário escolha uma forma de entrega inválida, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado de escolher forma de entrega (q10) é chamado
# Como o o usuario apenas pode escolher entre as formas de entrega disponíveis, para testar o estado de erro, basta tentar fechar a janela de seleção de forma de entrega
def entrega(pedido):
    if pedido.interacao == "Automatico":
        pedido.forma_entrega = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        pedido.forma_entrega = popup("Escolha a forma de entrega do seu pedido:", ["Retirar no balcao", "Entrega", "Voltar a editar o pedido"], True)
    
    if pedido.forma_entrega == "Voltar a editar o pedido":
        return confirmacao_pedido(pedido)    
    
    if not pedido.forma_entrega in ["Retirar no balcao", "Entrega"]:
        popup_notification("Forma de Entrega", "Forma de entrega inválida!!!")
        return main()
    
    else:
        clear()
        return pagamento(pedido)


# Função equivalente ao décimo terceiro estado do automato (q12)
# Neste estado, o usuário deve digitar o número do cartão de crédito
# Caso o usuário digite um número de cartão inválido, uma mensagem de erro é exibida 
# Ao clicar em OK na mensagem de erro, o usuario é redirecionado para inserir o número do cartão novamente (q12)
# Caso o usuário digite um número de cartão válido, o estado de digitar senha do cartão (q13) é chamado
# Como o o usuario apenas pode digitar um número de cartão válido, para testar o estado de erro, basta digitar um número de cartão com mais ou menos de 16 dígitos
def pagamento(pedido):
    if pedido.interacao == "Automatico":
        if pedido.indice < len(pedido.entradas_arquivo):
            pedido.cartao = pedido.entradas_arquivo[pedido.indice]
            pedido.indice = pedido.indice + 1
        
        else :
            if not pedido.cartao_error:
                pedido.cartao_error = True
                popup_notification("Cartão", "Número de cartão inválido!!!")
                return pagamento(pedido)
            
            else:
                return main()
    
    else:
        pedido.cartao = popup_text('Cartão de Crédito' ,"Digite o número do cartão: ")
    
    if len(pedido.cartao) != 16:
        if pedido.interacao == "Automatico":
            if not pedido.cartao_error:
                pedido.cartao_error = True
                popup_notification("Cartão", "Número de cartão inválido!!!")
                return pagamento(pedido)
            
            else:
                return pagamento(pedido)

        else:
            popup_notification("Cartão", "Quantidade de dígitos inválida!!!")
            return pagamento(pedido)
    
    else:
        pedido.senha_cartao = pedido.cartao[-4:]
        return senha_cartao(pedido)


# Função equivalente aos estados (q13, q14, q15 e q16) do automato 
# Neste estado, o usuário deve digitar a senha do cartão de crédito
# Caso o usuário digite uma senha inválida, uma mensagem de erro é exibida
# Como o o usuario apenas pode digitar uma senha válida, para testar o estado de erro, basta digitar uma senha diferente dos ultimos 4 dígitos do cartão
# Ao clicar em OK na mensagem de erro, o usuario é redirecionado para inserir a senha do cartão novamente (q14)
# Caso o usuário digite uma senha válida, o estado de imprimir sucesso no pedido (q17) é chamado
# Caso o usuário digite uma senha inválida 4 vezes, será exibida uma mensagem de erro e o usuário será redirecionado para o estado de escolher interação (q1)
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
                popup_notification("Senha do Cartão", "Senha do cartão inválida!!!")
                senha = popup_text('Senha do Cartão' ,"Digite a senha do cartão: ")
            
            if senha == pedido.senha_cartao:
                return imprime(pedido)
            tentativas += 1
        popup_notification("Senha do Cartão", "Numero de tentativas esgotadas!!!")
        return main()


# Função equivalente ao décimo sétimo estado do automato (q17)
# Neste estado, é exibida uma mensagem de sucesso no pedido e o usuário é redirecionado para o estado de escolher interação (q1)
def imprime(pedido):
    popup_notification("Pedido", "Pedido realizado com sucesso!!!")
    
    return main()


# Função utilizada para limpar o terminal (console) utilizada principalmente no modo texto da aplicação
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função de inicialização da aplicação e criação do objeto pedido
def main():
    meupedido = Pedido()
    escolher_interacao(meupedido)

if __name__ == "__main__":
    main()
