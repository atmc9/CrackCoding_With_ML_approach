# Longest Common SubString using Dynamic Programing
def Long_Common_Sub_String(s1, s2):
    if not s1 or not s2:
        return ''
    s1_len = len(s1)  # s1 is height - left of array
    s2_len = len(s2)  # s2 is width - top of array
    T = [[0 for j in range(s2_len+1)] for i in range(s1_len +1)]

    max_length = 0
    max_end_pos_s1 = 0  # LCSS ending position in string s1, it could be either s2

    for i in range(1, s1_len+1):
        for j in range(1, s2_len+1):
            if s1[i-1] == s2[j-1]:
                T[i][j] = T[i-1][j-1] + 1
                if max_length < T[i][j]:
                    max_length = T[i][j]
                    max_end_pos_s1 = i
            else:
                T[i][j] = 0

    return s1[max_end_pos_s1-max_length : max_end_pos_s1]


# main method
if __name__ == '__main__':
    print(Long_Common_Sub_String('abcdanvlsh', 'anveshabcd'))
