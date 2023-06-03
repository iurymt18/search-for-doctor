# import sqlite3 as lite
# import pandas as pd
import time
import openpyxl
tabela = pd.read_excel(r"C:\Users\Monteiro\Desktop\buscar medico\banco de dados\medicosdb.xlsx")
con = lite.connect('medicosdb.db')

#criando tabela médicos
# with con:
#     cur = con.cursor()
#     cur.execute("CREATE TABLE Medicos(id INTEGER, nome TEXT, sit TEXT, PRIMARY KEY('id' ))")
#     print()

#selecionando e exibindo dados da tabela
# cur=con.cursor()
# cur.execute("SELECT * FROM Medicos")
#
# print(cur.fetchall())

#inserindo dados um a um
# with.con:
#     cur=con.cursor()
#     cur.execute("INSERT INTO Medicos (id) VALUE('')")
#     cur.execute("INSERT INTO Medicos (nome) VALUE('')")
#     cur.execute("INSERT INTO Medicos (sit) VALUE('')")

#inserindo varios dados

#  with con:
#      cur = con.cursor()
#      query = ("INSERT INTO Medicos (id, nome, sit) VALUES(?,?,?)")
#      cur.execute(query)

#script com pandas para inserir dados da tabela
for i in range (len(tabela)):
    id = str(tabela.loc[i,"Codigo"])
    nome = tabela.loc[i, "Nome"]
    sit = tabela.loc[i, "S"]
    valores =[id, nome, sit]
    print(valores)
    with con:
        cur = con.cursor()
        query = ("INSERT INTO Medicos (id, nome, sit) VALUEs(?,?,?)")
        cur.execute(query,valores)



