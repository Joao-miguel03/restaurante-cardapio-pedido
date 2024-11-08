from itemDire.itemCardapio import Item_Cardapio

class PratoPrincipal(Item_Cardapio):
    def __init__(self, quantasPessoasServe, unidade_medida, descricao, foto_prato, nome, preco, disponivel):
        super().__init__(nome, preco, disponivel)
        self.quantasPessoasServe = quantasPessoasServe
        self.unidade_medida = unidade_medida
        self.descricao = descricao
        self.foto_prato = foto_prato

    def get_quantasPessoasServe(self):
        return self.quantasPessoasServe

    def set_quantasPessoasServe(self, value):
        self.quantasPessoasServe = value

    def get_unidade_medida(self):
        return self.unidade_medida

    def set_unidade_medida(self, value):
        self.unidade_medida = value

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, value):
        self.descricao = value

    def get_foto_prato(self):
        return self.foto_prato

    def set_foto_prato(self, value):
        self.foto_prato = value


