import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
# comando = '''CREATE TABLE Marca (
#                 id INTEGER NOT NULL,
#                 nome TEXT NOT NULL,
#                 sigla CHARACTER(2) NOT NULL,
#                 PRIMARY KEY (id)
#                 );'''
                
comando3 = '''CREATE TABLE Pessoa (
    cpf INTEGER NOT NULL,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL,
    oculos BOOLEAN NOT NULL,
    PRIMARY KEY (cpf));'''
    
comando2 = '''CREATE TABLE Veiculo (
placa CHARACTER(7) NOT NULL,
ano INTEGER NOT NULL,
cor TEXT NOT NULL,
motor REAL NOT NULL,
proprietario INTEGER NOT NULL,
marca INTEGER NOT NULL,
PRIMARY KEY (placa),
FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
FOREIGN KEY(marca) REFERENCES Marca(id)
);'''

comando4 = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
VALUES (12345678900, 'João', '2000-01-31', 1);'''

                  
cursor.execute(comando4)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()