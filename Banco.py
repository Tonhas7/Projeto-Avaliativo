import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.conexao.execute("PRAGMA foreign_keys = ON")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_usuarios(
            idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            usuario TEXT,
            senha TEXT)""")

        c.execute("""CREATE TABLE IF NOT EXISTS tbl_cidades(
            idcidade INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade TEXT,
            uf TEXT)""")

        c.execute("""CREATE TABLE IF NOT EXISTS tbl_clientes(
            idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            nascimento TEXT,
            cpf TEXT,
            genero TEXT,
            cidade TEXT
            idcidade INTEGER,
            FOREIGN KEY (idcidade) REFERENCES tbl_cidades (idcidade))""")  # Adicionada a criação da tabela tbl_clientes

        self.conexao.commit()
        c.close()
