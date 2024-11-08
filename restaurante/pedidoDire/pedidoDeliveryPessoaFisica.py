from pedidoDire.pedido import Pedido

class PedidoDeliveryPessoaFisica(Pedido):
    def __init__(self, nomeCliente, tempoPrevistoSaida, enderecoEntrega, valorFrete, horaSaidaEntrega, id, dataHorarioInicio, itensPedido, idAtendente, total, dataHoraFechamento, valorAPagar, formaPagamento):
        super().__init__(id, dataHorarioInicio, itensPedido, idAtendente, total, dataHoraFechamento, valorAPagar, formaPagamento)
        self.nomeCliente = nomeCliente
        self.tempoPrevistoSaida = tempoPrevistoSaida
        self.enderecoEntrega = enderecoEntrega
        self.valorFrete = valorAPagar
        self.horaSaidaEntrega = horaSaidaEntrega

    def get_nomeCliente(self):
        return self.nomeCliente

    def get_tempoPrevistoSaida(self):
        return self.tempoPrevistoSaida
    
    def get_enderecoEntrega(self):
        return self.enderecoEntrega

    def get_valorFrete(self):
        return self.valorFrete

    def get_horaSaidaEntrega(self):
        return self.horaSaidaEntrega