# Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array such
# that the intgers in the subsequence are sorted in increasing order. For example, if input is {1, 101, 2, 3, 100, 4, 5},
#  then output should be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10)
#  and if the input array is {10, 5, 4, 3}, then output should be 10

def max_sum_inc_subseq(S):
    T = list(S)

    for i in range(1, len(S)):
        for j in range(i):
            if S[j] <= S[i]:
                T[i] = max(T[i], S[i] + T[j])
    print(T)

    max_index = -1
    for i in range(len(S)):
        if T[max_index] < T[i]:
            max_index = i

    max_sum = T[max_index]
    index = max_index
    max_sum_list = []
    while max_sum > 0:
        if max_sum - S[index] >= 0:
            max_sum = max_sum - S[index]
            max_sum_list.insert(0, S[index])
        index = index - 1
    return T[max_index], max_sum_list

if __name__ == '__main__':
    print(max_sum_inc_subseq([1, 101, 2, 3, 100, 4, 5]))
