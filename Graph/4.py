from collections import defaultdict
from heapq import heapify, heappush, heappop

class Edge:
	def __init__(self , u , v , w):
		self.u = u;
		self.v = v;
		self.w = w;

def dijkstra(edges, source, target):
	nodes = defaultdict(list)
	for edge in edges:
		nodes[edge.u].append((edge.w,edge.v))

	q, seen, mins = [(0,source,())], set(), {source: 0}
	while q:
		(cost,node_1,path) = heappop(q)
		if node_1 not in seen:
			seen.add(node_1)
			path = (node_1, path)
			if node_1 == target:
				return cost

			for c, node_2 in nodes.get(node_1, ()):
				if node_2 in seen: 
					continue
				prev = mins.get(node_2, None)
				next = cost + c
				if(prev is None or next < prev):
					mins[node_2] = next
					heappush(q, (next, node_2, path))

	return 10 ** 9


def find_path(edges , disappeared_index , shortest_path , num_nodes):
	for index in disappeared_index:
		edges[index].w = shortest_path
	if(dijkstra(edges , 1 , num_nodes) < shortest_path):
		print("No")
		return []
	for index in disappeared_index:
		edges[index].w = 1
	if(dijkstra(edges , 1 , num_nodes) > shortest_path):
		print("No")
		return []

	for index in disappeared_index:
		for _ in range(1 , shortest_path + 1):
			edges[index].w += 1
			if(dijkstra(edges , 1 , num_nodes) == shortest_path):
				return edges
	return []

def print_final_answer(edges , num_nodes , num_edges):
	if(len(edges) != 0):
		print("Yes")
		for edge in edges:
			print(str(edge.u) + " " + str(edge.v) + " " + str(edge.w))

num_nodes , num_edges , num_disappeared = list(map(int , input().split()))
edges = []
disappeared_index = []
index_in_edges = 0

for _ in range(num_edges):
	u , v , w = list(map(int , input().split()))
	new_edge = Edge(u , v , w)
	edges.append(new_edge)
	if(w == 0):
		disappeared_index.append(index_in_edges)
	index_in_edges += 1

shortest_path = int(input())

print_final_answer(find_path(edges , disappeared_index , shortest_path , num_nodes) , num_nodes , num_nodes)