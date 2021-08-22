import math

def divide_by_degree(coordinates):
	new_subtree = []
	min_y_coordinate = min(coordinates , key = lambda y: y[1])

	for coordinate in coordinates:
		if(coordinate == min_y_coordinate):
			continue
		degree = math.atan( (coordinate[1] - min_y_coordinate[1]) / (coordinate[0] - min_y_coordinate[0]) ) * (180 / math.pi)
		if(degree >= 0):
			new_subtree.append((degree , coordinate[0] , coordinate[1] , coordinate[2]))
		elif(degree < 0):
			new_subtree.append((degree + 180 , coordinate[0] , coordinate[1] , coordinate[2]))

	new_subtree = sorted(new_subtree, key = lambda element: element[0])
	
	i = 0
	while(i < len(new_subtree)):
		new_subtree[i] = new_subtree[i][1 :]
		i += 1

	return new_subtree[0 : (len(new_subtree) - 1) // 2 + 1] , new_subtree[(len(new_subtree) - 1) // 2 + 1 :] , min_y_coordinate


def merged_subtrees(root , left_subtree , right_subtree , node_num):
	left_subtree.extend(right_subtree)
	left_subtree.append((node_num , root[2]))
	return left_subtree


def draw_tree(coordinates , height , node_num):
	if(len(coordinates) == 1 or height == 0):
		return [(node_num , min(coordinates , key = lambda x: x[0])[2])]

	height -= 1
	left_subtree , right_subtree , root = divide_by_degree(coordinates)
	left_answer = draw_tree(left_subtree , height , 2 * node_num)
	right_answer = draw_tree(right_subtree , height , 2 * node_num + 1)
	return merged_subtrees(root , left_answer , right_answer , node_num)


def print_answer(answer , num_coordinates , height):
	final_answer = [0] * num_coordinates
	num_nodes = 0
	
	for item in answer:
		final_answer[item[1]] = item[0]

	for num in final_answer:
		if(num != 0):
			num_nodes += 1

	if(num_nodes >= 1 and num_nodes <= (2 ** (height + 1)) - 1):
		for num in final_answer:
			print(num)
	else:
		print(-1)

n , k = list(map(int , input().split()))

coordinates = []

for index in range(n):
	new_x , new_y = list(map(int , input().split()))
	coordinates.append((new_x , new_y , index))

print_answer(draw_tree(coordinates , k , 1) , n , k)