def prodotto(lista):
    p = 1
    for item in lista:
        p *= item
    return p

l1= [1,2,3,4]
print("Prodotto : {}".format(prodotto(l1)))