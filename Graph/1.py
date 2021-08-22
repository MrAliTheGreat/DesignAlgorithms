class Edge:
	def __init__(self , u , v , weight):
		self.u = u
		self.v = v
		self.weight = weight

def find_root(vertex , parents):
	if(parents[vertex] == vertex):
		return vertex
	return find_root(parents[vertex] , parents)

def union(u_root , v_root , parents , heights):
	if(heights[u_root] > heights[v_root]):
		parents[v_root] = u_root
	else:
		parents[u_root] = v_root
		if(heights[u_root] == heights[v_root]):
			heights[v_root] += 1
	return parents , heights

def find_excluded_edges(edges , parents , heights , num_weights , sum_all_weights , not_mst_edges):
	sum_mst = 0
	mst_found = False
	i = 0
	prev_edge_weight = -1

	while i < len(edges):
		if(prev_edge_weight != edges[i].weight):
			for j in range(num_weights[edges[i].weight]):
				if(find_root(edges[i + j].u , parents) == find_root(edges[i + j].v , parents)):
					not_mst_edges[edges[i + j].u][edges[i + j].v] = 1	

		u_root = find_root(edges[i].u , parents)
		v_root = find_root(edges[i].v , parents)
		if(u_root != v_root):
			parents , heights = union(u_root , v_root , parents , heights)
			sum_mst += edges[i].weight

		prev_edge_weight = edges[i].weight
		i += 1

	return sum_all_weights - sum_mst , not_mst_edges

def print_final_answer(final_sum , final_status , n):
	print(final_sum)
	for i in range(n):
		row_str = ""
		for j in range(n):
			if(j == n - 1):
				row_str += (str(final_status[i][j]))
			else:
				row_str += (str(final_status[i][j]) + " ")
		print(row_str)


n , c = list(map(int , input().split()))
edges = []
num_weights = {}
sum_all_weights = 0
not_mst_edges = []

not_mst_edges = [[0 for _ in range(n)] for _ in range(n)]

for u in range(n):
	v = 0
	for weight in list(map(int , input().split())):
		sum_all_weights += weight
		new_edge = Edge(u , v , weight)
		edges.append(new_edge)
		if(weight not in num_weights.keys()):
			num_weights[weight] = 1
		else:
			num_weights[weight] += 1
		v += 1

final_sum , final_status = find_excluded_edges(sorted(edges , key = lambda edge: edge.weight) , list(range(n)) , [1] * n , num_weights , sum_all_weights , not_mst_edges)
print_final_answer(final_sum , final_status , n)