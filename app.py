from firebird.driver import connect
import streamlit as st
import pandas as pd


def read_db_config(file_path):  # funcao para ler arquivo ini do firebird
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            config[key.strip()] = value.strip()
    return config


config = read_db_config('txt_files/dbxconnections.txt')

# Conectar no banco de dados
conexao = connect(database=config['database_path'], user=config['username'], password=config['password'])
cursor = conexao.cursor()

st.title('Tributação dos Produtos')

cursor.execute('''
SELECT produto.codpro, produto.despro, tributo.uf, tributo.procla, tributo.sittrib, tributo.substituicao
FROM PRODUTO
inner JOIN tributo on tributo.codpro = produto.codpro
where produto.codemp = '001'
and tributo.idprodutotipo = '01'
and tributo.procla = '5'
ORDER BY PRODUTO.codpro
''')
produto = cursor.fetchall()

# PEGAR O NOME DOS CAMPOS DA TABELA
descricao = cursor.description
colunas = [tupla[0] for tupla in cursor.description]
# print(colunas)

# CRIANDO UMA TABELA COM OS DADOS DO BANCO
tabela_produtos = pd.DataFrame.from_records(produto, columns=[colunas])

# print(tabela_produtos)

conexao.close()
cursor.close()

st.write(tabela_produtos)




