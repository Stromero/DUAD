
class Category():

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

class Transaction():

    def __init__(self, detail_p,category_p,type_p,amount_p):
        self.detail = detail_p
        self.category = category_p
        self.type = type_p
        self.amount = amount_p 
        