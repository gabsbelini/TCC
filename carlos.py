entrada = open('entrada.txt', 'r')
saida = open('saida.txt', 'w')
eof = 10.52
lista = []
while isinstance(eof, float):
    fh = entrada.readline()
    if '.' in fh:
        eof = float(fh)
        lista.append(eof)
    else:
        eof = int(fh)
listaResultado=[]
for x in lista:
    if lista.index(x)+1 < (len(lista)):
        dafrente = lista[lista.index(x)+1]
        #print('daf',dafrente)
        resultado = dafrente - x
        listaResultado.append(resultado)
print(lista)


for x in listaResultado:
    if listaResultado.index(x)+1 < len(listaResultado):
        if x>0:
            print('subiu')
        else:
            print('desceu')
