from collections import defaultdict
import sys


class Graph:

	def __init__(self, graph):
		self.graph = graph 
		self. ROW = len(graph)

	def BFS(self, source, dest, parent):

		visited = [False]*(self.ROW)

		queue = list()

		queue.append(source)
		visited[source] = True

		while queue:

			mid = queue.pop(0)

			for index, value in enumerate(self.graph[mid]):
				if visited[index] == False and value > 0:
					queue.append(index)
					visited[index] = True
					parent[index] = mid
					if index == dest:
						return True

		return False
			
	def FF(self, source, sink):
		parent = [-1]*(self.ROW)

		max_flow = 0 

		while self.BFS(source, sink, parent):

			path_flow = float("Inf")
			s = sink
			while(s != source):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]

			
			max_flow += path_flow

			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]

		return max_flow

#f = open("BipartiteTest.txt")

t = int(input())
graph = [None] * t
for tcount in range(t):
	temp = input().split()
	v = int(temp[0])
	e = int(temp[1])
	graph[tcount] = [None] * v
	for i in range(v):
		graph[tcount][i] = [0] * v 
	
	for ecount in range(e):
		info = input().split()
		v1 = int(info[0]) - 1
		v2 = int(info[1]) - 1
		w = int(info[2])

		graph[tcount][v1][v2] = w 


for tcount in range(t):
	g = Graph(graph[tcount])
	source = 0
	sink = len(graph[tcount]) - 1
	print (g.FF(source, sink))


