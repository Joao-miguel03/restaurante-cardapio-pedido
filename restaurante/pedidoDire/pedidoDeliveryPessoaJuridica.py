from pedidoDire.pedido import Pedido

class PedidoDeliveryPessoaJuridica(Pedido):
    def __init__(self, nomeEmpresa, CNPJCliente, nomeResponsavel, tempoPrevistoSaida, enderecoEntrega, valorFrete, horaSaidaEntrega, id, dataHorarioInicio, itensPedido, idAtendente, total, dataHoraFechamento, valorAPagar, formaPagamento):
        super().__init__(id, dataHorarioInicio, itensPedido, idAtendente, total, dataHoraFechamento, valorAPagar, formaPagamento)
        self.nomeEmpresa = nomeEmpresa
        self.CNPJCliente = CNPJCliente
        self.nomeResponsavel = nomeResponsavel
        self.tempoPrevistoSaida = tempoPrevistoSaida
        self.enderecoEntrega = enderecoEntrega
        self.valorFrete = valorFrete
        self.horaSaidaEntrega = horaSaidaEntrega
    
    def get_nomeEmpresa(self):
        return self.nomeEmpresa

    def get_CNPJCliente(self):
        return self.CNPJCliente
    
    def getEnderecoEntrega(self):
        return self.enderecoEntrega
    
    def getValorFrete(self):
        return self.valorFrete
    
    def getSaidaEntrega(self):
        return self.horaSaidaEntrega