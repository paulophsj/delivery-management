from enum import Enum

class OrderStatus(Enum):
    EM_ANDAMENTO: str = 'EM_ANDAMENTO'
    PREPARADO: str = 'PREPARADO'
    ENTREGUE: str = 'ENTREGUE'
