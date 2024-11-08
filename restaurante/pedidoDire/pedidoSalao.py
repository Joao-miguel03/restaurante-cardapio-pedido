from pedidoDire.pedido import Pedido

class PedidoSalao(Pedido):
    def __init__(self, numeroMesa, id, dataHorarioInicio, itensPedido, idAtendente, total, dataHoraFechamento, valorAPagar, formaPagamento):
        super().__init__(id, dataHorarioInicio, itensPedido, idAtendente, total, dataHoraFechamento, valorAPagar, formaPagamento)
        self.numeroMesa = numeroMesa

    def get_numeroMesa(self):
        return self.numeroMesa

    def set_numeroMesa(self, value):
        self.numeroMesa = value