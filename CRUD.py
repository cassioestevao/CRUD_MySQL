import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='openwork',
)
cursor = conexao.cursor()

#/////////////////////////////////////   ESTUDO   /////////////////////////////////////////////////////////
nome_usuario = "admin"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_usuario}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

#/////////////////////////////////////////////////////////////////////////////////////////////////////////
cursor.close()
conexao.close()



#////////////////////////////////////// CREATE  /////////////////////////////////////////////////////////
#
#
#   nome_usuario = "admin"
#   senha = 123456
#   comando = f'INSERT INTO vendas (nome_usuario, senha) VALUES ("{nome_usuario}", {senha})'
#   cursor.execute(comando)
#   conexao.commit() # edita o banco de dados
#
#///////////////////////////////////////////////////////////////////////////////////////////////////////



# //////////////////////////////////// READ //////////////////////////////////////////////////////////
#
# 
# comando = f'SELECT * FROM openwork.usuario'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)
#///////////////////////////////////////////////////////////////////////////////////////////////////



#//////////////////////////////////// UPDATE //////////////////////////////////////////////////////
# 
#
# nome_usuario = "admin"
# valor = 123456
# comando = f'UPDATE vendas SET senha = {valor} WHERE username = "{nome_usuario}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados
#
#///////////////////////////////////////////////////////////////////////////////////////////////////



#/////////////////////////////////////// DELETE /////////////////////////////////////////////
# 
#   nome_produto = "admin"
#   comando = f'DELETE FROM username WHERE usuarios = "{nome_usuario}"'
#   cursor.execute(comando)
#   conexao.commit() # edita o banco de dados
#
#/////////////////////////////////////////////////////////////////////////////////////////////
