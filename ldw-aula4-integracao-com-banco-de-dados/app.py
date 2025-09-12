from flask import Flask, render_template
from controllers import routes
from models.database import db
import os

# criando instancia do flask
# __name__ representa o nome do arquivo que está sendo executrado
app = Flask(__name__, template_folder='views')

routes.ini_app(app)


# extraindo o diretório absoluto do arquivo
dir = os.path.abspath(os.path.dirname(__file__))

# Criando o arquivo do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/games.sqlite3')
# só starta o server se esse arquivo em específico for executado, não vai se app for importado e utilizado como um módulo
if __name__ == '__main__':
    db.init_app(app=app)
    
    # Verificar se 
    with app.test_request_context():
        db.create_all()
    
    # iniciando o servidor
    app.run(host='0.0.0.0', port='5000', debug=True)
