#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import individuals
import coloration 
import grafos 

#funções ligadas à População

def empty_pop():
    return []


def pop_inicial(G,k):
    pop1=empty_pop()
    i=0
    for i in range(k):
        new_ind=individuals.novo_ind(G,pop1,0)
    return pop1

def num_ind(pop1):
    return len(pop1)

def ultimo_num(pop1):
    if len(pop1)==0:
        return 0
    else:
        return pop1[-1][-1]


def lista_ind(pop1):
    return pop1

def add_ind(pop1, ind):
    if pop1 is None:
        pop1=[]
    pop1.append(ind)
    return pop1

def del_ind(pop1,ind):
    new_pop=[]
    for individual in pop1:
        if individual!=ind:
            new_pop.append(individual)
    return new_pop
    
def existe_ind(pop1,ind):             
    found=False
    i=0
    while i<len(pop1) and not found:
        ind1=pop1[i]
        if individuals.n_ind(ind1)==individuals.n_ind(ind):
            found=True
        i=i+1
    return found

def melhor_ind(G,pop1):
    if len(pop1) == 0:
        return None
    best_ind=pop1[0] 
    best_adapt=individuals.coe_adapt(G,best_ind)
    for ind in pop1[1:]:
        cur_coe_adapt=individuals.coe_adapt(G,ind) 
        if cur_coe_adapt>best_adapt: 
            best_ind=ind
            best_adapt=cur_coe_adapt

    return best_ind
    

def morte(G, pop1):
    res=empty_pop()
    for i in range(len(pop1)):
        if coloration.viable_col(G,pop1[i]):  
            res=add_ind(res,pop1[i])  
    return res  

def morte1(G, pop):
    pop1=pop[:]
    coe_values=lista_coe(G, pop1)
    min_coe=bubble_sort(coe_values)[0]
    found=False
    i=0
    while i < len(pop1) and not found:
        if individuals.coe_adapt(G, pop1[i])==min_coe:
            pop1=del_ind(pop1, pop1[i])
            found=True
        else:
            i=i+1
    return pop1


def lista_coe(G,pop):
    list1=[]
    i=0
    for i in range(len(pop)):
        list1=list1+[individuals.coe_adapt(G,pop[i])]
    return list1



def bubble_sort(w):
    n=len(w)
    for i in range(n):
        for j in range(0,n-i-1):
            if w[j]>w[j+1]:
                w[j],w[j+1]=w[j+1],w[j]
    return w