def find_all_spendings(prices , size_tours , num_countries , max_money , index_country , money_spent , all_sums):
	if(max_money < 0):
		return all_sums
	elif(index_country >= num_countries):
		if(money_spent not in  all_sums):
			all_sums.append(money_spent)
		return all_sums
	for index_tour in range(size_tours[index_country]):
		spent_value = find_all_spendings(prices , size_tours , num_countries , max_money - prices[index_country][index_tour] , index_country + 1 , money_spent + prices[index_country][index_tour] , all_sums)
	return all_sums

def find_max_spending(sums_first_half , sums_second_half , max_money):
	highest_spending = 0
	for num_second_half in sums_second_half:
		start = 0
		end = len(sums_first_half) - 1		
		while(start <= end):
			mid = (start + end) // 2
			if(sums_first_half[mid] + num_second_half <= max_money):
				spending = sums_first_half[mid] + num_second_half
				highest_spending = max(highest_spending , spending)
				start = mid + 1
			else:
				end = mid - 1
	return highest_spending

prices = []
answers = []
num_test = int(input())
for _ in range(num_test):
	max_money , num_countries = list(map(int , input().split()))
	size_tours = list(map(int , input().split()))
	for _ in range(num_countries):
		prices.append(sorted(list(map(int , input().split()))))
	sums_first_half = sorted(find_all_spendings(prices[0 : (num_countries - 1) // 2 + 1] , size_tours[0 : (num_countries - 1) // 2 + 1] , (num_countries - 1) // 2 + 1 , max_money , 0 , 0 , []))
	sums_second_half = find_all_spendings(prices[(num_countries - 1) // 2 + 1 : ] , size_tours[(num_countries - 1) // 2 + 1 : ] , num_countries - ((num_countries - 1) // 2 + 1) , max_money , 0 , 0 , [])
	answers.append(find_max_spending(sums_first_half , sums_second_half , max_money))
	prices = []

for answer in answers:
	print(answer)