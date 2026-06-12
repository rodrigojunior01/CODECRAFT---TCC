import sqlite3

DB_NAME = "codecraft.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            pontuacao INTEGER DEFAULT 0,
            nivel INTEGER DEFAULT 1
        )
    """)

    conn.commit()
    conn.close()


def inserir_jogador(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO jogadores (nome) VALUES (?)",
        (nome,)
    )

    conn.commit()
    conn.close()


def atualizar_jogador(nome, pontuacao, nivel):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE jogadores
        SET pontuacao = ?, nivel = ?
        WHERE nome = ?
    """, (pontuacao, nivel, nome))

    conn.commit()
    conn.close()
