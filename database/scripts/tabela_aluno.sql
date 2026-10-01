-- Cria a tabela 'alunos' se ela não existir
CREATE TABLE IF NOT EXISTS alunos (
    -- matricula: texto, 10 caracteres, obrigatória
    matricula TEXT NOT NULL PRIMARY KEY,                
    
    -- nome_completo: não nulo, não vazio, min 5 e máx 50 caracteres
    nome_completo TEXT NOT NULL CHECK(length(nome_completo) > 4 AND length(nome_completo) <= 50),                
    
    -- Constraint adicional: garante que a matrícula tenha exatamente 10 dígitos
    -- (Funciona para matrículas numéricas entre 1000000000 e 9999999999)
    CHECK(length(cast(matricula as text)) = 10)
);