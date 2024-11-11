from flask import Flask
from flask import request
from flask import render_template
from mysql.connector import (connection)

app = Flask(__name__)

@app.route('/')
def teste():
    return render_template('insert.html')

@app.route('/adicao', methods=['POST'])
def adicao():
    nome = request.form['nome']
    raca = request.form['raca']

    # CONEXÃO
    cnx = connection.MySQLConnection(
        user = 'root',
        password = 'labinfo',
        host = '127.0.0.1',
        database = 'petshop'
    )

    # ESCRITA
    sql = "INSERT INTO animal (nome, raca) VALUES (%s, %s)"
    tupla = (nome, raca)

    # ENVIO
    cursor = cnx.cursor()
    cursor.execute(sql,tupla)
    cnx.commit()

    # FECHAR
    cnx.close()

    return 'SUCESSO, adicionado!!!