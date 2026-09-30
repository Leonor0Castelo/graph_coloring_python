#!/usr/bin/env python
# coding: utf-8


#Funções ligadas ao individuo

import pop 
import coloration
import random
import grafos


def novo_ind(G,pop1,tempo):
    l=pop.ultimo_num(pop1)+1
    res=[coloration.col(G),tempo,l]
    pop1=pop.add_ind(pop1,res)
    return res

def col_ind(ind):
    return ind[0]

def n_ind(ind):         #ler o número que identifica cada individuo
    return ind[2]

def idade_ind(ind,ct):   #idade do individuo
    return ct-ind[1]

def col_ind(ind):   #coloração do indivíduo
    return ind[0]

def coe_adapt(G,ind):    #coeficiente de adaptação
    if not(coloration.viable_col(G,ind)):
        return 1/(1+coloration.def_col_count(G,ind))
    else:
        return grafos.dim(G)/coloration.num_cores(ind)

def criar_ind(G,ind,pop1,ct):
    if pop1==[]:
        pop1.ultimo_num(pop1)==0
    i=random.randrange(len(ind[0]))
    r=random.choice(ind[0])
    ind1 =[[], 0, 0]
    ind1[0]=ind[0][:i]+[r]+ind[0][i+1:]
    ind1[1]=ct
    ind1[2]=pop.ultimo_num(pop1)+1
    pop1=pop.add_ind(pop1,ind1)
    return ind1

def mutacao_ind(G,ind,pop):
    i=random.randrange(len(ind[0]))
    k=random.choice(ind[0])
    ind1=[[],0,0]
    ind1[0]=ind[0][:i]+[k]+ind[0][i+1:]
    ind1[1]=ind[1]
    ind1[2]=ind[2]
    if coe_adapt(G,ind1)>coe_adapt(G,ind):
        return ind1
    else:
        return ind