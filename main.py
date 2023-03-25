import pprint
from pedido import *
from estados import *
from auxiliar import *


def main():
    
    meupedido = Pedido()
    meupedido.senha = "1234"
    meupedido.numero_cartao = "123456789"
    meupedido.senha_cartao = "1234"


    clear()
    pprint.pprint(vars(meupedido))
    print('\n')
    estado_inicial(meupedido)



if __name__ == "__main__":
    main()
