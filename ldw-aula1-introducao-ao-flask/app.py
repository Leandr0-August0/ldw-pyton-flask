from flask import Flask, render_template

# criando instancia do flask
# __name__ representa o nome do arquivo que está sendo executrado
app = Flask(__name__, template_folder='views')

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
               'year' : 2020}
    return render_template('games.html', title=title, year=year, category=category, players=players, console=console)


# só starta o server se esse arquivo em específico for executado, não vai se app for importado e utilizado como um módulo
if __name__ == '__main__':
    # iniciando o servidor
    app.run(host='localhost', port='5000', debug=True)
