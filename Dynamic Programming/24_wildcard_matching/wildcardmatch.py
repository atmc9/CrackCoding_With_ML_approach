# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false

import sys

def wildcard_match(S1, S2):
    # creating a 2-D array T
    T = [[False] * (len(S2)+1) for _ in range(len(S1)+1)]

    for i in range(len(S1)+1):
        for j in range(len(S2)+1):
            if i ==0 and j ==0:
                T[i][j] = True
            elif j ==0:
                T[i][j] = False
            elif i ==0:
                T[i][j] = T[i][j-1] if S2[j-1] == '*' else False
            else:
                if S1[i-1] == S2[j-1] or S2[j-1] == '?':
                    T[i][j] = T[i-1][j-1]
                elif S2[j-1] == '*':
                    T[i][j] = (T[i][j-1] or T[i-1][j])
                else:
                    T[i][j] = False
    return T[len(S1)][len(S2)]
if __name__ == '__main__':
    print(wildcard_match('xaylmz', 'x?y*z'))
