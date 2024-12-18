from models import Pedido
from salvar import salvar_dados, carregar_dados

def visualizar_pedidos():
    pedidos = carregar_dados('pedidos.json', Pedido)
    print("\nPedidos:")
    for pedido in pedidos:
        print(pedido)
