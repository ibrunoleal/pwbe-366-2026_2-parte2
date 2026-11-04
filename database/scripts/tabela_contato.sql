CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL CHECK(length(nome) BETWEEN 5 AND 50),
    telefone TEXT NOT NULL UNIQUE CHECK(length(telefone) BETWEEN 13 AND 14),
    matricula TEXT NOT NULL,
    FOREIGN KEY (matricula) REFERENCES alunos(matricula)
);
