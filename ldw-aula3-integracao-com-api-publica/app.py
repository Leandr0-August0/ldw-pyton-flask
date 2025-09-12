from flask import Flask, render_template


from controllers import routes

# criando instancia do flask
# __name__ representa o nome do arquivo que está sendo executrado
app = Flask(__name__, template_folder='views')

routes.ini_app(app)
# só starta o server se esse arquivo em específico for executado, não vai se app for importado e utilizado como um módulo
if __name__ == '__main__':
    # iniciando o servidor
    app.run(host='localhost', port='5000', debug=True)
