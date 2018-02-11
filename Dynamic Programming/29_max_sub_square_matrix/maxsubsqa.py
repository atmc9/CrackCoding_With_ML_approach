# Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

def max_sub_square_matrix(S):
    rows = len(S)
    columns = len(S[0]) if rows > 0 else 0

    T = [[0] * (columns +1) for _ in range(rows + 1)]

    diag_i, diag_j = (0, 0)
    for i in range(1, rows + 1):
        for j in range(1, columns +1):
            if S[i-1][j-1] == 0:
                T[i][j] = 0
            else:
                T[i][j] = min(T[i-1][j], T[i][j-1], T[i-1][j-1]) + 1
                if T[diag_i][diag_j] < T[i][j]:
                    diag_i, diag_j = (i, j)

    max_sqa_len = T[diag_i][diag_j]

    max_sub_sqa = [ row[diag_j-max_sqa_len : diag_j] for row in S[diag_i-max_sqa_len : diag_i] ]
    return max_sqa_len , max_sub_sqa

if __name__ == '__main__':
    print(max_sub_square_matrix([[0, 0, 1, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1]]))
