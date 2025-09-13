from flask import render_template, request, redirect, url_for
import requests


def init_app(app):

    products = ['Camiseta Básica Preta', 'Calça Jeans Skinny', 'Blazer de Linho',
        'Vestido Midi Floral', 'Jaqueta de Couro', 'Saia Plissada', 'Blusa de Tricô', 'Shorts de Sarja']
    productlist = [{'Produto': 'Camiseta Básica', 'Categoria': 'Camisetas',
        'Modelo': 'Básica Preta', 'Tamanhos': 'P, M, G, GG'}]
    clients = ['Leandro']

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/clientes', methods=['GET', 'POST'])
    def clientes():

        if request.method == 'POST':
            if request.form.get('name'):
                clients.append(request.form.get('name'))
                return redirect(url_for('clientes'))

        return render_template('clientes.html',
                            clients=clients)

    @app.route('/novoproduto', methods=['GET', 'POST'])
    def novoproduto():

        # Tratando a requisição POST
        if request.method == 'POST':

            if request.form.get('product') and request.form.get('category') and request.form.get('model') and request.form.get('sizes'):
                productlist.append({'Produto': request.form.get('product'), 'Categoria': request.form.get(
                    'category'), 'Modelo': request.form.get('model'), 'Tamanhos': request.form.get('sizes')})
                return redirect(url_for('novoproduto'))

        return render_template('novoProduto.html', productlist=productlist)

    @app.route('/roupas', methods=['GET', 'POST'])
    @app.route('/roupas/<int:id>', methods=['GET', 'POST'])
    def roupas(id=None):
        # Coloque a URL real da API aqui
        API_URL = "https://fakestoreapi.com/products/category/men's clothing"

        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            produtos_street = response.json()
            # produtos_street deve ser uma lista de dicts, ex:
            # [{'name': 'Camiseta Oversized', 'category': 'Camisetas', 'model': 'Oversized', 'sizes': 'P, M, G'}, ...]
        except Exception as e:
            print(f"Erro ao buscar API: {e}")
            produtos_street = []  # fallback vazio

        if id is not None:
            produto = next((p for p in produtos_street if p['id'] == id), None)
            if produto:
                return render_template('roupaInfo.html', produto=produto)
            else:
                return "Produto não encontrado", 404
        else:
            return render_template('roupas.html', produtos=produtos_street)