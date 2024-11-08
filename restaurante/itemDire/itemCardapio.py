class Item_Cardapio:
    def __init__(self, nome, preco, disponivel):
        self.nome = nome
        self.preco = preco
        self.disponivel = disponivel

    def get_nome(self):
        return self.nome

    def set_nome(self, value):
        self.nome = value

    def get_preco(self):
        return self.preco

    def set_preco(self, value):
        self.preco = value

    def get_disponivel(self):
        return self.disponivel

    def set_disponivel(self, value):
        self.disponivel = value

    