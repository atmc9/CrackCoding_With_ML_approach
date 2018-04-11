def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    #T = [[False] * (len(s2)+1) for _ in range(len(s1) +1)]
    current = [(-1,-1)]

    for c in s3:
        newCurrent = []
        for i, j in current:
            if i+1 < len(s1) and s1[i+1] == c:
                print(i+1, j)
                newCurrent.append((i+1, j))
            if j+1 < len(s2) and s2[j+1] == c:
                print(i, j+1)
                newCurrent.append((i, j+1))
        current = newCurrent

    for i, j in current:
        if (i == len(s1)-1 and j == len(s2)-1):
            return True

    return False


if __name__ == '__main__':
    print(isInterleave('dbbca', 'aabcc', 'aabccdbbca'))
