class Usuario:
    def __init__(self, id, nome, email, senha, perfil):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"{self.nome} ({self.email}) - {self.perfil}"

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return self.nome

class Produto:
    def __init__(self, id, nome, preco, categoria):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def to_dict(self):
        data = self.__dict__.copy()
        data['categoria'] = self.categoria.to_dict()
        return data

    @classmethod
    def from_dict(cls, data):
        data['categoria'] = Categoria.from_dict(data['categoria'])
        return cls(**data)

    def __str__(self):
        return f"{self.id}. {self.nome} - R${self.preco} - {self.categoria.nome}"

class Pedido:
    def __init__(self, usuario, itens, total):
        self.usuario = usuario
        self.itens = itens
        self.total = total

    def to_dict(self):
        data = self.__dict__.copy()
        data['usuario'] = self.usuario.to_dict()
        data['itens'] = [item.to_dict() for item in self.itens]
        return data

    @classmethod
    def from_dict(cls, data):
        data['usuario'] = Usuario.from_dict(data['usuario'])
        data['itens'] = [Produto.from_dict(item) for item in data['itens']]
        return cls(**data)

    def __str__(self):
        return f"Pedido de {self.usuario.nome}: R${self.total}"
