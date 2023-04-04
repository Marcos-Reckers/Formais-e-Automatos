from dataclasses import dataclass, field

@dataclass
class Pedido:
    usuario: str = None             # Nome do usuário
    senha: str = None               # Senha do usuário
    recheio: str = None             # Recheio do sanduíche
    adicional1: str = None          # Sim ou Não para adicional de recheio no sanduíche
    recheio_adicional: str = None   # Recheio do adicional
    salada: str = None              # Salada do sanduíche
    molho: str = None               # Molho do sanduíche
    adicional2: str = None          # Sim ou Não para adicional de molho no sanduíche
    molho_adicional: str = None     # Molho do adicional
    bebida: str = None              # Bebida do sanduíche
    forma_entrega: str = None       # Forma de entrega do sanduíche
    cartao: str = None              # Número do cartão
    senha_cartao: str = None        # Senha do cartão
    interacao: str = None           # Interação com o usuário
    entradas_arquivo: list = field(default_factory=list) # Lista de entradas do arquivo
    indice: int = 0                 # Índice da lista de entradas do arquivo
    cartao_error: bool = False      # Flag para erro de cartão
