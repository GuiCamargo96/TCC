#from tkinter import *
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

import os

root = Tk(className = 'reconhecimento_facial_principal')
root.title('Reconhecimento Facial')
nomevalue = StringVar()
emailvalue = StringVar()

l = Label(root, text="Adicionar Nova Pessoa")
l.config(font=("Courier", 15))
l.pack()

Label(root, text="Nome: ").pack()
w1 = Entry(root, textvariable=nomevalue).pack()

Label(root, text="Email: ").pack()
w2 = Entry(root, textvariable=emailvalue).pack()

def adiciona_pessoa_btn():
    Nome = nomevalue.get()
    Email = emailvalue.get()
    os.system('python3 2_AdicionarPessoa.py %s %s' %(Nome, Email))

def resetar_pessoa_btn():
    os.system('python3 6_ResetarValores.py')

def prepara_dados_Fisher_btn():
    Nome = nomevalue.get()
    os.system('python3 5_1_PreparaDadosFisher.py %s'%Nome)

def reconhecimento_facial_Fisher_btn():
    os.system('python3 5_2_ReconhecimentoFacialFisher.py')

add_btn = Button(root, text = "Adicionar", command = adiciona_pessoa_btn)
add_btn.pack()

reset_btn = Button(root, text = "Resetar Entrada", command = resetar_pessoa_btn)
reset_btn.pack()

f=Frame(root,height=1, width=400, bg="black")
f.pack()

l = Label(root, text="Preparar Dados")
l.config(font=("Courier", 15))
l.pack()

recogL_btn = Button(root, text = "Preparar Dados (Fisher)", command = prepara_dados_Fisher_btn)
recogL_btn.pack()

f=Frame(root,height=1, width=400, bg="black")
f.pack()

l = Label(root, text="Reconhecimento Facial")
l.config(font=("Courier", 15))
l.pack()

recogL_btn = Button(root, text = "Reconhecimento Facial (Fisher)", command = reconhecimento_facial_Fisher_btn)
recogL_btn.pack()

root.mainloop()
