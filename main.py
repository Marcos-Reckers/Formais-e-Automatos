from lib.pedido import *
from lib.estados import *

def main():
    
    meupedido = Pedido()
    meupedido.senha_cartao = "1234"

    clear()
    estado_inicial(meupedido)

if __name__ == "__main__":
    main()
