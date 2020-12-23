class Produto:
    def __init__ (self, id, imagem, nome, descricao, preco_anterior, preco, qtd_parcelas, valor_parcela):
        self._id = id
        self._imagem = imagem
        self._nome = nome
        self._descricao = descricao
        self._preco_anterior = preco_anterior
        self._preco = preco
        self._qtd_parcelas = qtd_parcelas
        self._valor_parcela = valor_parcela

    def get_id (self):
        return self._id

    def get_imagem (self):
        return self._imagem
    
    def get_nome (self):
        return self._nome

    def get_descricao (self):
        return self._descricao

    def get_preco_anterior (self):
        return self._preco_anterior
    
    def get_preco (self):
        return self._preco
    
    def get_qtd_parcelas (self):
        return self._qtd_parcelas

    def get_valor_parcela (self):
        return self._valor_parcela