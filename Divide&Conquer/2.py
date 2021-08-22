def merged_coloring(start , mid , end , left_subboard , right_subboard):
    i = 0 ; j = 0
    while(i < len(left_subboard) and j < len(right_subboard)):
        left_subboard[j].extend(right_subboard[i])
        i += 1
        j += 1

    left_subboard.insert(0 , list(range(mid + 1 , end + 1)))
    left_subboard.insert(0 , list(range(start , mid + 1)))
    return left_subboard

def color_board(start , end):
    if(end == start):
        return [[start]]
    elif(end - start == 1):
        return [[start] , [end]]
    elif(end - start == 2):
        return [[start , start + 1], [start, end], [start + 1, end]]

    mid = (start + end) // 2
    left_subboard_coloring = color_board(start , mid)
    right_subboard_coloring = color_board(mid + 1 , end)
    final_coloring = merged_coloring(start , mid , end , left_subboard_coloring , right_subboard_coloring)
    return final_coloring

def print_answer(answer):
    i = 0 ; j = 0
    final_answer = ""

    print(len(answer))

    while(i < len(answer)):
        final_answer = str(len(answer[i]))
        while(j < len(answer[i])):
            final_answer += (" " + str(answer[i][j] + 1))
            j += 1
        print(final_answer)
        i += 1
        j = 0

size_board = int(input())

print_answer(color_board(0 , size_board - 1))