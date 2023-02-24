def C1():

   

    s=input("Ingrese el numero binario deseado para C1 \n")

    lista = list(s)

    for i in range(len(lista)):
        if lista[i] == "1":
            lista[i]="0"   
        else:
            lista[i]="1"
    

    
    print("En C1",lista)


def C2():
    s=input("Ingrese el numero binario deseado para C2 \n")

    lista = list(s)

    for i in range(len(lista)):
        if lista[i] == "1":
            lista[i]="0"   
        else:
            lista[i]="1"
        
    resp = ''.join(lista)
    decimal = int(resp, 2)
    decimal += 1

    lista = list(bin(decimal)[2:])

    print("En C2",lista)
