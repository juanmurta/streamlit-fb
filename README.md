# 💻 tributacao-produtos

# 📕 Descrição
Este projeto consiste em um script Python que se conecta a um banco de dados Firebird para extrair informações sobre a tributação de produtos. Ele utiliza a biblioteca `firebird-driver` para estabelecer a conexão com o banco de dados e executa uma consulta SQL para buscar dados específicos de produtos e suas respectivas tributações. Além disso, o script utiliza o Streamlit para criar uma interface web simples que exibe os dados em uma tabela.

# ☕ Como Usar
1. Instale as dependências necessárias (`firebird-driver`, `streamlit`, `pandas`).
2. Ajuste o arquivo de configuração `txt_files/dbxconnections.txt` com as informações de conexão do banco de dados (caminho do banco, usuário e senha).
3. Execute o script Python.
4. Acesse a interface web gerada pelo Streamlit no navegador para visualizar a tabela de tributação dos produtos.

# 🛠️ Estrutura do Projeto
- **txt_files/dbxconnections.txt**: Arquivo de configuração com as credenciais do banco de dados.
- **main.py**: Script principal que realiza a conexão com o banco de dados, executa a consulta SQL e exibe os dados no Streamlit.

# 📂 Exemplo de Arquivo de Configuração (`dbxconnections.txt`)
```plaintext
database_path=caminho/do/banco.fdb
username=seu_usuario
password=sua_senha
```

# Contribuindo para api-flask-faturamento
1. Para contribuir com api-flask-faturamento, siga estas etapas:
2. Bifurque este repositório.
3. Crie um branch: `git checkout -b <nome_branch>`.
4. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`.
5. Envie para o branch original: `git push origin api-flask-faturamento/<local>`.
6. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
