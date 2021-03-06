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

"""
para probar las preguntas :
python3 tests.py 01

"""
with open("data.csv", "r") as file:
    #with open("/tmp/data.csv", "r") as file: #para leer directamente en colab
    # with open("C:/Users/Usuario/Documents/GitHub/programacion-en-python-jdlodonog/data.csv", newline="") as file: # para leer en directorio local desde el github
    # with open("https://github.com/ciencia-de-los-datos/programacion-en-python-jdlodonog/blob/main/data.csv", newline="") as file: #pare leer directamente en la web
    Datos = file.readlines()
Datos

Datos = [line.replace("\t", ",") for line in Datos] # reemplazo los \t por comas
Datos = [line.replace("\n", "") for line in Datos] # reemplazo los \n por vacios

def pregunta_01():
            ## luego de cargados los datos, los abro y los cargo a la variable Datos
    with open("data.csv", "r") as file:
    #with open("/tmp/data.csv", "r") as file: #para leer directamente en colab
    # with open("C:/Users/Usuario/Documents/GitHub/programacion-en-python-jdlodonog/data.csv", newline="") as file: # para leer en directorio local desde el github
    # with open("https://github.com/ciencia-de-los-datos/programacion-en-python-jdlodonog/blob/main/data.csv", newline="") as file: #pare leer directamente en la web
        Datos = file.readlines()
    Datos

    # luego de asignar los datos, se hace a correspondiente limpieza de estos
    Datos = [line.replace("\t", ",") for line in Datos] # reemplazo los \t por comas
    #print(Datos[:2])
    Datos = [line.replace("\n", "") for line in Datos] # reemplazo los \n por vacios
    #print(Datos[:2])
    Datos = [line.split(",") for line in Datos] #separo mis datos en columnas por las comas
    #print(Datos[:2])

    
    result = sum([int(x[1]) for x in Datos])
           
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return result


#print("Pregunta 2")

def pregunta_02():
    from collections import Counter

    aux = [letra[0] for letra in Datos]
    print(aux)
    counter = list(Counter(aux).items()) 
    print(counter)
    counter.sort()
    print(counter)
    letra=[]
    numero=[]

    for item in counter: 
        print("{},{}".format(item[0],item[1]))    
        #print("{},{}".format(i,np.sum(i == N))) 
        letra.append(item[0])
        numero.append(item[1])
           
       # listaRespuesta2.append(item[1])
        
    listaRespuesta=list(zip(letra,numero)) 

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


def pregunta_03():
    with open("data.csv", "r") as file:
         Datos = file.readlines()
    Datos   
    Datos = [line.replace("\t", ",") for line in Datos] 
    Datos = [line.replace("\n", "") for line in Datos]
    
    
    
    letters_list = ["A", "B", "C", "D", "E"]
    #print(Datos[0:])
    #letters_list= sorted(list(set([i[0] for i in Datos[0:]])))     
    print(letters_list)
    sumaLetras=0
    valor=0

    vfinal=[]
    vfinal2=[]
    letra=[]
    for i in letters_list:  
        print("Letra " + i)  
        sumaLetras=0
        vfinal2=[]
        for j in Datos:  
            #print(j)
            #print(j[0]+" - "+ j[2])            
            
            if i== j[0]:
                #print("entre en el if")
                #valor= int(float(j[1]))
                vfinal2.append(j[2])
                #print(i +  "= " + j[2] ) 
                #print(str(valor))
                #sumaLetras+= valor     
                
                #print( i+ " " + str(sumaLetras))           
                #print("Letra "+ str(i) + " valor= "+ str(sumaLetras))
        print("imprimeindo valor final2")
        print(vfinal2)
        x=0
        b=[]
        b= [int(x[0]) for x in vfinal2] 
        z=sum(b)
        #print(z)
        #print("  ") 
        vfinal.append(z)
        print(i +" "+ str(z)) 
    print(vfinal)  
   
    print("Letra " +  str(i) + " " + str(z))      

    print(vfinal)

    listaRespuesta3=list(zip(letters_list, vfinal))
    print(listaRespuesta3)    
    
    print("lista")
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
    return listaRespuesta3


def pregunta_04():
    from collections import Counter
    from datetime import datetime
    with open("data.csv", "r") as file:
         Datos = file.readlines()
     
    Datos = [line.replace("\t", ",") for line in Datos] 
    Datos = [line.replace("\n", "") for line in Datos]
    print(Datos[:3])
    suma = Counter()
    #El Counter puede ir agregando elementos  usando formas de diccionarios 

    meses=[]
    numeros=[]
    
    for j in Datos: 
        #print(j)
        y=j[9:11]
        #print(y)       
        #print(item1[3][6:])
        
        month = j[9:11]
        #print("Mes"+ month)
        #print(month)
        suma[month] +=1
        #print(suma)

    suma=list(suma.items())
    suma.sort()


    for item in suma: 
        print("{},{}".format(item[0],item[1]))   
        meses.append(item[0])    
        numeros.append(item[1])  

    listResp4=list(zip(meses,numeros))

    
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
    
    datos = []
    final = []
    letras=[]
    listResp5=[]
    max1=[]
    min1=[]
    #Coge el numero y la letra y los pone en un una lista

    [datos.append({letra[0]:int(letra[2])}) for letra in Datos] #En esta parte lo puse en un diccionario con key letra y value numero 
    
    #print(datos)
    
    #Para cada elemento en el diccionario si k esta en d, aca tiene que coger cada letra del diccionario 
    dict_letras  = {
        k: [d.get(k) for d in datos if k in d]
        for k in set().union(*datos)
        }
    print(list((dict_letras)))

    [final.append([item[0], max(item[1]), min(item[1])]) for item in dict_letras.items()]
    final.sort()


    for item in final: 
        print("{},{},{}".format(item[0],item[1],item[2]))
        letras.append(item[0])
        max1.append(item[1])
        min1.append(item[2])
        
    listResp5=list(zip(letras,max1,min1))

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
    with open("data.csv", "r") as file:
        data2= file.readlines()
    data2

    data2 = [line.replace("\t", " ") for line in data2]
    data2 = [line.replace("\r\n", "") for line in data2]
    data2 = [line.split(" ") for line in data2]#se hace para separ bien los datos 


    #print(data2[:3])
    dataSlice5 = [item[4] for item in data2]
    #print(dataSlice5)

    aux = []
    datos = []
    final = []

    letra=[]
    max1=[]
    min1=[]

    for linea in dataSlice5:
        linea = linea.split(',')
        aux.append(linea)
        for item in linea:
            item = item.split(':')
            #print(item)
            datos.append({item[0]:int(item[1])})

    dict_letras  = {
        k: [d.get(k) for d in datos if k in d]
        for k in set().union(*datos)
        }   

    [final.append([item[0],min(item[1]), max(item[1])]) for item in dict_letras.items()]
    final.sort()

    for item in final: 
        print("{},{},{}".format(item[0],item[1],item[2]))
        letra.append(item[0])
        max1.append(item[1])    
        min1.append(item[2])


    listResp6=list(zip(letra,max1,min1))
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
    with open("data.csv", "r") as file:
        data2= file.readlines()
    data2


    data2 = [line.replace("\t", " ") for line in data2]
    data2 = [line.replace("\r\n", "") for line in data2]
    data2 = [line.split(" ") for line in data2]#se hace para separ bien los datos 

    datos = []

    numero=[]
    lista=[]
    [datos.append({letra[1]:letra[0]}) for letra in data2] 

    dict_letras  = {
        k: [d.get(k) for d in datos if k in d]
        for k in set().union(*datos)
    }

    result = sorted(tuple(dict_letras.items()))

    for item in result: 
        print(item)
        numero.append(int(item[0]))
        lista.append(item[1])

    listResp7=list(zip(numero,lista))
    print(listResp7)


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
    with open("data.csv", "r") as file:
        data2= file.readlines()
    data2

    data2 = [line.replace("\t", " ") for line in data2]
    data2 = [line.replace("\r\n", "") for line in data2]
    data2 = [line.split(" ") for line in data2]#se hace para separ bien los datos 

    datos = []
    numero=[]
    lista=[]

    #crea un diccionario con clave el numero y como valor la letra
    [datos.append({letra[1]:letra[0]}) for letra in data2] 

    dict_letras  = {
        k: [d.get(k) for d in datos if k in d]
        for k in set().union(*datos)
    }

    result = sorted(tuple(dict_letras.items()))

    for item in result: 
        print((item[0],sorted(set(item[1]))))
        numero.append(int(item[0]))
        lista.append(sorted(set(item[1])))

    listResp8=list(zip(numero,lista))
    print(listResp8)
    
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
    with open("data.csv", "r") as file:
        data2= file.readlines()
    data2
    
    data2 = [line.replace("\t", " ") for line in data2]
    data2 = [line.replace("\r\n", "") for line in data2]
    data2 = [line.split(" ") for line in data2]#se hace para separ bien los datos 


    #print(data2[:3])
    dataSlice5 = [item[4] for item in data2]
    #print(dataSlice5[:3])

    aux = []
    datos = []
    letra=[]
    numero=[]
  

    for linea in dataSlice5:
        linea = linea.split(',')
        aux.append(linea)
        for item in linea:
            item = item.split(':')
            #print(item)
            datos.append({item[0]:int(item[1])})

    dict_letras  = {
        k: [d.get(k) for d in datos if k in d]
        for k in set().union(*datos)
        }  

    dict_letras

    result = []
    for item in dict_letras.items():
        result.append((item[0], len(item[1])))

    result.sort()
    for item in result:
        print("{},{}".format(item[0],item[1]))
        letra.append(item[0])
        numero.append(item[1])

    
    listResp9=list(zip(letra,numero))
    print(listResp9)
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
    with open("data.csv", "r") as file:
        data2= file.readlines()
    data2

    data2 = [line.replace("\t", " ") for line in data2]
    data2 = [line.replace("\r\n", "") for line in data2]
    data = [line.split(" ") for line in data2]#se hace para separ bien los datos 


    dataSlice = [item[3] for item in data ]
    dataSlice4 = [line.split(',') for line in dataSlice]

    dataSlice = [item[4] for item in data ]
    dataSlice5 = [line.split(',') for line in dataSlice]

    letra=[]
    num1=[]
    num2=[]


    for item, data4, data5 in zip(data, dataSlice4, dataSlice5): 
        print((item[0], len(data4), len(data5)))
        letra.append(item[0])
        num1.append(len(data4))
        num2.append(len(data5))

    listResp10=list(zip(letra,num1,num2))


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
    return listResp10

def pregunta_11():
    with open("data.csv", "r") as file:
        data2= file.readlines()
    data2

    data2 = [line.replace("\t", " ") for line in data2]
    data2 = [line.replace("\r\n", "") for line in data2]
    data = [line.split(" ") for line in data2]#se hace para separ bien los datos 


    dataSlice = [item[3] for item in data ]
    dataSlice4 = [line.split(',') for line in dataSlice]

    dataSlice = [item[4] for item in data ]
    dataSlice5 = [line.split(',') for line in dataSlice]

    letra11=[]
    num1=[]
    
    dataSlice = [item[3] for item in data ]
    dataSlice4 = [line.split(',') for line in dataSlice]

    from collections import Counter  
    suma = Counter() 
    
    for valor, letras in zip(data, dataSlice4): 
        for letra in letras:
            suma[letra] += int(valor[1])

    suma=list(suma.items())
    suma.sort()

    for item in suma: 
        print("{},{}".format(item[0],item[1]))
        letra11.append(item[0])
        num1.append(item[1])

 
    listResp11=list(zip(letra11,num1))
    print(listResp11)
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

    with open("data.csv", "r") as file:
        data2= file.readlines()
    Datos2=data2

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
