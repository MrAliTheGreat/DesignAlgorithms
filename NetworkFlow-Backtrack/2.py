def BFS(graph , start_node , end_node):
	parents = [-1] * len(graph)
	visited = [False] * len(graph)
	q = [] 
	q.append(start_node) 
	visited[start_node] = True
	while (len(q) != 0):
		u = q.pop(0) 
		for i in range(len(graph[u])):
			if(visited[i] == False and graph[u][i] > 0):
				q.append(i) 
				visited[i] = True
				parents[i] = u
	return visited , parents


def ford_fulkerson(graph , num_projects , num_companies):
	max_flow = 0
	while(True):
		visited , parents = BFS(graph , 0 , num_projects + num_companies + 1)
		
		if(visited[num_projects + num_companies + 1] == False):
			return max_flow

		v = num_projects + num_companies + 1
		min_increased_flow = float("inf")
		while(v != 0): 
			min_increased_flow = min(min_increased_flow, graph[parents[v]][v]) 
			v = parents[v] 		
		v = num_projects + num_companies + 1
		while(v != 0):
			u = parents[v]
			graph[u][v] -= min_increased_flow
			graph[v][u] += min_increased_flow
			v = u
		max_flow += min_increased_flow
	return max_flow


def create_graph(num_projects , num_companies , project_costs , company_money , wanted_projects):
	total_money = 0
	graph = [[0 for _ in range(num_projects + num_companies + 2)] for _ in range(num_projects + num_companies + 2)]
	for i in range(num_projects + num_companies + 2):
		if(i == 0):
			for j in range(num_companies):
				graph[i][j + 1] = company_money[j]
				total_money += company_money[j]
		elif(i == num_projects + num_companies + 1):
			continue
		elif(i >= 1 and i <= num_companies):
			for j in range(num_projects):
				if(wanted_projects[i - 1][j] == 1):
					graph[i][j + 1 + num_companies] = float("inf")
		else:
			graph[i][num_projects + num_companies + 1] = project_costs[i - num_companies - 1]
	return graph , total_money


num_projects , num_companies = list(map(int , input().split()))
project_costs = list(map(int , input().split()))
company_money = list(map(int , input().split()))
wanted_projects = []
for _ in range(num_companies):
	wanted_projects.append(list(map(int , input().split())))

graph , total_money = create_graph(num_projects , num_companies , project_costs , company_money , wanted_projects)
print(total_money - ford_fulkerson(graph , num_projects , num_companies))