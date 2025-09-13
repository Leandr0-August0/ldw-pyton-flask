from flask import render_template, request, redirect, url_for

def init_app(app):
    
    products = ['Camiseta Básica Preta', 'Calça Jeans Skinny', 'Blazer de Linho', 'Vestido Midi Floral', 'Jaqueta de Couro', 'Saia Plissada', 'Blusa de Tricô', 'Shorts de Sarja']
    productlist = [{'Produto': 'Camiseta Básica', 'Categoria': 'Camisetas', 'Modelo': 'Básica Preta', 'Tamanhos': 'P, M, G, GG'}]
    clients=['Leandro']
        
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/clientes', methods=['GET','POST'])
    def clientes():
        
        if request.method == 'POST':
            if request.form.get('name'):
                clients.append(request.form.get('name'))
                return redirect(url_for('clientes'))
        
        return render_template('clientes.html', 
                            clients=clients)

    @app.route('/novoproduto', methods=['GET','POST'])
    def novoproduto():
        
        # Tratando a requisição POST
        if request.method == 'POST':
            
            if request.form.get('product') and request.form.get('category') and request.form.get('model') and request.form.get('sizes'):
                productlist.append({'Produto': request.form.get('product'), 'Categoria' : request.form.get('category'), 'Modelo': request.form.get('model'), 'Tamanhos': request.form.get('sizes')})
                return redirect(url_for('novoproduto'))
                
        return render_template('novoProduto.html', productlist=productlist)