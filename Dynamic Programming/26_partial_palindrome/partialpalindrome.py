# Write a function that, given a string, returns the leftmost largest part of that string that is a palindrome,
# discarding stuff left and right that canot participate. For example
#     abcxxyayxxd -> xxyayxx
#     wwwxxwwb -> wwxxww
#     abcdefg -> a
#     abcbcd -> bcb

def partial_palindrome(S):

    T = [[0] * (len(S)) for _ in range(len(S))]

    for i in range(len(S)):
        for j in range(len(S) - i):
            if i == 0:
                T[j][j+i] = 1
            else:
                if S[j] == S[j+i]:
                    T[j][j+i] = max(2+T[j+1][j+i-1], T[j][j+i-1], T[j+1][j+i])
                else:
                    T[j][j+i] = max(T[j][j+i-1], T[j+1][j+i])

    pos_i = 0
    pos_j = len(S) -1
    max_len = T[pos_i][pos_j]
    while (pos_j != pos_i) and (T[pos_i][pos_j] == T[pos_i][pos_j-1] or T[pos_i][pos_j] == T[pos_i+1][pos_j]):
        if T[pos_i][pos_j] == T[pos_i+1][pos_j]:
            pos_i = pos_i + 1
        else:
            pos_j = pos_j - 1

    return S[pos_i : pos_j +1]
    #return S[pos_j-max_len+1:pos_j+1]


if __name__ == '__main__':
    print(partial_palindrome('abcbm'))
