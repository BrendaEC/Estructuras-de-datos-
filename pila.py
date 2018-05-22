from heapq import heappop, heappush
from copy import deepcopy

#FILA
class Fila:
    def __init__(self):
        self.fila = []
    def obtener(self):
        return self.fila.pop(0)
    def meter(self,e):
        self.fila.append(e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)



#PILA
class Pila:
    def __init__(self):
        self.pila = []
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)



class Grafo:
    def __init__(self):
        self.V = set()
        self.E = dict()
        self.vecinos = dict()
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos:
            self.vecinos[v] = set()
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp




#busqueda por profundidad
def DFS(self, ni):
    visitados = []
    f = Pila()
    f.meter(ni)
    while (f.longitud > 0):
        na = f.obtener()
        visitados.append(na)
        ln = g.vecinos[na]
        for nodo in ln:
            if nodo not in visitados:
                f.meter(nodo)
    return visitados


#busqueda por amplitud
def BFS(self, ni):
    visitados = []
    f = Fila()
    f.meter(ni)
    while (f.longitud > 0):
        na = f.obtener()
        visitados.append(na)
        ln = g.vecinos[na]
        for nodo in ln:
            if nodo not in visitados:
                f.meter(nodo)
    return visitados


# Dijkstra's algorithm
def shortest(self, v):
    q = [(0, v,())]
    dist = dict()
    visited = set()
    while len(q) > 0:
        (l, u, p) = heappop(q)
        if u not in visited:
            visited.add(u)
            dist[u] = (l, u, list(flatten(p))[::-1] + [u])
            p = (u, p)
        for n in self.vecinos[u]:
                if n not in visited:
                    el = self.E[(u, n)]
                    heappush(q, (l + el, n,p))
    return dist


def kruskal(self):
    e = deepcopy(self.E)
    arbol = Grafo()
    peso = 0
    comp = dict()
    t = sorted(e.keys(), key=lambda k: e[k], reverse=True)
    nuevo = set()
    while len(t) > 0 and len(nuevo) < len(self.V):
        # print(len(t))
        arista = t.pop()
        w = e[arista]
        del e[arista]
        (u, v) = arista
        c = comp.get(v, {v})
        if u not in c:
            # print('u ',u, 'v ',v ,'c ', c)
            arbol.conecta(u, v, w)
            peso += w
            nuevo = c.union(comp.get(u, {u}))
            for i in nuevo:
                comp[i] = nuevo
    print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
    return arbol

def vecinoMasCercano(self):
    ni = random.choice(list(self.V))
    result = [ni]
    while len(result) < len(self.V):
        ln = set(self.vecinos[ni])
        le = dict()
        res = (ln - set(result))
        for nv in res:
            le[nv] = self.E[(ni, nv)]
            menor = min(le, key=le.get)
            result.append(menor)
            ni = menor
    return result





g= Grafo()
g.conecta('Mty', 'X', 8)
g.conecta('Mty', 'Bac', 25)
g.conecta('Mty', 'IM', 13)
g.conecta('Mty', 'Pque', 19)
g.conecta('Mty', 'Ch', 9)
g.conecta('Mty', 'Teo', 10)
g.conecta('Mty', 'MY', 25)
g.conecta('Mty', 'Maz', 9)
g.conecta('Mty', 'LP', 23)
g.conecta('Mty', 'PpV', 10)
g.conecta('LP', 'Maz', 14)
g.conecta('LP', 'IM', 21)
g.conecta('LP', 'X', 26)
g.conecta('LP', 'PpV', 27)
g.conecta('LP', 'Ch', 24)
g.conecta('LP', 'Teo', 24)
g.conecta('LP', 'Pque', 35)
g.conecta('LP', 'MY', 40)
g.conecta('LP', 'Bac', 40)
g.conecta('Maz', 'IM', 6)
g.conecta('Maz', 'X', 13)
g.conecta('Maz', 'PpV', 14)
g.conecta('Maz', 'Ch', 11)
g.conecta('Maz', 'Teo', 11)
g.conecta('Maz', 'Pque', 21)
g.conecta('Maz', 'MY', 26)
g.conecta('Maz', 'Bac', 27)
g.conecta('IM', 'X', 17)
g.conecta('IM', 'PpV', 15)
g.conecta('IM', 'Ch', 15)
g.conecta('IM', 'Teo', 9)
g.conecta('IM', 'Pque', 28)
g.conecta('IM', 'MY', 35)
g.conecta('IM', 'Bac', 34)
g.conecta('X', 'PpV', 6)
g.conecta('X', 'Ch', 6)
g.conecta('X', 'Teo', 6)
g.conecta('X', 'Pque', 17)
g.conecta('X', 'MY', 22)
g.conecta('X', 'Bac', 22)
g.conecta('PpV', 'Ch', 4)
g.conecta('PpV', 'Teo', 3)
g.conecta('PpV', 'Pque', 11)
g.conecta('PpV', 'MY', 16)
g.conecta('PpV', 'Bac', 16)
g.conecta('Ch', 'Teo', 1)
g.conecta('Ch', 'Pque', 11)
g.conecta('Ch', 'MY', 17)
g.conecta('Ch', 'Bac', 16)
g.conecta('Teo', 'Pque', 11)
g.conecta('Teo', 'MY', 16)
g.conecta('Teo', 'Bac', 16)
g.conecta('Pque', 'MY', 7)
g.conecta('Pque', 'Bac', 6)
g.conecta('MY', 'Bac', 4)



print(BFS(g, 'Mty'))
print(DFS(g, 'Mty'))


#Escoge un nodo al azar
import random

N = random.choice(list(g.V))
print(DFS(g, N))
print(BFS(g, N))



#Vecino mas cercano
def Vecino
    N = random.choice(list(g.V))
    recorrido=()


