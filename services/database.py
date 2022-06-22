import sqlite3 
#objetos SQLite criados em um thread só podem ser usados ​​nesse mesmo thread
#check_same_thread=False <- para o erro

#Banco Login/Cadastro
conexao_cadastro = sqlite3.connect('cadastro.db', check_same_thread=False)
cursor_login = conexao_cadastro.cursor()
cursor_login.execute("CREATE TABLE IF NOT EXISTS CadastroLogin (nome text, telefone text, \
       email text, cpf text, senha text)")

#Banco Cliente
conexao_cliente = sqlite3.connect("cliente.db", check_same_thread=False)
cursor_cliente = conexao_cliente.cursor()
cursor_cliente.execute("CREATE TABLE IF NOT EXISTS Cliente(id integer primary key autoincrement, \
       nome text, idade int, sexo text, estado text, telefone text, email text, cpf text);")

#Banco Estoque
conexao_estoque = sqlite3.connect("estoque.db", check_same_thread=False)
cursor_estoque = conexao_estoque.cursor()
cursor_estoque.execute("CREATE TABLE IF NOT EXISTS Estoque(id integer primary key autoincrement, \
       nome text, marca text, categoria text, valor text, quantidade int);")