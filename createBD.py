import sqlite3 as lite

# Criando conexao com banco
conn = lite.connect('dados.db')

# Criando tabela de categorias
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

# Criando tabela de receitas
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

# Criando tabela de gastos
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")