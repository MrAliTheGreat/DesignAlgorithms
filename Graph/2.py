def find_time_events(distances , num_houses , num_events , time_event):
	events = []
	for _ in range(num_events):
		guest , host = list(map(int , input().split()))
		guest -= 1 ; host -= 1
		if(len(events) == 0):
			events.append([host , [guest]])
		elif(events[-1][0] == host):
			events[-1][1].append(guest)
		elif(events[-1][0] != host):
			events.append([host , [guest]])

	time_nodes = [{"leave" : 0 , "arrive" : 0} for _ in range(num_houses)]
	start_event_time = -1
	largest_start_event_time = start_event_time

	for i in range(len(events)):
		for j in range(len(events[i][1])):
			guest = events[i][1][j]; host = events[i][0]

			start_event_time = max(time_nodes[host]["arrive"] , time_nodes[guest]["leave"] + distances[guest][host])
			print(start_event_time + time_event)
			time_nodes[guest]["arrive"] = start_event_time + time_event + distances[host][guest]
			time_nodes[guest]["leave"] = time_nodes[guest]["arrive"]
			largest_start_event_time = max(largest_start_event_time , start_event_time)
			if(time_nodes[host]["leave"] < largest_start_event_time + time_event):
				time_nodes[host]["leave"] = largest_start_event_time + time_event

		start_event_time = -1
		largest_start_event_time = start_event_time


def floyd_warshall(distances , num_houses):
	for k in range(num_houses):
		for i in range(num_houses):
			for j in range(num_houses):
				if(distances[i][j] > distances[i][k] + distances[k][j]):
					distances[i][j] = distances[i][k] + distances[k][j]
	return distances


num_houses , num_roads = list(map(int , input().split()))
distances = [[10 ** 15 for _ in range(num_houses)] for _ in range(num_houses)]

for i in range(num_houses):
	distances[i][i] = 0

for _ in range(num_roads):
	u , v , w = list(map(int , input().split()))
	u -= 1; v -= 1
	distances[u][v] = min(distances[u][v] , w)
	distances[v][u] = min(distances[v][u] , w)

num_events , time_event = list(map(int , input().split()))

find_time_events(floyd_warshall(distances , num_houses) , num_houses , num_events , time_event)