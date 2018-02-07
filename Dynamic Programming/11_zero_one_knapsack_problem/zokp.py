# Problem description:
# A thief has a bag size of say W = 7,
# there are items with weights, values
#  Weight   | Value
#   1       |   1
#   3       |   4
#   4       |   5
#   5       |   7

# the goal is to collect more value in the bag of W=7
# Note: you cannot collect partial values - 0/1 knapsack, either you got the item or not

def zero_one_knapsack(w, items):
    len_items = len(items)
    T = [[0] * (w+1) for i in range(len_items+1)]
    for i in range(1, len_items+1):
        for j in range(1, w+1):
            (i_weight, i_value) = items[i-1]
            #print(items[i-1])
            if i_weight <= j:
                T[i][j] = max(T[i-1][j], i_value + T[i-1][j-i_weight])
            else:
                T[i][j] = T[i-1][j]

    val = []
    i = len_items
    j = w
    while i > 0 and j > 0:
        if T[i][j] == T[i][j-1]:
            j = j-1
        elif T[i][j] == T[i-1][j]:
            i = i-1
        else:
            (i_weight, i_value) = items[i-1]
            val.append(items[i-1])
            i = i-1
            j = j - i_weight

    return val

if __name__ == '__main__':
    print(zero_one_knapsack(7, [(1,1),(3,4),(4,5),(5,7)]))
