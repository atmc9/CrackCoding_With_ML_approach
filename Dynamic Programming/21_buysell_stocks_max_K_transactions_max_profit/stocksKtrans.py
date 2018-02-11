# suppose if we have stocks for N days in a list say S,
# if we have a limit to do only K-transactions (transaction include both selling and buying),
# what is the best profit we could have made and what are those transactions.

def buy_sell_stocks_K_trans(S, K):
    T = [[0] * len(S) for _ in range(K+1)]

    for i in range(1, K+1):
      for j in range(len(S)):
          tempmax = 0
          for m in range(j):
              if S[m] < S[j]:
                  temp = S[j] - S[m] + T[i-1][m]
                  tempmax = max(temp, tempmax)
          T[i][j] = max(tempmax, T[i][j-1])

    return (T[K][len(S)-1], getTransactions(T, S))

def getTransactions(T, S):
    pos = []
    val = []
    i = len(T) - 1
    j = len(S) - 1
    profit = T[i][j]
    while j>=0:
          if T[i][j] == T[i][j-1]:
              j = j-1
          else:
              sell_index = j
              profit = profit - S[j]
              i = i-1
              j = j-1
              while j >=0 and profit != T[i][j] - S[j]:
                  j = j-1
              profit = profit + S[j]
              pos.insert(0, (j, sell_index))
              val.insert(0, (S[j], S[sell_index]))

    return val, pos



if __name__ == '__main__':
    print(buy_sell_stocks_K_trans([2,5,7,1,4,3,1,3], 3))
