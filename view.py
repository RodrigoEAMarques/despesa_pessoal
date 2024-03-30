import sqlite3 as lite

# Conexao com o banco
conn = lite.connect('dados.db')

# Funções para inserir no banco
# -------------------------------------


# Inserir categorias
def insert_categorie(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO Categoria (nome) VALUES(?)"
        cur.execute(query, i)


# Inserir receitas
def insert_receitas(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES(?, ?, ?)"
        cur.execute(query, i)


# Inserir gastos
def insert_gastos(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES(?, ?, ?)"
        cur.execute(query, i)


# Funções para deletar no banco
# -------------------------------------


def delete_receitas(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)


def delete_gastos(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)


# Funções para ver os dados
# ------------------------------------

# Ver categoria
def post_categoria():
    list_itens = []
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for line in linha:
            list_itens.append(line)

    return list_itens


# Ver receitas
def post_receitas():
    list_itens = []
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for line in linha:
            list_itens.append(line)

    return list_itens


# Ver gastos
def post_gastos():
    list_itens = []
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for line in linha:
            list_itens.append(line)

    return list_itens