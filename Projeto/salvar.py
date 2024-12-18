import json
from models import Usuario, Produto, Pedido, Categoria


def salvar_dados(filename, dados):
    with open(filename, 'w') as f:
        json.dump([obj.to_dict() for obj in dados], f, indent=4)

def carregar_dados(filename, cls):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [cls.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Autenticação
def autenticar(usuarios, email, senha):
    return next((u for u in usuarios if u.email == email and u.senha == senha), None)
