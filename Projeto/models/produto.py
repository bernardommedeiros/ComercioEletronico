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
