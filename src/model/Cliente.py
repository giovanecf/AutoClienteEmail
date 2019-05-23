from src.DataBase.DataBase import DataBase


class Cliente:

    def __init__(self):
        self.nome = None
        self.email = None
        self.id = None


    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email



