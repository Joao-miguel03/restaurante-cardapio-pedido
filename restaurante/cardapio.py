class Cardapio:
    def __init__(self):
        self.lista_item = []
    
    def adicionar_item(self,item):
        self.lista_item.append(item)

    def remover_item(self, item):
        self.lista_item.remove(item)
    
    def imprimir_itens(self):
        for i in self.lista_item:
            resposta = "não"
            print(f"- - - - - - - - - - - - - - - - - - - - - -")
            try:
                print(f"- Nome: {i.get_nome()} (serve {i.get_quantasPessoasServe()} pessoas) -")
            except: 
                print(f"- Nome: {i.get_nome()} -")
            
            print(f"- Preço: {i.get_preco()} -")
            if i.get_disponivel():
                resposta = "sim" 
                
            print(f"- Disponével: {resposta} -")
            try: 
                print(f"- Descrição: {i.get_descricao()} -")
                print(f"- - - - - - - - - - - - - - - - - - - - - -")
            except:
                print(f"- - - - - - - - - - - - - - - - - - - - - -")
                
