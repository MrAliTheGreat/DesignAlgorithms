def get_max_sum(nodes_info , current_node , dp):
	if(len(nodes_info[current_node][1]) == 0):
		dp[current_node] = (0 , 0)
		return dp

	for i in range(len(nodes_info[current_node][1])):
		dp = get_max_sum(nodes_info , nodes_info[current_node][1][i] , dp)

	total_chosen = 0
	min_diff = -1
	max_sum = 0

	for key in nodes_info[current_node][1]:
		if(min_diff == -1):
			if(dp[key][0] + nodes_info[key][0] > dp[key][1]):
				min_diff = nodes_info[key][0]
			elif(dp[key][0] + nodes_info[key][0] <= dp[key][1]):
				min_diff = dp[key][1] - dp[key][0]
			tuple_child = dp[key]
			child_value = nodes_info[key][0]
			chosen_element = max((dp[key][0] + nodes_info[key][0]) , dp[key][1])
		
		if(dp[key][0] + nodes_info[key][0] > dp[key][1]):
			max_sum += (dp[key][0] + nodes_info[key][0])
			if(nodes_info[key][0] < min_diff):
				min_diff = nodes_info[key][0]
				tuple_child = dp[key]
				child_value = nodes_info[key][0]
				chosen_element = dp[key][0] + nodes_info[key][0]

		elif(dp[key][0] + nodes_info[key][0] <= dp[key][1]):
			max_sum += dp[key][1]
			if(dp[key][1] - dp[key][0] < min_diff):
				min_diff = dp[key][1] - dp[key][0]
				tuple_child = dp[key]
				child_value = nodes_info[key][0]
				chosen_element = dp[key][1]

		total_chosen += 1

	if(total_chosen % 2 == 0):
		if(chosen_element in tuple_child):
			dp[current_node] = (max_sum , max_sum - chosen_element + tuple_child[0])
		else:
			dp[current_node] = (max_sum , max_sum - chosen_element + tuple_child[0])
	else:
		if(chosen_element in tuple_child):
			dp[current_node] = (max_sum - chosen_element + tuple_child[0] , max_sum)
		else:
			dp[current_node] = (max_sum - chosen_element + tuple_child[0] , max_sum)

	return dp 


nodes_info = {-1 : (0 , [1])}
num_nodes = int(input())
for i in range(num_nodes):
	info = list(map(int , input().split()))
	nodes_info[i + 1] = (info[1] , [])
	if(info[0] == -1):
		continue
	nodes_info[info[0]][1].append(i + 1)

print(max(get_max_sum(nodes_info , -1 , {})[-1]))