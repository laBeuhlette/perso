import time
import random


liste1=[12,56,54,98,23,87,45,654,123,65,748,654,123,6,54,123]




def petit (liste):
    test=liste[0]
    for i in liste:
        if i<test:
            test=i
    return test

def grand (liste):
    test=liste[0]
    for i in liste:
        if i>test:
            test=i
    return test

def triselect (liste):
    liste2=[]
    for i in range(0,len(liste)):
        elem=petit(liste)
        liste.remove(elem)
        liste2.append(elem)
    return liste2

def listal ():
    taille = random.randint(0,15)
    liste=[]
    for i in range(0,taille):
        rand = random.randint(0,100)
        liste.append(rand)
    return liste

def concat(liste1,liste2):
    for i in liste2:
        liste1.append(i)
    return liste1
    

def pivote (obj,liste):
    l1=[]
    l2=[]
    L=[]
    for i in liste:
        if i<obj:
            l1.append(i)
        elif i>obj:
            l2.append(i)
    L=concat(L,l1)
    L.append(obj)
    L=concat(L,l2)
    return L

def tripiv (liste):
    for i in liste:
        liste=pivote(i,liste)
        print(liste)
    return liste

print(tripiv(listal()))
