# -*- coding: utf-8 -*-
from Tkinter import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Firefox()
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
root = Tk()
botao = Button(root, text="botao")
botao.grid(row=11, column=3)
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
var10 = StringVar()
var11 = StringVar()
var12 = StringVar()
var13 = StringVar()
var14 = StringVar()
var15 = StringVar()
var16 = StringVar()
print(var1.get())
c1 = Checkbutton(root, text="Processamento de Linguagem Natural", onvalue="Processamento de Linguagem Natural", offvalue="", variable=var1)
#c2 = Checkbutton(root, text="Representação de conhecimento e raciocinio", variable=var2, onvalue=5, offvalue=0)
#c3 = Checkbutton(root, text="Resolucao de problemas", variable=var3, onvalue=7, offvalue=0)
c1.grid(row=0, column=0, sticky=W)
#c2.grid(column=0, sticky=N)
#c3.grid(column=0, sticky=N)

a1 = Checkbutton(root, text="Recuperação de Informação", variable=var4, onvalue=' Recuperação de Informação', offvalue='')
a2 = Checkbutton(root, text="Extração de Informação", variable=var5, onvalue=' Extração de Informação', offvalue='')
a3 = Checkbutton(root, text="Geração de Linguagem Natural", variable=var6, onvalue=' Geração de Linguagem Natural', offvalue='')
a4 = Checkbutton(root, text="Reconhecimento de Fala", variable=var7, onvalue=' Reconhecimento de Fala', offvalue='')
a5 = Checkbutton(root, text="Tradução de Linguagem", variable=var8, onvalue=' Tradução de Linguagem', offvalue='')
a6 = Checkbutton(root, text="Optical Character Recognition", variable=var9, onvalue=' OCR', offvalue='')
a7 = Checkbutton(root, text="Modelo de Recuperação Booleana", variable=var10, onvalue=7, offvalue='')
a8 = Checkbutton(root, text="Rankeamento e Atribuição de Peso", variable=var11, onvalue=7, offvalue='')
a9 = Checkbutton(root, text="Recuperação XML", variable=var12, onvalue=7, offvalue='')
a10 = Checkbutton(root, text="Extração de Relações Entre Termos", variable=var13, onvalue=7, offvalue='')
a11 = Checkbutton(root, text="Classificação de Documentos", variable=var14, onvalue=7, offvalue='')
a12 = Checkbutton(root, text="Extração de Dados", variable=var15, onvalue=7, offvalue='')
a13 = Checkbutton(root, text="Teorema de Bayes", variable=var16, onvalue=7, offvalue='')
var1.get()
a1.grid(row=0, column=1, sticky=W)
a2.grid(row=3, column=1, sticky=W)
a3.grid(row=7, column=1, sticky=W)
a4.grid(row=8, column=1, sticky=W)
a5.grid(row=9, column=1, sticky=W)
a6.grid(row=10, column=1, sticky=W)
a7.grid(row=0, column=2, sticky=W)
a8.grid(row=1, column=2, sticky=W)
a9.grid(row=2, column=2, sticky=W)
a10.grid(row=3, column=2, sticky=W)
a11.grid(row=4, column=2, sticky=W)
a12.grid(row=5, column=2, sticky=W)
a13.grid(row=4, column=3, sticky=W)
print('var1 dps', var1.get())
def recebeDataIHC(event):
    driver = init_driver()
    lookup(driver, var1.get()+var2.get()+var3.get()+var4.get()+var5.get()+var6.get()+var7.get()+var8.get()+var9.get()+'\n')
    time.sleep(5)
    driver.quit()

    print(x)
botao.bind('<Button-1>', recebeDataIHC)
'''
variavel = "comer coco"
driver = init_driver()
lookup(driver, "inteligencia artificial\n")
time.sleep(5)
driver.quit()
'''
root.mainloop()



