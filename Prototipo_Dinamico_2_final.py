from Tkinter import *

atual = 0
ultimo = 0
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

linha = -1
while lista:
    if lista[0].startswith('http'):
        linha += 1
        variaveisCheckbox = adicionaTopLayer(lista[0], variaveisCheckbox, linha, root)
        ultimo = ''
    elif lista[0].startswith('----ht'):
        atual = '----ht'
        if len(atual) > len(ultimo):
            variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, linha, 1, root)
        else:
            linha += 1
            variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, linha, 1, root)
        ultimo = '----ht'
    elif lista[0].startswith('--------ht'):
        atual = '--------ht'
        if len(atual) > len(ultimo):
            variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, linha, 2, root)
        else:
            linha += 1
            variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, linha, 2, root)
        ultimo = '--------ht'
    elif lista[0].startswith('------------ht'):
        atual = '------------ht'
        if len(atual) > len(ultimo):
            variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, linha, 3, root)
        else:
            linha += 1
            variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, linha, 3, root)
        ultimo = '------------ht'
    elif lista[0].startswith('----------------ht'):
        atual = '----------------ht'
        if len(atual) > len(ultimo):
            variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, linha, 4, root)
        else:
            linha += 1
            variaveisCheckbox = adicionaOutros(lista[0], variaveisCheckbox, linha, 4, root)
        ultimo = '----------------ht'
    lista.pop(0)

botao = Button(root, text="botao")
botao.grid(row=0, column=6)
botao.bind('<Button-1>', printaIHC)

root.mainloop()
