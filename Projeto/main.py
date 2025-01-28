from models.usuario import Usuario
from models.produto import Produto
from models.pedido import Pedido
from models.categoria import Categoria
from models.itemCarrinho import ItemCarrinho
from salvar import salvar_dados, carregar_dados, autenticar
from views.clientes import gerenciar_clientes
from views.categorias import gerenciar_categorias
from views.vendas import visualizar_pedidos
from views.vendaitem import gerenciar_produtos

def criar_conta(usuarios):
    nome = input("Informe seu nome: ")
    email = input("Informe seu e-mail: ")
    senha = input("Informe sua senha: ")
    usuario = Usuario(len(usuarios) + 1, nome, email, senha, "cliente")
    usuarios.append(usuario)
    salvar_dados('usuarios.json', usuarios)
    print(f"Conta criada com sucesso! Bem-vindo, {nome}.")

def admin_dashboard():
    while True:
        print("\nMenu Admin:")
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Categorias")
        print("3 - Visualizar Pedidos")
        print("4 - Gerenciar Clientes")
        print("5 - Sair")
        escolha_admin = input("Escolha uma opção: ")

        if escolha_admin == "1":
            gerenciar_produtos()
        elif escolha_admin == "2":
            gerenciar_categorias()
        elif escolha_admin == "3":
            visualizar_pedidos()
        elif escolha_admin == "4":
            gerenciar_clientes()
        elif escolha_admin == "5":
            break
        else:
            print("Opção inválida.")

def cliente_dashboard(usuario):
    produtos = carregar_dados('produtos.json', Produto)
    pedidos = carregar_dados('pedidos.json', Pedido)
    carrinho = []
    while True:
        print("\nMenu Cliente:")
        print("1 - Listar Produtos")
        print("2 - Adicionar ao Carrinho")
        print("3 - Visualizar Carrinho")
        print("4 - Finalizar Compra")
        print("5 - Visualizar Meus Pedidos")
        print("6 - Sair")
        escolha_cliente = input("Escolha uma opção: ")

        if escolha_cliente == "1":
            for produto in produtos:
                print(produto)
        elif escolha_cliente == "2":
            produto_id = int(input("ID do produto: "))
            produto = next((p for p in produtos if p.id == produto_id), None)
            if produto:
                quantidade = int(input("Quantidade: "))
                item_carrinho = ItemCarrinho(produto, quantidade)
                carrinho.append(item_carrinho)
                print(f"{quantidade}x {produto.nome} foi adicionado ao seu carrinho.")
            else:
                print("Produto não encontrado.")
        elif escolha_cliente == "3":
            for item in carrinho:
                print(item)
        elif escolha_cliente == "4":
            total = sum(item.produto.preco * item.quantidade for item in carrinho)
            pedidos.append(Pedido(usuario, carrinho, total))
            salvar_dados('pedidos.json', pedidos)
            carrinho.clear()
            print(f"Compra finalizada! Total: R${total}")
        elif escolha_cliente == "5":
            for pedido in pedidos:
                if pedido.usuario.id == usuario.id:
                    print(pedido)
        elif escolha_cliente == "6":
            break
        else:
            print("Opção inválida.")

def main():
    usuarios = carregar_dados('usuarios.json', Usuario)
    produtos = carregar_dados('produtos.json', Produto)
    pedidos = carregar_dados('pedidos.json', Pedido)
    categorias = carregar_dados('categorias.json', Categoria)

    # Adiciona um administrador padrão se não existir
    if not any(u.email == 'admin' for u in usuarios):
        admin = Usuario(len(usuarios) + 1, 'Admin', 'admin', 'admin', 'admin')
        usuarios.append(admin)
        salvar_dados('usuarios.json', usuarios)

    # Adiciona produtos padrão se não existirem
    if not produtos:
        categoria_roupas = Categoria(1, "Roupas")
        produtos = [
            Produto(1, "Camisa", 50.0, categoria_roupas),
            Produto(2, "Tênis", 150.0, categoria_roupas),
            Produto(3, "Short", 30.0, categoria_roupas),
            Produto(4, "Meia", 10.0, categoria_roupas),
            Produto(5, "Boné", 25.0, categoria_roupas)
        ]
        salvar_dados('produtos.json', produtos)
        categorias.append(categoria_roupas)
        salvar_dados('categorias.json', categorias)

    print("Bem-vindo ao Sistema de Comércio Eletrônico!")

    while True:
        print("\nMenu:")
        print("1 - Criar Conta")
        print("2 - Entrar")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_conta(usuarios)
        elif escolha == "2":
            email = input("Informe seu e-mail: ")
            senha = input("Informe sua senha: ")
            usuario = autenticar(usuarios, email, senha)

            if usuario:
                print(f"Bem-vindo, {usuario.nome}!")
                if usuario.perfil == "admin":
                    admin_dashboard()
                else:
                    cliente_dashboard(usuario)
            else:
                print("Usuário ou senha inválidos.")
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
