from database_con_exe import *

class Pertanyaan_induk():
    counti = 1
    def __init__(self,question):
        self.question = question
        self.id = Pertanyaan_induk.counti
        Pertanyaan_induk.counti += 1

class Pertanyaan():
    count = 1
    def __init__(self, question):
        self.question = question
        self.id = Pertanyaan.count
        Pertanyaan.count += 1

class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

mycursor.execute("SELECT id,pw from tabel_admin")
daftar_id = list()
for i in mycursor:
    id = i[0]
    pw = i[1]
    id_pw =[id,pw]
    daftar_id.append(id_pw)
id = 0
pw = 1

