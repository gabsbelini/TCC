from Tkinter import *


listaposLinhas = [0,0,0,0,0]
posLinhac0 = 0
variaveisCheckbox = []
lista = []
def printaIHC(event):
    palavrasSelecionadas = []
    for x in variaveisCheckbox:
        if x.get() != '':
            palavrasSelecionadas.append(x.get())
    print palavrasSelecionadas

def adicionaOutros(iri, variaveisCheckbox, posLinha, posColuna, root):
    for letra in iri:
        if letra == ':':
            idx = iri.index(letra)
            palavra = iri[idx+1:]
    var = StringVar()
    variaveisCheckbox.append(var)
    ck = Checkbutton(root, text=palavra, onvalue=palavra, offvalue="", variable=variaveisCheckbox[-1])
    print(palavra, posLinha, posColuna )
    #print('linha', posLinha)
    ck.grid(row=posLinha, column=posColuna, sticky=W)
    return variaveisCheckbox

def adicionaTopLayer(iri, variaveisCheckbox, posLinhac0, root):
    for letra in iri:
        if letra == ':':
            idx = iri.index(letra)
            palavra = iri[idx+1:]
    var = StringVar()
    variaveisCheckbox.append(var)
    cx = Checkbutton(root, text=palavra, onvalue=palavra, offvalue="", variable=variaveisCheckbox[-1])
    cx.grid(row=posLinhac0, column=0, sticky=W)
    print('linha top', posLinhac0)
    return variaveisCheckbox
arquivo = open('ontoTree.txt', 'r')
for linha in arquivo:
    lista.append(linha.strip('\n'))
root = Tk()


while lista:
    if lista[0].startswith('teste'):
        if max(listaposLinhas) == 0:
            posLinhac0 = 0
        else:
            posLinhac0 = max(listaposLinhas)
            posLinhac0 += 1
        variaveisCheckbox = adicionaTopLayer(lista[0], variaveisCheckbox, posLinhac0, root)
        for item in listaposLinhas:
            listaposLinhas[listaposLinhas.index(item)] = max(listaposLinhas)
        for item in listaposLinhas:
            listaposLinhas[listaposLinhas.index(item)] = item+ 1
        listaposLinhas[-1] = 500
        print(listaposLinhas)
        print('entrou toplayer')
    elif lista[0].startswith('----t'):
        variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, listaposLinhas[1], 1, root)
        listaposLinhas[1] += 1
    elif lista[0].startswith('--------t'):
        variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, listaposLinhas[2], 2, root)
        listaposLinhas[2] += 1
    elif lista[0].startswith('------------t'):
        variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, listaposLinhas[3], 3, root)
        listaposLinhas[3] += 1
    elif lista[0].startswith('----------------t'):
        variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, listaposLinhas[4], 4, root)
        listaposLinhas[4] += 1
    lista.pop(0)

botao = Button(root, text="botao")
botao.grid(row=0, column=6)
botao.bind('<Button-1>', printaIHC)

root.mainloop()
