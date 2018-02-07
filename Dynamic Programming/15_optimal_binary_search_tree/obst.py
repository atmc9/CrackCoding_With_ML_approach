# Problem Description
import sys

def optimal_binary_search_tree(nodes):
    len_nodes = len(nodes)
    T = [[0] * (len_nodes) for _ in range(len_nodes)]
    C = [[0] * (len_nodes) for _ in range(len_nodes)]
    frequency = [x[1] for x in nodes]
    for i in range(len_nodes):
        for j in range(len_nodes-i):

            if i ==0:
                T[j][j] = nodes[j][1]
            else:
                (split, min_amount) = pick_root(T, j, j+i)
                T[j][j+i] = sum(frequency[j:j+i+1]) + min_amount
                C[j][j+i] = split

    tree = get_tree(C, 0, len_nodes -1)

    return T[0][len_nodes-1], tree

def pick_root(T, i, j):
    min_amount = sys.maxsize
    split = -1
    for k in range(i, j+1):
        if k == i:
            temp = T[i+1][j]
        elif k == j:
            temp = T[i][j-1]
        else:
            temp = T[i][k-1] + T[k+1][j]
        if temp < min_amount:
            min_amount = temp
            split = k
    return (split, min_amount)

def get_tree(C, i, j):
    if i == 0 and j == 0:
        return ''
    elif i == j:
        return str(i)
    elif C[i][j] == i:
        return str(C[i][j]) + '('+ get_tree(C, C[i][j]+1, j) + ')'
    elif C[i][j] == j:
        return  '('+ get_tree(C, i, C[i][j]- 1) + ')' + str(C[i][j])
    else:
        return '('+ get_tree(C, i, C[i][j]- 1) +')'+ str(C[i][j]) + '('+ get_tree(C, C[i][j]+1, j) + ')'


if __name__ == '__main__':
    print(optimal_binary_search_tree([(10,4),(12,2),(16,6),(21,3)]))
