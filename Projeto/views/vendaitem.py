# views/vendaitem.py

from models import Produto, Pedido, Categoria
from salvar import salvar_dados, carregar_dados

def gerenciar_produtos():
    produtos = carregar_dados('produtos.json', Produto)
    categorias = carregar_dados('categorias.json', Categoria)
    while True:
        print("\nGerenciamento de Produtos:")
        print("1 - Adicionar Produto")
        print("2 - Reajustar Preço de Produto")
        print("3 - Listar Produtos")
        print("4 - Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Produto: ")
            preco = float(input("Preço do Produto: "))
            categoria_id = int(input("ID da Categoria: "))
            categoria = next((c for c in categorias if c.id == categoria_id), None)
            if categoria:
                produto = Produto(len(produtos) + 1, nome, preco, categoria)
                produtos.append(produto)
                salvar_dados('produtos.json', produtos)
                print("Produto adicionado com sucesso!")
            else:
                print("Categoria não encontrada.")
        elif escolha == "2":
            produto_id = int(input("ID do Produto: "))
            produto = next((p for p in produtos if p.id == produto_id), None)
            if produto:
                novo_preco = float(input(f"Novo preço para {produto.nome}: "))
                produto.preco = novo_preco
                salvar_dados('produtos.json', produtos)
                print("Preço reajustado com sucesso!")
            else:
                print("Produto não encontrado.")
        elif escolha == "3":
            for produto in produtos:
                print(f"{produto.id} - {produto}")
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")
