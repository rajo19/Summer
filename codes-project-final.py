f=open('bless.txt',"r")
lines=f.readlines()
result=[]
for x in lines:
    result.append(x.split(';')[0])
f.close()

f=open('bless.txt',"r")
lines=f.readlines()
result1=[]
for x in lines:
    result1.append(x.split(';')[1])
f.close()

import networkx as nx
import matplotlib.pyplot as plt
import math

g = nx.read_edgelist('./LMI_w1000_p1000.txt',
  data=(('weight',float),), create_using=nx.Graph())


x=0
k=0
y=0
c=0
z1=[]
j1=[]
for j in result:
    for (u, v, wt) in g.edges.data('weight'):
        if (j in u):
            a=list(g.neighbors(u))
            for i in a:
                x=x+g.degree(i)
                k=k+1
        if(j in v):
            b=list(g.neighbors(v))
            for l in b:
                y=y+g.degree(l)
                c=c+1
    z=(x+y)/(c+k)
    z1.append(z)
    j1.append(j)

x=0
k=0
y=0
c=0
z2=[]
j2=[]
for j in result1:
    for (u, v, wt) in g.edges.data('weight'):
        if (j in u):
            a=list(g.neighbors(u))
            for i in a:
                x=x+g.degree(i)
                k=k+1
        if(j in v):
            b=list(g.neighbors(v))
            for l in b:
                y=y+g.degree(l)
                c=c+1
    z=(x+y)/(c+k)
    z2.append(z)
    j2.append(j)

x=[]
y=[]
for k in range(len(result)):
    j=result[k]
    i=result1[k]
    for (u, v, wt) in g.edges.data('weight'):
        if (j in u):
            a=list(g.neighbors(u))
    b=[]
    for (u, v, wt) in g.edges.data('weight'):
        if (i in u):
            b=list(g.neighbors(u))
    c=[]
    for i in a:
        for j in b:
            if (i==j):
                c.append(i)
    xl=len(a)-len(c)
    yl=len(b)-len(c)
    x.append(xl)
    y.append(yl)

s1=[]
s2=[]
for k in range(len(result)):
    j=result[k]
    i=result1[k]
    for (u, v, wt) in g.edges.data('weight'):
        if (j in u):
            a=list(g.neighbors(u))
    ea=0
    for c in a:
        ea=len(list(g.neighbors(c)))+ea
    da=0
    for c in a:
        da+=g.degree(c)*math.log(g.degree(c))
    sa=math.log(2*ea)-1/2/ea*da
    b=[]
    for (u, v, wt) in g.edges.data('weight'):
        if (i in u):
            b=list(g.neighbors(u))
    eb=0
    for c in b:
        eb=g.degree(c)+eb
    db=0
    for c in b:
        db+=g.degree(c)*math.log(g.degree(c))
    sb=math.log(2*eb)-1/2/eb*db
    s1.append(sa)
    s2.append(sb)

import pandas
df = pandas.DataFrame(data={"A":j1,"A1":z1,"A2":x,"A3":x,"A4":s1,"B":j2,"B1":z2,"B2":y,"B3":y,"B4":s2})
df.to_csv("./final.csv", sep=',',index=False)
