from itemDire.itemCardapio import Item_Cardapio

class Bebida(Item_Cardapio):
    def __init__(self, tipo_recipiente, quantidade_ml, tem_refil, nome, preco, disponivel):
        self.tipo_recipiente = tipo_recipiente
        self.quantidade_ml = quantidade_ml
        self.tem_refil = tem_refil
        super().__init__(nome, preco, disponivel)

    def get_tipo_recipiente(self):
        return self.tipo_recipiente

    def set_tipo_recipiente(self, value):
        self.tipo_recipiente = value

    def get_quantidade_ml(self):
        return self.quantidade_ml

    def set_quantidade_ml(self, value):
        self.quantidade_ml = value

    def get_tem_refil(self):
        return self.tem_refil

    def set_tem_refil(self, value):
        self.tem_refil = value
