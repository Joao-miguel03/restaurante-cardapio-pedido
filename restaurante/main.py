#import das classes de pedido
from pedidoDire.pedidoSalao import PedidoSalao
from pedidoDire.pedidoDeliveryPessoaFisica import PedidoDeliveryPessoaFisica
from pedidoDire.pedidoDeliveryPessoaJuridica import PedidoDeliveryPessoaJuridica
#import das classes de item
from itemDire.bebida import Bebida
from itemDire.pratoPrincipal import PratoPrincipal
from itemDire.petisco import Petisco
from itemDire.sobremesa import Sobremesa
from cardapio import Cardapio

cardapioRestaurante = Cardapio()
prato1 = PratoPrincipal(10, 1, "um delicioso prato gostoso", "foto.png", "torta de frango", 30, False)

cardapioRestaurante.adicionar_item(prato1)

cardapioRestaurante.imprimir_itens()
