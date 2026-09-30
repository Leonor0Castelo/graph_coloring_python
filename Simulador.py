#!/usr/bin/env python
# coding: utf-8

# In[1]:


import coloration 
import cap 
import pop 
import grafos
import event
import individuals
import exprandom 
import math 
import random 
import matplotlib.pyplot as plt

def sim(ht,tri,tlim,tfil,G,k):
    
    c=cap.newc()
    population=pop.pop_inicial(G,k)
    ct=0
    c=cap.addE(c,event.evt(ct+tfil,"sel",population))
    
    for ind in pop.lista_ind(population):
        c=cap.addE(c,event.evt(ct+exprandom.exprandom(tri),"ev",ind))
        c=cap.addE(c,event.evt(ct+exprandom.exprandom(tlim),"av",ind))
        
    xtrace = [0]
    ytrace = [k]
    
    while ct<=ht:
        ce=cap.nextE(c)
        ct=event.time(ce)
        ck=event.kind(ce)
        ci=event.individual(ce)
        if ck=="av" and pop.existe_ind(population,ci):
            A=individuals.coe_adapt(G,ci)
            I=individuals.idade_ind(ci,ct)
            q=1-(2/math.pi)*math.atan((1+A)**(1+(8/(1+I))))
            l = random.random()
            if l<=q:
                pop1=pop.del_ind(population,ci)
            else:
                c=cap.addE(c,event.evt(ct+exprandom.exprandom(tlim),"av",ci))
                
        elif ck=="ev" and pop.existe_ind(population,ci):
            L=pop.num_ind(population)            
            m=1/(1+(math.e)**((k-L)/10))
            n=random.random()
            if n<m:
                ind2=individuals.mutacao_ind(G,ci,population)
                if ind2==ci:
                    c=cap.addE(c,event.evt(ct+exprandom.exprandom(tri),"ev",ci))
                else:
                    population=pop.del_ind(population,ci)
                    population=pop.add_ind(population,ind2)
                    c=cap.addE(c,event.evt(ct+exprandom.exprandom(tri),"ev",ind2))
                    c=cap.addE(c,event.evt(ct+exprandom.exprandom(tlim),"av",ind2))
            else:
                ind3=individuals.criar_ind(G,ci,population,ct)
                c=cap.addE(c,event.evt(ct+exprandom.exprandom(tri),"ev",ci))
                c=cap.addE(c,event.evt(ct+exprandom.exprandom(tri),"ev",ind3))
                c=cap.addE(c,event.evt(ct+exprandom.exprandom(tlim),"av",ind3))
        else:
                population=pop.morte(G,population)
                while pop.num_ind(population)>3*k//2:
                    population=pop.morte1(G,population) 
                c=cap.addE(c,event.evt(ct+tfil,"sel",population))
        
        xtrace.append(ct)
        ytrace.append(pop.num_ind(population))
        c=cap.delE(c,ce)
        ce=cap.nextE(c)
        ct=event.time(ce)
        ck=event.kind(ce)
        ci=event.individual(ce)
        
    plt.plot(xtrace, ytrace)
    plt.xlabel('Tempo(ms)')
    plt.ylabel('Número de individuos')
    plt.title('População')
    plt.show()
    print(pop.melhor_ind(G,population))
    return coloration.num_cores(pop.melhor_ind(G,population))


# In[ ]:




