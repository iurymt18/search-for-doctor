import sqlite3 as lite
from io import BytesIO
from tkinter import *
from PIL import ImageTk, Image
from urllib.request import urlopen

#banco de dados
con = lite.connect('medicosdb.db')

def exibir_foto(valor):
    try:

        URL = f"https://api.cremesp.org.br/guia-medico/medico-info/{valor}/image"
        u = urlopen(URL)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        photo = ImageTk.PhotoImage(im)
        cx_foto.config(image=photo)
        cx_foto.image = photo

    except:
        foto_nao_disponivel = PhotoImage(file="img/imagem_indisponivel.png")
        cx_foto.config(image=foto_nao_disponivel)
        cx_foto.image = foto_nao_disponivel


def consulta(crm):
    with con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Medicos WHERE id={crm}")
        dados = cur.fetchall()
    return dados
#exibir dados
def exibir_dados(crm,nome,sit):
    l_resultados.config(text=f"CRM: {crm} | Nome: {nome} | Situação: {sit}", font="Arial 15", fg="white")



# função do botão
def on_click():
    crm = ed.get()
    if consulta(crm):
        dados=consulta(crm)[0]
        nome = dados[1]
        if dados [2] == "A":
            sit = "Ativo"
        else:
            sit = "Inativo"
        exibir_dados(crm,nome,sit)
        exibir_foto(crm)

    else:
        l_resultados.config(text=f"CRM {crm} não encontrado!",font="Arial 15", fg="white")
        exibir_foto(crm)


# janela
janela = Tk()
janela.title("search-for-doctor")
janela.geometry("1050x700+150+5")
janela.resizable(False,False)
janela.config(background="#343434")
#layout
#logo_top
logo = PhotoImage(file="img/logo.png")
logo_top_image = Label(janela, bg="#343434", image=logo)
logo_top_image.grid(column=0,row=0, padx=147, pady=20)
#2 caixa busca
cx_busca = Label(janela, text="", bg="#343434")
cx_busca.grid(column=0, row=2, pady=20)
#3 label texto  descritivo
l_texto = Label(cx_busca, text="Digite o CRM para realizar busca: ", bg="#343434", font='Arial 25', fg='white')
l_texto.grid(column=0, row=0, pady=20)
#4 input
ed = Entry(cx_busca, width=50, bg="#343434", fg="white", font="Arial 14")
ed.grid(column=0, row=1, ipady=5)
#5 button
btn_buscar = Button(cx_busca, bg="#343434", text="buscar", fg="white", font="Arial 12",command=on_click)
btn_buscar.grid(column=1, row=1, padx=2 ,ipadx=5, ipady=6)
#6 caixa de resultados
l_resultados = Label(janela,text="", bg="#343434")
l_resultados.grid(column=0, row=3, pady=0)
#7 caixa foto
cx_foto = Label(janela,bg="#343434", image=None)
cx_foto.grid(column=0, row=4)

janela.mainloop()





