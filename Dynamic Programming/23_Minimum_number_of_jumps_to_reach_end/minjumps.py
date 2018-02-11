# Given an array of integers where each element represents the max number of steps that can be made forward from that element.
# Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element).
# If an element is 0, then cannot move through that element.
import sys

def min_number_of_jumps(S):
    # base case if S length is 0
    if not S:
        return 0

    # creating a 1-D array T
    T = [sys.maxsize] * len(S)
    pos = [0] * len(S)
    T[0] = 0
    for i in range(1,len(S)):
        for j in range(i):
            if S[j] >= i-j:
                T[i] = min(T[i], T[j]+1)
                pos[i] = j if T[j]+1 <= T[i] else pos[i]

    # return the mimimum jumps, jumping positions
    return T[-1], get_jumping_pos_values(pos, S)

def get_jumping_pos_values(pos, S):
    pos_list = []
    i = len(pos) -1
    pos_list.append(i)
    while i > 0:
        pos_list.insert(0, pos[i])
        i = pos[i]
    return pos_list, [S[i] for i in pos_list]

if __name__ == '__main__':
    print(min_number_of_jumps([2, 3, 1, 1, 2, 4, 2, 0, 1, 1]))
