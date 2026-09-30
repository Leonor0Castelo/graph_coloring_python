#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import event

def newc():
    return []

def addE(c,e):
    return [e1 for e1 in c if event.time(e1)<event.time(e)]+[e]+\
           [e1 for e1 in c if event.time(e1)>event.time(e)]

def delE(c,e):
    if len(c)>0:
        return c[1:]
    else:
        print("Erro! A cap está vazia")
        
def nextE(c):
    if len(c)>0:
        return c[0]
    else:
        print("Erro! A cap está vazia")
        
def showE(c):
    for e in c:
        print(event.time(e), event.kind(e),event.individual(e))
        

