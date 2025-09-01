from flask import render_template, request, redirect, url_for

def init_app(app):
    
    products = ['Camiseta Básica Preta', 'Calça Jeans Skinny', 'Blazer de Linho', 'Vestido Midi Floral', 'Jaqueta de Couro', 'Saia Plissada', 'Blusa de Tricô', 'Shorts de Sarja']
    productlist = [{'Produto': 'Camiseta Básica', 'Categoria': 'Camisetas', 'Modelo': 'Básica Preta', 'Tamanhos': 'P, M, G, GG'}]
        
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/produtos', methods=['GET','POST'])
    def produtos():
        product = 'Camiseta Básica'
        category = 'Camisetas'
        sizes = [{'Tamanho' : 'P',
                'Medidas': '46x68'}, 
        {'Tamanho' : 'M', 'Medidas':'50x70'},
        {'Tamanho': 'G', 'Medidas':'54x72'},
        {'Tamanho': 'GG', 'Medidas': '58x74'}]
        
        return render_template('produtos.html', 
                            product=product,
                            category=category,
                            products=products,
                            sizes=sizes,
                            productlist=productlist)

    @app.route('/novoproduto', methods=['GET','POST'])
    def novoproduto():
        
        # Tratando a requisição POST
        if request.method == 'POST':
            
            if request.form.get('product') and request.form.get('category') and request.form.get('model') and request.form.get('sizes'):
                productlist.append({'Produto': request.form.get('product'), 'Categoria' : request.form.get('category'), 'Modelo': request.form.get('model'), 'Tamanhos': request.form.get('sizes')})
                return redirect(url_for('novoproduto'))
                
        return render_template('novoProduto.html', productlist=productlist)