#! /usr/bin/env python3
from collections import defaultdict

'''
Problem Statement:
    - Topologically sort the following Graph:
        Nodes: A,B,C,D,E,F,G,H,I
        Graph:
            G -> H <- A         I
            A -> B -> C -> F
            D -> E -> F
            D -> B -> C -> F
    - Assumption: the given graph is a Directed Acyclic Graph (no back - edges, only tree - edges, cross - edges, and forward - edges)
'''

def dfs_visit(adj, s, visited, stack):
    visited.add(s)
    for v in adj[s]:
        if v not in visited:
            dfs_visit(adj, v, visited, stack)
    stack.append(s)

def dfs(nodes, adj):
    visited = set()
    stack = []
    for v in nodes:
        if v not in visited:
            dfs_visit(adj, v, visited, stack)
    return stack

def topSort(nodes, adj):
    return list(reversed(dfs(nodes, adj)))

if __name__ == '__main__':
    graph_nodes = 'ABCDEFGHI'
    directed_acyclic_graph = [('G','H'), ('A', 'H'),
                              ('A', 'B'), ('B', 'C'),
                              ('C', 'F'), ('D', 'B'),
                              ('D', 'E'), ('E', 'F'), ]
    adj = defaultdict(set)
    for u, v in directed_acyclic_graph:
        adj[u].add(v)
    print(topSort(graph_nodes, adj))