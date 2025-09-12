from flask import render_template, request, redirect, url_for
import requests

def init_app(app):
    
    products = ['Camiseta Básica Preta', 'Calça Jeans Skinny', 'Blazer de Linho', 'Vestido Midi Floral', 'Jaqueta de Couro', 'Saia Plissada', 'Blusa de Tricô', 'Shorts de Sarja']
    productlist = [{'Produto': 'Camiseta Básica', 'Categoria': 'Camisetas', 'Modelo': 'Básica Preta', 'Tamanhos': 'P, M, G, GG'}]
        
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/clientes', methods=['GET','POST'])
    def clientes():
        clientes=['Leandro']
        
        return render_template('clientes.html', 
                            clientes=clientes)

    @app.route('/novoproduto', methods=['GET','POST'])
    def novoproduto():
        
        # Tratando a requisição POST
        if request.method == 'POST':
            
            if request.form.get('product') and request.form.get('category') and request.form.get('model') and request.form.get('sizes'):
                productlist.append({'Produto': request.form.get('product'), 'Categoria' : request.form.get('category'), 'Modelo': request.form.get('model'), 'Tamanhos': request.form.get('sizes')})
                return redirect(url_for('novoproduto'))
                
        return render_template('novoProduto.html', productlist=productlist)
    
    
    @app.route('/roupas')
    def roupas():
        API_URL = "https://fakestoreapi.com/products/category/men's clothing"  # Coloque a URL real da API aqui
        
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            produtos_street = response.json()
            # produtos_street deve ser uma lista de dicts, ex: 
            # [{'name': 'Camiseta Oversized', 'category': 'Camisetas', 'model': 'Oversized', 'sizes': 'P, M, G'}, ...]
        except Exception as e:
            print(f"Erro ao buscar API: {e}")
            produtos_street = []  # fallback vazio
        
        return render_template('roupas.html', produtos=produtos_street)