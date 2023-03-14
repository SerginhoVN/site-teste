from flask import Flask

app = Flask(__name__)

menu = """ #tem três aspas pq é string multilinhas
< a href="/">Página Inicial</a> | < a href="/sobre">Sobre</a> | < a href="/contato">Contato</a><br>
"""

@app.route("/")
def hello_world():
  return "Olá, mundo! Esse é meu site. (Sérgio Vieira)"

@app.route("/sobre")
def sobre():
  return "Aqui vai o conteúdo da página Sobre"

@app.route("/contato")
def contato():
  return "Aqui vai o conteúdo da página Contato"
