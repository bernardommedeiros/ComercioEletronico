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
