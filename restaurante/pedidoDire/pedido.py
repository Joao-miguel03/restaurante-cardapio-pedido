class Pedido:
    def __init__(self, id, dataHorarioInicio, itensPedido, idAtendente, total, dataHoraFechamento, valorAPagar, formaPagamento):
        self.id = id
        self.dataHorarioInicio = dataHorarioInicio
        self.itensPedido = itensPedido
        self.idAtendente = idAtendente
        self.total = total
        self.dataHoraFechamento = dataHoraFechamento
        self.valorAPagar = valorAPagar
        self.formaPagamento = formaPagamento

    def get_id(self):
        return self.id
    
    def get_dataHorarioInicio(self):
        return self.dataHorarioInicio

    def get_dataHoraFechamento(self):
        return self.dataHoraFechamento

    def get_itensPedido(self):
        return self.itensPedido

    def get_total(self):
        return self.total

    def set_total(self, value):
        self.total = value

    def fecharPedido(self, value):
        self.dataHoraFechamento = value

    def get_valorAPagar(self):
        return self.valorAPagar
    
    def adicionarPedido(self, pedido):
        self.itensPedido.append(pedido)

        
