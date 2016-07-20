#-*- coding: utf-8 -*-
from Tkinter import *
import time
''' arquitetura, fluxograma visual mostrando interação entre o programas,interface com usser
, ontologia, internet, usuário, busca na internet, pode fazer em astah
falar sobre como criei a ontologia, o programa, de onde tirei a ontologia, SS mostrando protege,
 partes da ontologia, SS do XML da ontologia, talvez ate explicar como gerar o XML da ontologia, qual formato salvar etc...
 explicar o processo de extração da ontologia e geração do arquivo para montar a interface, falar sobre interface grafica
 explicar como usar a interface, como ela esta organizada identação etc... Falar que o usuario pode selecionar...
 explicar um pouco sobre selenium, mostrar um exemplo de uma busca, explicar que o selenium é tipo um robo,
 como se fosse um user interagindo com o browser dizezr que o google nao permite urlreq direta e bloqueia.

 A conclusao eu explico como eu atingi cada obj especifico, e ai com eles como eu atingi o obj geral do trab, e apos
 isso explicar possibilidades futuras, fazer ontologia de outra area e utilizar no sistema
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver

atual = 0
ultimo = 0
listaposLinhas = [0,0,0,0,0]
listaFlags = [False, False, False, False, False]
posLinhac0 = 0
variaveisCheckbox = []



def init_driver():
    driver = webdriver.Chrome('/home/gabsbelini/chromedriver')
    driver.wait = WebDriverWait(driver, 5)
    return driver

def lookup(driver, query):
    driver.get("http://www.google.com")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "q")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "btnK")))
        box.send_keys(query)
        button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")

def printaIHC(event):
    palavrasSelecionadas = []
    for x in variaveisCheckbox:
        if x.get() != '':
            palavrasSelecionadas.append(x.get().strip('\n'))
    palavrasSelecionadas[-1] = palavrasSelecionadas[-1]+'\n'
    print palavrasSelecionadas
    palavrasSelecionadas = [w.replace('_', ' ') for w in palavrasSelecionadas]
    driver = init_driver()
    lookup(driver, palavrasSelecionadas)
    time.sleep(5)
    driver.quit()

def adicionaOutros(iri, variaveisCheckbox, posLinha, posColuna, root):
    for letra in iri:
        if letra == '#':
            idx = iri.index(letra)
            palavra = iri[idx+1:]
    var = StringVar()
    variaveisCheckbox.append(var)
    ck = Checkbutton(root, text=palavra, onvalue=palavra+' ', offvalue="", variable=variaveisCheckbox[-1])
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
    cx = Checkbutton(root, text=palavra, onvalue=palavra+' ', offvalue="", variable=variaveisCheckbox[-1])
    cx.grid(row=posLinhac0, column=0, sticky=W)
    print('linha top', posLinhac0)
    return variaveisCheckbox

def abreArquivo(arqtxt):
    arquivo = open(arqtxt, 'r')
    lista = [linha for linha in arquivo]
    print('tamanho lista', len(lista))
    lista = lista[15:]
    return lista


def getFileName(event):
    global filename
    filename = entry1.get()
    root1.destroy()
#filename = '1'
root1 = Tk()
botaook = Label(root1, text='OK', bg='green', fg='white')
botaook.bind('<Button-1>', getFileName)
botaook.grid(row=2, column=1)
entry1 = Entry(root1)
label1 = Label(root1, text='Nome do arquivo')
entry1.grid(row=1, column=1)
label1.grid(row=0, sticky=E)
root1.mainloop()
lista = abreArquivo(filename)
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
