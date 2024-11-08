from itemDire.itemCardapio import Item_Cardapio

class Sobremesa(Item_Cardapio):
    def __init__(self, unidade_medida, descricao, todo_sobremesa, nome, preco, disponivel):
        super().__init__(nome, preco, disponivel)
        self.unidade_medida = unidade_medida
        self.descricao = descricao
        self.todo_sobremesa = todo_sobremesa

    def get_unidade_medida(self):
        return self.unidade_medida

    def set_unidade_medida(self, value):
        self.unidade_medida = value

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, value):
        self.descricao = value

    def get_todo_sobremesa(self):
        return self.todo_sobremesa

    def set_todo_sobremesa(self, value):
        self.todo_sobremesa = value
