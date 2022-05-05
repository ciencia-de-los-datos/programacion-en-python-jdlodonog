"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from re import A

import numpy as np
#from numpy import append

"""
para probar las preguntas :
python3 tests.py 01

"""
with open("C:/Users/Usuario/Documents/GitHub/programacion-en-python-jdlodonog/data.csv", newline="") as file:
#with open("/tmp/data.csv", "r") as file:
        Datos = file.readlines()
Datos
#print(Datos[:2])
    # luego de asignar los datos, se hace a correspondiente limpieza de estos
Datos = [line.replace("\t", ",") for line in Datos] # reemplazo los \t por comas
#print(Datos[:2])
Datos = [line.replace("\n", "") for line in Datos] # reemplazo los \n por vacios
#print(Datos[:2])
Datos = [line.split(",") for line in Datos] #separo mis datos en columnas por las comas
#print(Datos[:2])

def pregunta_01():
            ## luego de cargados los datos, los abro y los cargo a la variable Datos
    with open("C:/Users/Usuario/Documents/GitHub/programacion-en-python-jdlodonog/data.csv", newline="") as file:
    #with open("/tmp/data.csv", "r") as file:
        Datos = file.readlines()
    Datos

    # luego de asignar los datos, se hace a correspondiente limpieza de estos
    Datos = [line.replace("\t", ",") for line in Datos] # reemplazo los \t por comas
    #print(Datos[:2])
    Datos = [line.replace("\n", "") for line in Datos] # reemplazo los \n por vacios
    #print(Datos[:2])
    Datos = [line.split(",") for line in Datos] #separo mis datos en columnas por las comas
    #print(Datos[:2])

    x=np.sum([int(i[1]) for i in Datos[0:]])

    z=0
    z=x
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return z


#print("Pregunta 2")

def pregunta_02():

    T=tuple()
    L = sorted(list(set([i[0] for i in Datos[0:]]))) #set para volervelo un arreglo y quitar duplicados, list para hacerlo más manejable y list para ordenarlo
    listaRespuesta=[]
    listaRespuesta2=[]
    #print(L)# Imprime la lista de las letras , entonces el for coge cada primer elemento que corresponde a las letras y los pone en un vector, 
        #Luego el set los rodena y elimina los elementos duplicados, y luego lo organiza con el sorted
    N = np.array([i[0] for i in Datos[0:]]) # array para volverlo un arreglo y trabajarlo como un vector
    #Coge cada uno de los elementos y los pone en un vector y luego con el Numpy los pone en una matriz

    #print(N)    

    #print(np.sum("A" == N))# Este coge y suma cada elemento de la lista 
    """
        for i in L:
        #Este np.sum( i == N) Coge cada elemento de la lista N y lo suma 
        print(np.sum(i == N))
    """

    for i in L:
        #print("{},{}".format(i,np.sum(i == N))) 
        x=0
        x=np.sum(i == N)     
        listaRespuesta2.append(x)
        
    listaRespuesta=list(zip(L,listaRespuesta2))
   # print("Lista respuesta")
    #print(listaRespuesta)
    #print(listaRespuesta2)
    #T=tuple(list(zip(L,listaRespuesta)))


    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return listaRespuesta

"""


L = sorted(list(set([i[0] for i in Datos[0:]]))) #set para volervelo un arreglo y quitar duplicados, list para hacerlo más manejable y list para ordenarlo
    #print(L)
N = np.array([i[0] for i in Datos[0:]]) # array para volverlo un arreglo y trabajarlo como un vector
    #print(N)
M = np.array([i[1] for i in Datos[0:]])
    #print(M)
listResp3=[]
auxListResp3=[]

for i in L:
        X = i == N
        Resultantes = M[X].astype(int)
        z=0
        z=np.sum(Resultantes)
        auxListResp3.append(z)

        print("{},{}".format(i,np.sum(Resultantes)))

listResp3=list(zip(L,auxListResp3))
print(listResp3)
"""

def pregunta_03():

    import numpy as np

    L = sorted(list(set([i[0] for i in Datos[0:]]))) #set para volervelo un arreglo y quitar duplicados, list para hacerlo más manejable y list para ordenarlo
    #print(L)
    N = np.array([i[0] for i in Datos[0:]]) # array para volverlo un arreglo y trabajarlo como un vector
    #print(N)
    M = np.array([i[1] for i in Datos[0:]])
    #print(M)
    listResp3=[]
    auxListResp3=[]

    for i in L:
        X = i == N
        Resultantes = M[X].astype(int)
        z=0
        z=np.sum(Resultantes)
        auxListResp3.append(z)

        #print("{},{}".format(i,np.sum(Resultantes)))

    listResp3=list(zip(L,auxListResp3))
    #print(listResp3)

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return listResp3


def pregunta_04():

    import numpy as np

    listResp4=[]
    auxListResp4=[]

    fechas = [i[2] for i in Datos[0:]]
    fechas = [line.split("-") for line in fechas]
    fechas

    meses = sorted(list(set([i[1] for i in fechas])))
    meses

    registros = np.array([i[1] for i in fechas])
    #registros

    for i in meses:
         #print("{},{}".format(i,np.sum(i == registros)))
         x=0
         x=np.sum(i == registros)
         auxListResp4.append(x)

    listResp4=list(zip(meses,auxListResp4))
    # print(listResp4)
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return  listResp4


def pregunta_05():
    listResp5=[]
    listMax=[]
    listMin=[]

    import numpy as np

    L = sorted(list(set([i[0] for i in Datos[0:]])))
    #print(L)

    T =np.array([i[0] for i in Datos[0:]])
    #print(T)

    N = np.array([i[1] for i in Datos[0:]])
    #print(N)

    for i in L:
        x = i == T
        Num = N[x].astype(int)
        Max = np.amax(Num)
        Min = np.amin(Num)
        #print("{},{},{}".format(i,Max,Min))
        listMax.append(Max)
        listMin.append(Min)
       
    listResp5=list(zip(L,listMax,listMin))
    #print("Lista respuesta 5")
    #print(listResp5)

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return listResp5


def pregunta_06():
    listResp6=[]
    listMax=[]
    listMin=[]

    #print("PREGUNTA 6")
    with open("C:/Users/Usuario/Documents/GitHub/programacion-en-python-jdlodonog/data.csv", newline="") as file:
        Datos2 = file.readlines()

    #Datos2 = [line.replace("\t", ";") for line in Datos2] # reemplazo los \t por comas

        #print(Datos2[:3])
        Datos2 = [line.replace("\n", "") for line in Datos2] # reemplazo los \n por vacios
        #print("")
        #print(Datos2[:3])
        Datos2 = [line.split("\t") for line in Datos2] #separ
        #print("")
        #print(Datos2[:3])


        import numpy as np
        m = ([i[4] for i in Datos2])

        m = [line.replace(":", "=") for line in m]
        m = [line.split(",") for line in m]

        lista = []

        for fila in m:
            for i in fila:
                lista.append(i)

        lista = [line.split("=") for line in lista]
        #print(lista[:2])


        U = sorted(list(set([i[0] for i in lista])))
        #U

        T = np.array([i[0] for i in lista])

        N = np.array([i[1] for i in lista])

        for i in U:
            x = i == T
            Num = N[x].astype(int)
            Max = np.amax(Num)
            Min = np.amin(Num)
            #print("{},{},{}".format(i,Min,Max))
            listMax.append(Max)
            listMin.append(Min)

        listResp6=list(zip(U,listMin,listMax))    
        #print(listResp6)        

    
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return listResp6


def pregunta_07():
    listResp7=[]
    auxList=[]
    auxNumero=[]
    #Falta organizarlo para mostrarlo en el return
    L = np.array([i[0] for i in Datos])
    N = np.array([i[1] for i in Datos])
    U = sorted(list(set([i[1] for i in Datos])))
    for i in U:
        x = i == N
        Letra = L[x].astype(str)
        #print((i,Letra.tolist()))
        auxNumero.append(int(i))
        auxList.append(Letra.tolist())
    
    listResp7=list(zip(auxNumero,auxList))
   # print(listResp7)

    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return listResp7


def pregunta_08():
    #Falta generarlo como una lista de tuplas para mandarlo por el return
    listResp8=[]
    auxList=[]
    auxNumero=[]

    col1 = [i[0] for i in Datos]
    #print(col1)
    col2 = [i[1] for i in Datos]
    #print(col1)
    Col_1_2 = np.array([col1,col2])
    #Col_1_2

    unicos = sorted(set(col2))

    for i in unicos:
        x = i == Col_1_2[1]
        letras = Col_1_2[0][x]
        z=sorted(set(letras.tolist()))
        auxList.append(z)
        auxNumero.append(int(i))
        #print((i,sorted(set(letras.tolist()))))

    listResp8=list(zip(auxNumero,auxList))
    #print(listResp8)
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return listResp8


def pregunta_09():
    #print("PREGUNTA 9")
    with open("C:/Users/Usuario/Documents/GitHub/programacion-en-python-jdlodonog/data.csv", newline="") as file:
        Datos2 = file.readlines()

    #Datos2 = [line.replace("\t", ";") for line in Datos2] # reemplazo los \t por comas

    #print(Datos2[:3])
    Datos2 = [line.replace("\n", "") for line in Datos2] # reemplazo los \n por vacios
    #print("")
    #print(Datos2[:3])
    Datos2 = [line.split("\t") for line in Datos2] #separ
    #print("")
    #print(Datos2[:3])


    import numpy as np
    listResp9=[]
    auxList=[]
    auxNumero=[]


    m = ([i[4] for i in Datos2])
    #print(m)

    m = [line.replace(":", "=") for line in m]
    m = [line.replace("\r", "") for line in m]
    m = [line.split(",") for line in m]

    lista = []

    for fila in m:
        #print(fila)
        for i in fila:
            #print(i[1])
            lista.append(i)

    lista = [line.split("=") for line in lista]   

    m = [i[0] for i in lista]
    m

    frec = []

    for i in m:
        frec.append(m.count(i))
        n = sorted(list(set(zip(m,frec))))

    for i in n:
        #print("{},{}".format(i[0],i[1]))
        auxList.append(i[0])
        auxNumero.append(int(i[1]))

    #aca lo tengo como una
    listResp9=list(zip(auxList,auxNumero))
    #print(listResp9)
    dict1=dict(listResp9)
    
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return dict1


def pregunta_10():
    
    with open("C:/Users/Usuario/Documents/GitHub/programacion-en-python-jdlodonog/data.csv", newline="") as file:
        Datos4 = file.readlines()

    Datos4 = [line.replace("\n", "") for line in Datos4] # reemplazo los \n por vacios
    Datos4 = [line.split("\t") for line in Datos4] #separ

    #print(Datos4[:4])
    #Lista de primera letra Mayuscula
    col1 = np.array([i[0] for i in Datos4])
    #print("col1")
    #print(col1[:4])

    #lista de letras minusculas
    col3 = [i[3] for i in Datos4]
    col3 = [line.replace(",", "") for line in col3]
    #print("col3")
    #print(col3[:4])


    lista_b = []
    #cuenta las letras minusculas
    for i in col3:
        lista_b.append(len(i))

    #print("lista b")
    #print(lista_b[:4])
    #separo las claves
    col4 = [i[4] for i in Datos4]
    col4 = [line.replace("\r", "") for line in col4]
    col4 = [line.split(",") for line in col4]
    #print("col4")
    #print(col4[:4])

    lista_n = []
    #calculo en numero de elementos 
    for l in col4:
     lista_n.append(len(l))

    #print("LISTA_N")
    #print(lista_n[:4])

    z = list(zip(col1,lista_b,lista_n))
    #print("Z")
    #print(z)

    """
    
    for i in z:
        print("{},{},{}".format(i[0],i[1],i[2]))
    """

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return z


def pregunta_11():
    #revisarlo todo
    with open("C:/Users/Usuario/Documents/GitHub/programacion-en-python-jdlodonog/data.csv", newline="") as file:
        Datos = file.readlines()

        Datos = [line.replace("\n", "") for line in Datos] # reemplazo los \n por vacios
        Datos = [line.split("\t") for line in Datos] #separ

    #----------------------------------------------------
    Letras = []
    Numeros = []
    listResp11=[]
    auxList=[]
    auxNumero=[]

    for i in Datos:
        Letras.append(i[3])

    for i in Datos:
      Numeros.append(i[1])
    #----------------------------------------------------------

    Sep = []
    #Separa las letras de la columna 3
    Separados = [line.split(",") for line in Letras]
    #print("Separados")
    #print(Separados)

    #genera un listado concada una de las letras
    for i in Separados:
        for j in i:
         Sep.append(j)
         
    #print("Sep")
    #print(Sep)
    #-----------------------------------------------------------
    #determina el tamaño de cada uno,se puede utilizar como indice 
    x = [len(i) for i in Separados]
    #print("X")
    #print(x)

    # saco la lista de numeros
    y = [[i] for i in Numeros]
    #print("y")
    #print(y)

    Numeros_repetido = []
    #para cada elemento en el rango del tamaño de X, en este caso 
    for i in range(len(x)):
     #print(y[i])
     #print(x[i])
     Numeros_repetido.append((y[i]*x[i]))
    #print("Numeros_repetido")
    #print(Numeros_repetido)

    Num_sep = []
    for i in Numeros_repetido:
        for j in i:
         Num_sep.append(j)
    #print("Num_sep")     
    #print(Num_sep)

    #-------------------------------------------------------
    import numpy as np

    L = sorted(set(Sep))
    #print(L)
    N = np.array(Sep) # array para volverlo un arreglo y trabajarlo como un vector
    #print(N)
    M = np.array(Num_sep)
    #print(M)


    for i in L:
        X = i == N
        Resultantes = M[X].astype(int)
        z=np.sum(Resultantes)
        auxList.append(i)
        auxNumero.append(z)
        #print("{},{}".format(i,np.sum(Resultantes)))
    
        #aca lo tengo como una
    listResp11=list(zip(auxList,auxNumero))
    #print(listResp11)
    dict11=dict(listResp11)

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return dict11


def pregunta_12():

    print("")
    print("Pregunta 12")

   
    with open("C:/Users/Usuario/Documents/GitHub/programacion-en-python-jdlodonog/data.csv", newline="") as file:
         Datos2 = file.readlines()

    #Datos2 = [line.replace("\t", ";") for line in Datos2] # reemplazo los \t por comas

    #print(Datos2[:3])
    Datos2 = [line.replace("\n", "") for line in Datos2] # reemplazo los \n por vacios
    print("")
    print(Datos2[:3])
    Datos2 = [line.replace("\r", "") for line in Datos2] 
    Datos2 = [line.split("\t") for line in Datos2] #separ
    print("")
    print(Datos2[:3])

    x=[i[4] for i in Datos2]
    l=[i[0] for i in Datos2]
    print(x[:3])
    xz=[line.split(",") for line in x]
    print("XY")
    print(xz[:3])

    auxNumero=[]
    auxNum=[]
    
    for i in xz:
        auxSuma=0
        auxlista=[]
        for j in i:
            xyz=j[4:]
            xyz=int(xyz)
            
            auxlista.append(xyz)
            #print(xyz)
            #print("suma")
            #print(auxlista)
            #print(sum(auxlista))
        auxNumero.append(sum(auxlista))    
        #print("")
        #print(auxNumero)

    print(len(auxNumero))  
    print(auxNumero)  
    #ya tengo cada suma tengo que poner el resoltado 
    print("")
    print(l)

    l2=sorted(set(l))
    print("")
    print(l2)
    
   
    print("")
    auxRespuesta=[]
    for letra in l2:   
        print("letra de busqueda")     
        print(letra)
        contador=0
        auxNum=[]
        for j in l:
            
            if j== letra:
                print("letra "+j)
                #print(j)
                print("indice " + str(contador))
                # z=l.index(j)
               # print(contador)
                print("valor a sumar")
                print(auxNumero[contador])
                auxNum.append(auxNumero[contador])
                print("elemento para la suma")
                print(auxNum)
            contador+=1
        auxRespuesta.append(sum(auxNum))


    print(auxRespuesta)
    listResp12=list(zip(l2,auxRespuesta))
    #print(listResp12)
    dict12=dict(listResp12)

    """
   
    for i in l2:
        X = i == l
        Resultantes = auxNumero[X].astype(int)
        z=np.sum(Resultantes)
        print(i)
        print(z)
        
        #auxList.append(i)
        #auxNumero.append(z)
        #print("{},{}".format(i,np.sum(Resultantes)))
    
        #aca lo tengo como una
    #listResp11=list(zip(auxList,auxNumero))
    """

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return dict12
