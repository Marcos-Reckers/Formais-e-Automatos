import os
def imprime(pedido):
    print("==========================================")
    print("Obrigado por utilizar o sistema de pedidos")
    print("==========================================\n")
    print("Seu pedido é:\n")
    print("Recheio: ", pedido.recheio)
    if not pedido.molho_adicional == []:
        print("Recheio adicional: ", pedido.recheio_adicional)
    print("Salada: ", pedido.salada)
    print("Molho: ", pedido.molho)
    if not pedido.molho_adicional == []:
        print("Molho adicional: ", pedido.molho_adicional)
    print("Bebida: ", pedido.bebida)
    print("Forma de entrega: ", pedido.forma_entrega)
    print("==========================================\n")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
