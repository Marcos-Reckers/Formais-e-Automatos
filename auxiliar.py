import os
def imprime(pedido):
    print("==========================================")
    print("Obrigado por utilizar o sistema de pedidos")
    print("==========================================\n")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
