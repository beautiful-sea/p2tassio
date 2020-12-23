import json
from application.model.entity.Produto import Produto

with open ('application\\products.json') as product_file:
        product_list = json.load(product_file)

class ProdutoDAO:
    def __init__(self):
        self._produtos = []

        for produto in product_list:
             self._produtos.append(Produto(produto['id'], produto['image'], produto['name'], produto['description'], produto['oldPrice'], produto['price'], produto['installments']['count'], produto['installments']['value']))

    def get_produtos(self):
        return self._produtos