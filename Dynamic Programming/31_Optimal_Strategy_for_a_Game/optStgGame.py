def optimal_strategy_for_a_game(S):
    if not S :
        return 0

    T = [[(0,0)] * len(S) for _ in range(len(S))]

    for p in range(len(S)):
        for q in range(len(S) - p):
            i = q
            j = q + p

            if i == j:
                T[i][j] = (S[i], 0)
            else:
                # if we select first k = i
                val1 = S[i] + T[i+1][j][1]

                # if we select last k = j
                val2 = S[j] + T[i][j-1][1]

                if val1 > val2:
                    T[i][j] = (val1, T[i+1][j][0])
                else:
                    T[i][j] = (val2, T[i][j-1][0])

    return T[0][len(S)-1]



if __name__ == '__main__':
    print(optimal_strategy_for_a_game([3, 9, 1, 2]))
