import os
from lib.pedido import Pedido


# Função para escolher o tipo de interação:
# Manual: O usuário digita os dados
# Automatico: O usuário escolhe um arquivo de entrada
def escolher_interacao(pedido):
    print("Escolha o modo de interacao:\n")
    print("Real")
    print("Automatico")
    pedido.interacao = input("\nDigite o modo de interacao: ")
    
    if pedido.interacao == "Automatico":
        nome_arquivo = input("Digite o nome do arquivo: ")
        if nome_arquivo != None and ".txt" in nome_arquivo and FileNotFoundError():
            with open(nome_arquivo, "r") as arquivo:
                for line in arquivo.readlines():
                    pedido.entradas_arquivo.append(line.strip())
            clear()
            return estado_inicial(pedido)
        else:
            print("Arquivo invalido!")
    
    elif pedido.interacao == "Real":
        clear()
        return estado_inicial(pedido)
    
    else:
        clear()
        print("Interacao invalida\n\n")
        return escolher_interacao(pedido)
    
    
# Função equivalente ao estado inicial do automato (q0)
# Neste estado, o usuário deve digitar seu nome de usuário
# Qualquer conjunto de caracteres é aceito como nome de usuário exceto entrada vazia
# Caso o usuário digite um nome de usuário inválido, uma mensagem de erro é exibida
# Para testar o estado de erro, basta digitar um nome de usuário vazio
def estado_inicial(pedido):
    if pedido.interacao == "Automatico":
        pedido.usuario = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Bem vindo ao sistema de pedidos")
        pedido.usuario = input("Digite seu nome de usuário: ")

    if not pedido.usuario:
        print("\nNome de usuario invalido!\n")
        return escolher_interacao(pedido)
    else:
        return senha_inicial(pedido)


# Função equivalente ao segundo estado do automato (q1)
# Neste estado, o usuário deve digitar sua senha
# Qualquer conjunto de caracteres é aceito como senha exceto entrada
# Caso o usuário digite uma senha inválida, uma mensagem de erro é exibida
# Para testar o estado de erro, basta digitar uma senha vazia
def senha_inicial(pedido):
    if pedido.interacao == "Automatico":
        pedido.senha = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    else:
        pedido.senha = input("Digite sua senha: ")
        clear()
        
    if not pedido.senha:
        print("\nSenha invalida!\n")
        return escolher_interacao(pedido)
    else:
        return qual_recheio(pedido)

# Função equivalente ao terceiro estado do automato (q2)
# Neste estado, o usuário deve escolher o recheio do sanduíche
# Os recheios disponíveis são: Frango, Carne, Vegetariano
# O usuário deve digitar o recheio exatamente como proposto pelo sistema
# Caso o usuário digite um recheio inválido, uma mensagem de erro é exibida
# Caso o usuário digite voltar, o estado inicial é chamado novamente
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
    
# Função equivalente ao quarto estado do automato (q3)
# Neste estado, o usuário deve escolher se deseja adicionar um recheio adicional
# As opções disponíveis são: Sim, Não
# O usuário deve digitar a resposta exatamente como proposto pelo sistema
# Caso o usuário escolha sim, o estado de adicionar recheio adicional (q4) é chamado
# Caso o usuário escolha não, o estado de escolher salada (q5) é chamado
# Caso o usuário escolha uma opção inválida, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado de escolher recheio (q2) é chamado
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

# Função equivalente ao quinto estado do automato (q4)
# Neste estado, o usuário deve escolher o recheio adicional do sanduíche
# Os recheios disponíveis são: Frango, Carne, Vegetariano
# O usuário deve digitar o recheio exatamente como proposto pelo sistema
# Caso o usuário escolha um recheio inválido, uma mensagem de erro é exibida
# Caso o usuário escolha "Cancelar adicional", o estado de escolher salada (q5) é chamado
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

# Função equivalente ao sexto estado do automato (q5)
# Neste estado, o usuário deve escolher a salada do sanduíche
# As saladas disponíveis são: Alface, Tomate, Cenoura, Sem salada
# O usuário deve digitar a salada exatamente como proposto pelo sistema
# Caso o usuário escolha uma salada inválida, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado de escolher recheio (q2) é chamado
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

# Função equivalente ao sétimo estado do automato (q6)
# Neste estado, o usuário deve escolher o molho do sanduíche
# Os molhos disponíveis são: Maionese, Ketchup, Mostarda, Sem molho
# O usuário deve digitar o molho exatamente como proposto pelo sistema
# Caso o usuário escolha um molho inválido, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado de escolher salada (q5) é chamado
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
    
# Função equivalente ao oitavo estado do automato (q7)
# Neste estado, o usuário deve escolher se deseja adicionar um molho adicional ao sanduíche
# As opções disponíveis são: Sim, Não
# O usuário deve digitar a resposta exatamente como proposto pelo sistema
# Caso escolha "Sim", o estado de escolher molho adicional (q8) é chamado
# Caso escolha "Não", o estado de escolher bebida (q9) é chamado
# Caso o usuário escolha uma opção inválida, uma mensagem de erro é exibida
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

# Função equivalente ao nono estado do automato (q8)
# Neste estado, o usuário deve escolher o molho adicional do sanduíche
# Os molhos disponíveis são: Maionese, Ketchup, Mostarda
# O usuário deve digitar o molho exatamente como proposto pelo sistema
# Caso o usuário escolha um molho adicional inválido, uma mensagem de erro é exibida
# Caso o usuário escolha "Cancelar adicional", o estado de escolher bebida (q9) é chamado
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

# Função equivalente ao décimo estado do automato (q9)
# Neste estado, o usuário deve escolher a bebida que acompanha sanduíche
# As bebidas disponíveis são: Refrigerante, Suco, Agua
# O usuário deve digitar a bebida exatamente como proposto pelo sistema
# Caso o usuário escolha uma bebida inválida, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado de escolher molho adicional (q8) é chamado
def qual_bebida(pedido):
    if pedido.interacao == "Automatico":
        pedido.bebida = pedido.entradas_arquivo[pedido.indice]
        pedido.indice = pedido.indice + 1
    
    else:
        print("Escolha a bebida do seu sanduíche:\n")
        print("Refrigerante")
        print("Suco")
        print("Agua")
        print("\nVoltar")
        pedido.bebida = input("Digite a bebida: ")
    
    if pedido.bebida == "Voltar":
        clear()
        return qual_molho(pedido)
    
    elif not pedido.bebida in ["Refrigerante", "Suco", "Agua"]:
        clear()
        print("Bebida inválida")
        return escolher_interacao(pedido)
    
    else:
        clear()
        return confirmacao_pedido(pedido)

# Função equivalente ao décimo primeiro estado do automato (q10)
# Neste estado, o usuário deve escolher se deseja adicionar mais algum lanche ao seu pedido
# As opções disponíveis são: Sim, Não, Voltar a editar o pedido
# O usuário deve digitarsua opção exatamente como proposto pelo sistema
# Caso escolha "Sim", o estado de escolher recheio (q2) é chamado
# Caso escolha "Não", o estado de escolher forma de entrega (q11) é chamado
# Caso escolha "Voltar a editar o pedido", o estado de escolher molho (q7) é chamado
# Caso o usuário escolha uma opção inválida, uma mensagem de erro é exibida
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
        print("Opção de adição de pedido inválida\n\n")
        return escolher_interacao(pedido)


# Função equivalente ao décimo segundo estado do automato (q11)
# Neste estado, o usuário deve escolher a forma de entrega do seu pedido
# As formas de entrega disponíveis são: Retirar no balcão, Entrega
# O usuário deve digitar sua opção exatamente como proposto pelo sistema
# Caso o usuário escolha uma forma de entrega inválida, uma mensagem de erro é exibida
# Caso o usuário escolha voltar, o estado de escolher forma de entrega (q10) é chamado
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
    
    if not pedido.forma_entrega in ["Retirar no balcao", "Entrega"]:
        clear()
        print("Opção de entrega inválida\n\n")
        return escolher_interacao(pedido)
    
    else:
        clear()
        return pagamento(pedido)

# Função equivalente ao décimo terceiro estado do automato (q12)
# Neste estado, o usuário deve digitar o número do cartão de crédito
# Caso o usuário digite um número de cartão inválido, uma mensagem de erro é exibida e o usuário continua em q12
# Caso o usuário digite um número de cartão válido, o estado de digitar senha do cartão (q13) é chamado
def pagamento(pedido):
    if pedido.interacao == "Automatico":
        if pedido.indice < len(pedido.entradas_arquivo):
            pedido.cartao = pedido.entradas_arquivo[pedido.indice]
            pedido.indice = pedido.indice + 1
        
        else :
            print("Número de cartão inválido\n\n")
            return escolher_interacao(pedido)
    
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


# Função equivalente aos estados (q13, q14, q15 e q16) do automato 
# Neste estado, o usuário deve digitar a senha do cartão de crédito
# Caso o usuário digite uma senha inválida, uma mensagem de erro é exibida
# Como o o usuario apenas pode digitar uma senha válida, para testar o estado de erro, basta digitar uma senha diferente dos ultimos 4 dígitos do cartão
# Apos a mensagem de erro, o usuario é redirecionado para o proximo estado de insercao de senha do cartao (q13->q14->q15->q16)
# Caso o usuário digite uma senha válida, o estado de imprimir sucesso no pedido (q17) é chamado
# Caso o usuário digite uma senha inválida 4 vezes, será exibida uma mensagem de erro e o usuário será redirecionado para o estado de escolher interação (q1)
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
        while (senha != pedido.senha_cartao and tentativas < 4):
            if pedido.interacao == "Automatico":
                if pedido.indice < len(pedido.entradas_arquivo):
                    pedido.cartao = pedido.entradas_arquivo[pedido.indice]
                    pedido.indice = pedido.indice + 1
            
            else:
                print("Senha inválida tente novamente\n")
                senha = input("Digite a senha do cartão: ")

            if senha == pedido.senha_cartao:
                return imprime(pedido)
            tentativas += 1
        clear()
        print("Número de tentativas de senha excedido\n\n")
        return escolher_interacao(pedido)

# Função equivalente ao décimo sétimo estado do automato (q17)
# Neste estado, é exibida uma mensagem de sucesso no pedido e o usuário é redirecionado para o estado de escolher interação (q1)
def imprime(pedido):
    print("=======================================================")
    print("=========== Pedido realizado com sucesso!! ============")
    print("====== Obrigado por utilizar o sistema de pedidos======")
    print("=======================================================\n")
    
    return main()
# Limpar o terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função de inicialização da aplicação e criação do objeto pedido
def main():
    #clear()
    meupedido = Pedido()
    escolher_interacao(meupedido)

if __name__ == "__main__":
    main()
