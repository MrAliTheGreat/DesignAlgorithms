def get_happiness(line , size_line):
	i = 0
	happiness_to_left = [0] * size_line
	temp = {}
	while(i < size_line):
		if(line[i] in temp.keys()):
			temp[line[i]] += 1
		else:
			temp[line[i]] = 1
		
		happiness_to_left[i] = temp[line[i]]
		i += 1

	temp.clear()
	i -= 1
	
	happiness_to_right = [0] * size_line

	while(i >= 0):
		if(line[i] in temp.keys()):
			temp[line[i]] += 1
		else:
			temp[line[i]] = 1
		happiness_to_right[i] = temp[line[i]]
		i -= 1

	return happiness_to_left , happiness_to_right

def merge_left_right(left_happiness , right_happiness):
	i = 0 ; j = 0 ; anger = 0
	while(i < len(right_happiness) and j < len(left_happiness)):
		if(right_happiness[i] < left_happiness[j]):
			anger += (len(left_happiness) - j)
			i += 1
		elif(right_happiness[i] >= left_happiness[j]):
			j += 1
	return anger

def find_num_anger(line , start , end , happiness):
	if(start >= end):
		return 0
	mid = (start + end) // 2
	left_anger = find_num_anger(line , start , mid , happiness)
	right_anger = find_num_anger(line , mid + 1 , end , happiness)
	merged_anger = merge_left_right(sorted(happiness[0][start : mid + 1]) , sorted(happiness[1][mid + 1 : end + 1]))
	return(left_anger + merged_anger + right_anger)

size_line = int(input())

line = list(map(int , input().split()))

print(find_num_anger(line , 0 , size_line - 1 , get_happiness(line , size_line)))