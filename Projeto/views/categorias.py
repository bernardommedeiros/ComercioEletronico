# views/categorias.py

from models import Categoria
from salvar import salvar_dados, carregar_dados

def gerenciar_categorias():
    categorias = carregar_dados('categorias.json', Categoria)
    while True:
        print("\nGerenciamento de Categorias:")
        print("1 - Adicionar Categoria")
        print("2 - Listar Categorias")
        print("3 - Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome da Categoria: ")
            categoria = Categoria(len(categorias) + 1, nome)
            categorias.append(categoria)
            salvar_dados('categorias.json', categorias)
            print("Categoria adicionada com sucesso!")
        elif escolha == "2":
            for categoria in categorias:
                print(categoria)
        elif escolha == "3":
            break
        else:
            print("Opção inválida.")
