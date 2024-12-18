# views/clientes.py

from models import Usuario
from salvar import salvar_dados, carregar_dados

def gerenciar_clientes():
    usuarios = carregar_dados('usuarios.json', Usuario)
    while True:
        print("\nGerenciamento de Clientes:")
        print("1 - Listar Clientes")
        print("2 - Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            for usuario in usuarios:
                print(usuario)
        elif escolha == "2":
            break
        else:
            print("Opção inválida.")
