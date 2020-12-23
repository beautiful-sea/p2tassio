import json
from application.model.entity.Produto import Produto

class ProdutoDAO:
    def __init__(self):
        with open ('application\\products.json') as product_file: # BUSCANDO LISTA DE PRODUTOS JSON NO ARQUIVO E ATRIBUINDO A VARIAVEL
            product_list = json.load(product_file)
        self._produtos = []

        for produto in product_list:# CONVERTENDO LISTA DE PRODUTOS EM JSON PARA LISTA DE PRODUTOS EM OBJETOS
             self._produtos.append(Produto(produto['id'], produto['image'], produto['name'], produto['description'], produto['oldPrice'], produto['price'], produto['installments']['count'], produto['installments']['value']))

    def get_produtos(self):
        return self._produtos