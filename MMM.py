a=int(input("Introduzca el número de entradas que desea hacer."))
b=0
d=[]
f=0
Mayor=0
Menor=1


while (b<a):
    b=b+1
    c=int(input("Valor:"))

    if (Mayor < c):
        Mayor=c
    else:
        Mayor=Mayor
        
    f=f+c
    d.append(c)
    e=len(d)

def Media():
    media=f/e
    print("La media es: "+str(media))
    
def Mediana():

    con=Mayor
    Ord=[]
    Des=d
    Ord.insert(0,Mayor)
    g=0
    Mediana=0
    Inicio=0
    while (e>g):

        con=con-1
        contador=d.count(con)
        g=len(Ord)
        if(contador>0):
            if(contador>1):
                Ord.insert(0,con)
                Des.remove(con)
                con=con+1
            else:
                Ord.insert(0,con)
        

            
    if(g%2==0):
        g=(g/2)-1;
        Mediana=((Ord[int(g)]+Ord[int(g)+1])/2)
    else:
        g=(g/2)-1
        Mediana=(Ord[int(g+0.5)])
        
    print("El orden es: "+str(Ord))
    print("La mediana: "+str(Mediana))
    
def Moda():
    for hola in d:
        hola




Media()
Mediana()
Moda()
