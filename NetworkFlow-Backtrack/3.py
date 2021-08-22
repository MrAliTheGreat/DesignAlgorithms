def BFS(graph_flow , graph_cost , size_graph , start_node , max_cost):
	parents = [-1] * size_graph
	visited = [False] * size_graph
	q = [] 
	q.append(start_node) 
	visited[start_node] = True
	while (len(q) != 0):
		u = q.pop(0)
		for i in range(size_graph):
			if(visited[i] == False and graph_flow[u][i] > 0 and graph_cost[u][i] <= max_cost):
				q.append(i) 
				visited[i] = True
				parents[i] = u
	return visited , parents

def find_min_spent(graph_flow , graph_cost , size_graph , size_table , sorted_table , copy_graph_flow):
	pos_answer = -1
	start = 0;
	end = (size_table ** 2) - 1
	while(start <= end):
		mid = (start + end) // 2
		max_flow = 0
		make_copy(copy_graph_flow , graph_flow , size_graph)
		while(True):
			visited , parents = BFS(graph_flow , graph_cost , size_graph , 0 , sorted_table[mid])
			
			if(visited[size_graph - 1] == False):
				break

			v = size_graph - 1
			increase_flow = float("inf")
			while(v != 0):
				increase_flow = min(increase_flow , graph_flow[parents[v]][v])
				v = parents[v]

			max_flow += increase_flow

			v = size_graph - 1
			while(v != 0):
				u = parents[v]
				graph_flow[u][v] -= increase_flow
				graph_flow[v][u] += increase_flow
				v = u

		if(max_flow == size_table):
			pos_answer = mid
			end = mid - 1
		else:
			start = mid + 1
	return sorted_table[pos_answer]


def create_graph(table , size_table):
	size_graph = (size_table * 2) + 2
	graph_flow = [[0 for _ in range(size_graph)] for _ in range(size_graph)]
	graph_cost = [[0 for _ in range(size_graph)] for _ in range(size_graph)]
	for i in range(size_graph):
		if(i == 0):
			for j in range(size_table):
				graph_flow[i][j + 1] = 1
		elif(i >= 1 and i <= size_table):
			for j in range(size_table):
				graph_flow[i][j + 1 + size_table] = 1
				graph_cost[i][j + 1 + size_table] = table[i - 1][j]
				graph_cost[j + 1 + size_table][i] = table[i - 1][j]
		elif(i == size_graph - 1):
			continue
		else:
			graph_flow[i][size_graph - 1] = 1
	return graph_flow , graph_cost


def make_copy(graph_flow , copy_graph_flow , size_graph):
	for i in range(size_graph):
		for j in range(size_graph):
			copy_graph_flow[i][j] = graph_flow[i][j]
	return copy_graph_flow


table = []
sorted_table = []
size_table = int(input())
for _ in range(size_table):
	row_table = list(map(int , input().split()))
	table.append(row_table)
	sorted_table.extend(row_table)

graph_flow , graph_cost = create_graph(table , size_table)
copy_graph_flow = [[0 for _ in range((size_table * 2) + 2)] for _ in range((size_table * 2) + 2)]

copy_graph_flow = make_copy(graph_flow , copy_graph_flow , (size_table * 2) + 2)
print(find_min_spent(graph_flow , graph_cost , (size_table * 2) + 2 , size_table , sorted(sorted_table) , copy_graph_flow))