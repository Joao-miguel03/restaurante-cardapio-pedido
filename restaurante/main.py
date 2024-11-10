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
prato2 = PratoPrincipal(10, 2, "um delicioso prato exótico", "foto.png", "lula a pimenta malagueta", 45, False)

sobremesa1 = Sobremesa(4, "Equilíbrio entre o útil e desagradável", 4,"Pudim de pitaya", 25, False)
sobremesa2 = Sobremesa(4, "Doce na medida certa!", 4, "cheesecake de morango", 25, False)

bebida1 = Bebida("garrafa de vidro", 1,False, "coca cola", 10, False)
bebida2 = Bebida("copo",1.5, False, "vinho", 25, False)

petisco1 = Petisco(10, "melhor petisco", "foto.png", "Muffin de Presunto com Queijo Muçarela", 30, False)
petisco2 = Petisco(10, "tão bom que poderia ser prato principal", "foto.png", "carne louca com cerveja", 50, False)


cardapioRestaurante.adicionar_item(sobremesa2)

cardapioRestaurante.imprimir_itens()
