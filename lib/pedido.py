from dataclasses import dataclass, field

@dataclass
class Pedido:
    usuario:str = None
    senha:str = None
    recheio:str = None
    adicional1:str = None
    recheio_adicional:str = None
    salada:str = None
    molho:str = None
    adicional2:str = None
    molho_adicional:str = None
    bebida:str = None
    forma_entrega:str = None
    cartao:str = None
    senha_cartao:str = None
    interacao:str = None
    entradas_arquivo:list = field(default_factory=list)
    indice:int = 0
