#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def newgraph(N):
    return [N,[]]

def edge_index(g,x,y):
    i=0
    notFound=True
    while notFound and i<len(g[1]):
        notFound=(g[1][i]==(x,y) or g[1][i]==(y,x))
        i=i+1
    if not notFound:
        i=i-1
    return i

def addedge(g,x,y):
    i=edge_index(g,x,y)
    if i==len(g[1]):
        return [g[0],g[1]+[(x,y)]+[(y,x)]]
    else:
        return g

def deledge(g,x,y):
    i=edge_index(g,x,y)
    return [g[0],g[1][:i-1]+[1][i:]]

def dim(g):
    return g[0]

def graphQ(g):
    if type(g)==list:
        if len(g)==2:
            if type(g[0])==int:
                if type(g[1])==list:
                    i=0
                    notFound=True
                    while notFound and i<len(g[1]):
                        notFound=len(g[1][i])==2
                        i=i+1
                    if notFound:
                        return len(list_nodes(g)<=g[0])
                    else:
                        return False
                    
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    

def list_nodes(g):
    l=[]
    for e in g[l]:
        if not g[0] in l:
            l=l+[g[0]]
        if not g[l] in l:
            l=l+[g[1]]
    return l
    
def emptyQ(g):
    return len(g[1])==0

def edge(g,x,y):
    return (x, y) in g[1] or (y, x) in g[1]

