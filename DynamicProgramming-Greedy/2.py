def is_primary(primay_connections , connection):
	if(connection in primay_connections):
		return True
	return False

def find_overlap(connections , help_dict , current_connection):
	overlap_connections = []
	if(current_connection in primay_connections):
		return []
	for connection in connections:
		if(((current_connection[0] < connection[0] and connection[0] < current_connection[1] and current_connection[1] < connection[1]) or (connection[0] < current_connection[0] and current_connection[0] < connection[1] and connection[1] < current_connection[1])) and not is_primary(primay_connections , connection)):
			overlap_connections.append(connection)
	return overlap_connections

def find_position(connections , num_edges):
	help_list = [connections[0]]
	help_dict = {tuple(connections[0]) : 1}
	counter_ok = 0

	while(len(help_list) != 0):
		current_connection = help_list.pop(0)
		overlap_connections = find_overlap(connections , help_dict , current_connection)

		for new_connection in overlap_connections:
			if(new_connection in help_list and help_dict[tuple(new_connection)] == help_dict[tuple(current_connection)]):
				return {}
			elif(new_connection in help_list and help_dict[tuple(new_connection)] != help_dict[tuple(current_connection)]):
				help_list.remove(new_connection)
			elif(new_connection not in help_list):
				help_list.append(new_connection)
				help_dict[tuple(new_connection)] = int(not(help_dict[tuple(current_connection)]))

		for i in range(num_edges):
			if(tuple(connections[i]) not in help_dict.keys()):
				help_list.append(connections[i])
				help_dict[tuple(connections[i])] = 1
				break;

	return help_dict

def print_answer(final_dict , connections):
	answer = ""
	if(final_dict == {}):
		print("Impossible")
	else:
		for connection in connections:
			if(final_dict[tuple(connection)] == 1):
				answer += "I"
			else:
				answer += "O"
		print(answer)

connections = []
primay_connections = []
num_vertex , num_edges = list(map(int , input().strip().split()))

for _ in range(num_edges):
	connections.append(sorted(list(map(int , input().strip().split()))))

for i in range(1 , num_vertex):
	primay_connections.append([i , i + 1])
primay_connections.append([1 , num_vertex])

print_answer(find_position(connections , num_edges) , connections)
