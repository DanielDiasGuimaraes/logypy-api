from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def conexao_bd():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'logpy'
    )
    return conexao

@app.route('/login', methods = ['POST'])
def enviar_nome():
        dados = request.get_json()
        user = dados['user']
        password = dados['password']

        try:
            conexao = conexao_bd()
            cursor = conexao.cursor()

            query = 'SELECT * FROM usuarios WHERE user = %s AND password = %s'
            cursor.execute(query, (user,password))
            resultado_da_consulta_mysql = cursor.fetchone()

            if resultado_da_consulta_mysql:
                return jsonify({
                    'msg':'1'
                })
            else:
                return jsonify({
                    'msg':'0'
                })
        except Exception as e:
            return jsonify({
                'msg': e
            })
        finally:
            cursor.close()
            conexao.close()


@app.route('/verificar_bd_codigo_produto', methods = ['POST'])
def verifcar_codigo_produto():
    dados = request.get_json()
    codigo = dados['codigo']

    try:
        conexao = conexao_bd()
        cursor = conexao.cursor()

        query = 'SELECT * FROM produtos WHERE codigo = %s'
        cursor.execute(query, (codigo,))
        res = cursor.fetchone()

        if res:
            return jsonify({
                'msg':'1'
            })
        else:
            return jsonify({
                'msg':'0'
            })
    except Exception as e:
        return jsonify({
            'msg': e
        })
    finally: 
        cursor.close()
        conexao.close()
    
@app.route('/cadastro_produto', methods = ['POST'])
def logica_cadastrar_produto():
    dados = request.get_json()
    nome = dados['nome']
    modelo = dados['modelo']
    descricao = dados['descricao']
    fabricante = dados['fabricante']
    fornecedor = dados['fornecedor']
    codigo = dados['codigo']
    preco = dados['preco']

    try:
        conexao = conexao_bd()
        cursor = conexao.cursor()

        query = 'INSERT INTO produtos (nome, modelo, descricao, fabricante, fornecedor, codigo, preco) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(query, (nome, modelo, descricao, fabricante, fornecedor, codigo, preco))
        conexao.commit()

        return jsonify({'msg': '1'})
    except Exception as e:
        return jsonify({'msg': '0'})
    finally:
        cursor.close()
        conexao.close()





@app.route('/consultar_produto_alterar', methods = ['POST'])
def consultar_produto():
    try:
        dados = request.get_json()
        codigo = dados['codigo']

        conexao = conexao_bd()
        cursor = conexao.cursor()

        query = 'SELECT * FROM produtos WHERE codigo = %s'
        cursor.execute(query, (codigo,))
        res = cursor.fetchone()

        if res:
            nome = res[0]
            modelo = res[1]
            descricao = res[2]
            fabricante = res[3]
            fornecedor = res[4]
            codigo = res[5]
            preco = res[6]

            return jsonify({
                'nome': nome,
                'modelo': modelo,
                'descricao': descricao,
                'fabricante': fabricante,
                'fornecedor': fornecedor,
                'codigo': codigo,
                'preco': preco
            })
        else:
            return jsonify({
                'msg':'Produto não encontrado.'
            })
    except Exception as e:
        return jsonify({
            'msg': str(e)
        })
    finally:
        cursor.close()
        conexao.close()

@app.route('/listar_produto', methods = ['GET'])
def listar_produto_em_estoque():
    try:
        conexao  = conexao_bd()
        cursor = conexao.cursor()

        query = 'SELECT *  FROM produtos'
        cursor.execute(query)
        res = cursor.fetchall()

        if res:
            return jsonify({
                'msg': res
            })
        else:
            return jsonify({
                'msg':'0'
            })
    except Exception as e :
        print(f'{e}')
    finally:
        cursor.close()
        conexao.close()


@app.route('/excluir_produto', methods = ['POST'])
def excluirproduto():
    try:
        json_dados_front = request.get_json()
        codigo = json_dados_front['codigo']


        conexao  = conexao_bd()
        cursor = conexao.cursor()

        #Conusltar ~
        query_consulta = 'SELECT * FROM produtos WHERE codigo = %s'
        cursor.execute(query_consulta, (codigo,))
        res = cursor.fetchone()
        if res:
            query = 'DELETE FROM produtos WHERE codigo = %s'
            cursor.execute(query, (codigo,))
            conexao.commit()

            return jsonify({
                'msg':'1'
            })
        else:
            #00 seria produto nao encontrado
            return jsonify({
                'msg':'0'
            })
    except Exception as e:
        print(f'{e}')
    finally:
        cursor.close()
        conexao.close()
        

app.run(port=5000)