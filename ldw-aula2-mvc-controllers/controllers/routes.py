from flask import render_template, request, redirect, url_for


# Lista em python (array)
players = ['Lucas', 'Eric', 'Kaique', 'Leandro']
gamelist = [{}]
def ini_app(app):

  # definindo a rota principal da aplicação
    @app.route('/')
    def home():  # função que vai ser acionada ao utilizar a rota
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        title = 'Tarisland'
        year = 2022
        category = 'MMORPG'

        # Dicionário em python (objeto)
        console = {'name': 'PS5',
                   'manofactory': 'sony',
                   'year': 2020}

        # tratando requisições com request
        if request.method == 'POST':
            # coletando o texto da input
            if request.form.get('player'):
                players.append(request.form.get('player'))
                return redirect(url_for('games'))

        return render_template('games.html', title=title, year=year, category=category, players=players, console=console)


    @app.route('/newGame', methods=['GET', 'POST'])
    def newgame():
        if request.method == "POST":
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                gamelist.append({'title': request.form.get('title'),
                                 'year': request.form.get('year'),
                                 'category': request.form.get('category')})
                return redirect(url_for('newgame'))
        return render_template('newGame.html', gamelist=gamelist)
