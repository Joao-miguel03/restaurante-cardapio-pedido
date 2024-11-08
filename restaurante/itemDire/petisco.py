from itemDire.itemCardapio import Item_Cardapio

class Petisco(Item_Cardapio):
    def __init__(self,unidade_medida, descricao, foto_petisco, nome, preco, disponivel):
        super().__init__(nome, preco, disponivel)
        self.unidade_medida = unidade_medida
        self.descricao = descricao
        self.foto_petisco = foto_petisco

    def get_unidade_medida(self):
        return self.unidade_medida

    def set_unidade_medida(self, value):
        self.unidade_medida = value

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, value):
        self.descricao = value

    def get_foto_petisco(self):
        return self.foto_petisco

    def set_foto_petisco(self, value):
        self.foto_petisco = value


