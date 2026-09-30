#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import individuals 
import grafos 

#coloração

#coloração

def col(G):
    N=grafos.dim(G)
    res=[]
    i=1
    while i<N+1:
        res=res+[i]
        i=i+1
    return res
        
#Uma função que vai  ver se a coloração(col) é possível

def viable_col(G,ind):
    found=False
    col=individuals.col_ind(ind)
    x=0
    while x<len(col) and not(found):
        y=1
        while y<len(col) and not(found):
            if grafos.edge(G,x,y) and col[x]==col[y]:
                found=True
            else:
                    y=y+1
        x=x+1
    return not(found)

                   
def procura(n,w):
    found=False
    i=0
    while i<len(w) and not found:
        if w[i]==n:
            found=True
        i=i+1
 
    return found
                   
#função que vai contar o número de cores do grafo G

def num_cores(ind):
    mylist=[]
    res=len(mylist)
    h=individuals.col_ind(ind)
    i=0
    while i<len(h):
        if not procura(h[i],mylist):
            mylist=mylist+[h[i]]
            res=res+1
        i=i+1
        mylist=mylist
        
    return res
                   

#função que vai ver o número de defeitos de coloração

def def_col_count(G,ind):
    m=individuals.col_ind(ind)
    if viable_col(G,ind):
        return 0
    else:
        res=0
        i=0
        for i in range(len(m)-1): #vai averiguar se a cor de dois nós ligados é igual e, se for, o numero de defeitos aumenta
            if m[i]==m[i+1]:
                res=res+1
            res=res
        return res
            