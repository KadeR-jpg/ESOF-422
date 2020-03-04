import numpy as np


class Graph:
    graph_dict = {}

    def addEdge(self, node, neighbor):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbor]
        else:
            self.graph_dict[node].append(neighbor)

    def show_edges(self):
        for node in self.graph_dict:
            for neighbor in self.graph_dict[node]:
                print("(", node,", ", neighbor, ")")



graph = {'0': ['0', '1', '2'],
         '1': ['1', '2'],
         '2': ['2', '3', '4'],
         '3': ['3', '6'],
         '4': ['4', '5', '6'],
         '5': ['5', '4'],
         '6': ['6']}


visited =[]

print(graph['2'])


def DFS(ofGraph, node, ofVisited):
    if node not in ofVisited:
        ofVisited.append(node)
        for neighbor in ofGraph[node]:
            DFS(ofGraph, neighbor, ofVisited)
        return ofVisited


def simplePaths(ofGraph):
    allSimple = []
    for node in ofGraph:
        allSimple.append((DFS(ofGraph, node, [])))
    return allSimple


print(simplePaths(graph))


def makeEdges(ofGraph):
    edges = []
    for node in ofGraph:
        for neighbor in ofGraph[node]:
            edges.append((node, neighbor))
    return edges

# def getSimplePath(ofGraph):

print(makeEdges(graph))
