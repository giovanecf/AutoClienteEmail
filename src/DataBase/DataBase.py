import sqlite3

class DataBase:
        #conn, c = None, None

    def __init__(self):
        self.conn = sqlite3.connect("dataBase")
        self.c = self.conn.cursor()


    def CadastrarCliente(self, cliente):
        self.c.execute("INSERT INTO Cliente (NOME, EMAIL) VALUES (?, ?)",
                        (cliente.nome, cliente.email))

        self.conn.commit()
        #self.db.c.close()
        #self.db.conn.close()

    def ObterClientes(self):
        self.c.execute("SELECT * FROM Cliente")
        data = self.c.fetchall()

        #self.db.c.close()
        #self.db.conn.close()

        return data

    def PesquisarClientes(self, pesquisa):
        self.c.execute("""SELECT * FROM Cliente WHERE NOME LIKE ? OR EMAIL LIKE ?""",
                       ("%"+pesquisa+"%", "%"+pesquisa+"%"))
        data = self.c.fetchall()

        #self.db.c.close()
        #self.db.conn.close()

        return data

    def EditarCliente(self, cliente):
        self.c.execute("UPDATE Cliente SET NOME = ?, EMAIL = ? WHERE ID = ?",
                        (cliente.nome, cliente.email, cliente.id))

        self.conn.commit()
        #self.db.c.close()
        #self.db.conn.close()


    def DeletarCliente(self, cliente):
        self.c.execute("DELETE FROM Cliente WHERE ID = ?",(cliente.id,))

        self.conn.commit()
        #self.db.c.close()
        #self.db.conn.close()