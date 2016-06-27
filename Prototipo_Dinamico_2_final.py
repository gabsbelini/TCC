from Tkinter import *


listaposLinhas = [0,0,0,0,0]
listaFlags = [False, False, False, False, False]
posLinhac0 = 0
variaveisCheckbox = []
lista = []
def printaIHC(event):
    palavrasSelecionadas = []
    for x in variaveisCheckbox:
        if x.get() != '':
            palavrasSelecionadas.append(x.get().strip('\n'))
    print palavrasSelecionadas

def adicionaOutros(iri, variaveisCheckbox, posLinha, posColuna, root):
    for letra in iri:
        if letra == '#':
            idx = iri.index(letra)
            palavra = iri[idx+1:]
    var = StringVar()
    variaveisCheckbox.append(var)
    ck = Checkbutton(root, text=palavra, onvalue=palavra, offvalue="", variable=variaveisCheckbox[-1])
    print(palavra, posLinha, posColuna )
    ck.grid(row=posLinha, column=posColuna, sticky=W)
    return variaveisCheckbox

def adicionaTopLayer(iri, variaveisCheckbox, posLinhac0, root):
    for letra in iri:
        if letra == '#':
            idx = iri.index(letra)
            palavra = iri[idx+1:]
    var = StringVar()
    variaveisCheckbox.append(var)
    cx = Checkbutton(root, text=palavra, onvalue=palavra, offvalue="", variable=variaveisCheckbox[-1])
    cx.grid(row=posLinhac0, column=0, sticky=W)
    print('linha top', posLinhac0)
    return variaveisCheckbox

def abreArquivo():
    arquivo = open('ontoTreeFinal.txt', 'r')
    lista = [linha for linha in arquivo]
    print('tamanho lista', len(lista))
    return lista
lista = abreArquivo()
root = Tk()


while lista:
    if lista[0].startswith('http'):
        if max(listaposLinhas) == 0:
            posLinhac0 = 0
        else:
            posLinhac0 = max(listaposLinhas)
        variaveisCheckbox = adicionaTopLayer(lista[0], variaveisCheckbox, posLinhac0, root)
        listaposLinhas = [max(listaposLinhas) for x in listaposLinhas]
        listaFlags = [False for x in listaFlags]
        print(listaposLinhas)
        print('entrou toplayer')
    elif lista[0].startswith('----ht'):
        variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, listaposLinhas[1], 1, root)
        listaposLinhas[1] += 1
        listaFlags[1] = True
    elif lista[0].startswith('--------ht'):
        if listaposLinhas[3] == True or listaposLinhas[4] == True:
            listaposLinhas[3] = max(listaposLinhas[3], listaposLinhas[4], listaposLinhas[2])
        variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, listaposLinhas[2], 2, root)
        listaposLinhas[2] += 1
        listaFlags[2] = True
    elif lista[0].startswith('------------ht'):
        if listaFlags[4] == True:
            listaposLinhas[3] = max(listaposLinhas[4], listaposLinhas[3])
        variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, listaposLinhas[3], 3, root)
        listaposLinhas[3] += 1
        listaFlags[3] = True
    elif lista[0].startswith('----------------ht'):
        variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, listaposLinhas[4], 4, root)
        listaposLinhas[4] += 1
        listaFlags[4] = True
    lista.pop(0)

botao = Button(root, text="botao")
botao.grid(row=0, column=6)
botao.bind('<Button-1>', printaIHC)

root.mainloop()
