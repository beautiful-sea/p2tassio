from application import app
from flask import render_template, request
import json
from application.model.dao.ProdutoDAO import ProdutoDAO

@app.route("/")
def home():
    produtos = ProdutoDAO().get_produtos()
    return render_template('index.html', produtos = produtos)