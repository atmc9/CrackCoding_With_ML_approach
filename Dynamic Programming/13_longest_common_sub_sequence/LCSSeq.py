# Solving Longest common sub sequence using Dynamic programming

def longest_common_sub_sequence(s1, s2):
    if not s1 or not s2:
        return ''
    s1_len = len(s1)  # height of matrix
    s2_len = len(s2)  # width of matrix
    T = [[0 for j in range(s2_len + 1)] for i in range(s1_len + 1)]
    for i in range(1, s1_len + 1):
        for j in range(1, s2_len + 1):
            if s1[i-1] == s2[j-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i][j-1], T[i-1][j])
    val = ''
    i = s1_len
    j = s2_len
    # starting from right-bottom corner traverse for longest common sub sequence
    while i > 0 and j>0:
        if s1[i-1] == s2[j-1]:
            val = s1[i-1] + val
            i = i-1
            j = j-1
        elif T[i][j] == T[i][j-1]:
            j = j-1
        else:
            i = i-1
    return val

if __name__ == '__main__':
    print(longest_common_sub_sequence('anvesh', 'abenvsh'))
