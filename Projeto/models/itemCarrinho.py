class ItemCarrinho:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def to_dict(self):
        data = self.__dict__.copy()
        data['produto'] = self.produto.to_dict()
        return data

    @classmethod
    def from_dict(cls, data):
        data['produto'] = Produto.from_dict(data['produto'])
        return cls(**data)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} - R${self.produto.preco} cada"
