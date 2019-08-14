# Create a program that finds the shortest path through a graph using its edges.
#
# Algorithm: 
# 1. Create empty set S= {} . This will hold the set of nodes we already know the shortest path to.
# 2. Create a full set Q={all nodes}. This is the set of nodes we don't know the shortest path to.
# 3. Create a weighted array d, where every node is inialized to infinity, and the starting node s0 has d[s0] = 0
# 4.      while Q does not equal NULL:
#              Extract Min from Q and add it to S
#              For each vertex v coming out of S:
#                   relax(u,v,w) 
import math

class Node:
    def __init__(self,name):
        self.name=name
        self.next=[]
        self.length={}
        
    def setData(self,nextlist,length):
        self.next=nextlist
        self.length=dict(zip(nextlist,length))
        
def Dijkstra(A,B,graph_in):
    S=[] # create empty set S
    Q=graph_in
    d={}
    for curNode in graph_in:
        d[curNode]=math.inf
    d[A]=0
    while Q:
        curNode=min(d, key=d.get) #Extract Min
        print(str(d))
        print(str(curNode.name))
        if curNode==B:
            return d[curNode]
        Q.pop(Q.index(curNode)) #Take out of Q
        S.append(curNode) #Put into S
        for v in curNode.next: #for each vertex v coming out of the extracted node:
            d[v]=curNode.length[v]+d[curNode]   #relax v
        d.pop(curNode)
        
def main():
    A=Node("A")
    B=Node("B")
    C=Node("C")
    D=Node("D")
    E=Node("E")
    A.setData([B,C],[10,3])
    B.setData([C,D],[1,2])
    C.setData([B,D,E],[4,8,2])
    D.setData([E],[7])
    E.setData([D],[1])
    shortest_path=Dijkstra(A,D,[A,B,C,D,E])
    print("The shortest path from "+A.name+" to "+D.name+" is "+str(shortest_path))

main()
