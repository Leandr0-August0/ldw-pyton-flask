from flask import render_template


def ini_app(app):

  # definindo a rota principal da aplicação
    @app.route('/')
    def home():  # função que vai ser acionada ao utilizar a rota
        return render_template('index.html')

    @app.route('/games')
    def games():
        title = 'Tarisland'
        year = 2022
        category = 'MMORPG'

        # Lista em python (array)
        players = ['Lucas', 'Eric', 'Kaique', 'Leandro']

        # Dicionário em python (objeto)
        console = {'name': 'PS5',
                   'manofactory': 'sony',
                   'year': 2020}
        return render_template('games.html', title=title, year=year, category=category, players=players, console=console)
