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
        data['itens'] = [ItemCarrinho.from_dict(item) for item in data['itens']]
        return cls(**data)

    def __str__(self):
        return f"Pedido de {self.usuario.nome}: R${self.total}"
