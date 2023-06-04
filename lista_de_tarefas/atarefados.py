import mysql.connector
from datetime import datetime


class Dbase:
    def __init__(self):
       self._conector = mysql.connector.connect(user='root', host='127.0.0.1', password='', database='tarefas')

    def insert(self, n, d, h):
        a = self._conector
        b = a.cursor()
        c = f"insert into tarefinhas(nome, dia, hora) values('{n}', '{d}', '{h}');"
        b.execute(c)
        a.commit()
        b.close()
        a.close()

    def select(self):
        a = self._conector
        b = a.cursor()
        c = "select * from tarefinhas;"
        b.execute(c)
        for i in b:
            for co in i:
                print(co)
        b.close()
        a.close()

    def delete(self, d):
        a = self._conector
        b = a.cursor()
        c = f"delete from tarefinhas where idtarefas = '{d}';"
        b.execute(c)
        a.commit()
        b.close()
        a.close()


class Atarefado:
    def __init__(self, dat):
        self.tarefas = dat

    def adicionar(self, no):
        di = datetime.now().day
        ho = datetime.now().hour
        self.tarefas.insert(no, di, ho)

    def mostar(self):
        self.tarefas.select()

    def remover(self, d):
        self.tarefas.delete(d)



tarefa = Atarefado(Dbase())
#tarefa.adicionar('lavar a louça')
#tarefa.mostar()
#tarefa.remover(4)

