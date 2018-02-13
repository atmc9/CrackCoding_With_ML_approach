def burstballons(nums):
    if not nums:
            return 0
    inpLen = len(nums)

    if inpLen == 1:
        return nums[0]

    T = [[0] * (inpLen) for _ in range(inpLen)]

    for p in range(inpLen):
        for q in range(inpLen - p):
            i = q
            j = q+p
            for k in range(i, j+1):
                val = 0
                if i <= k-1:
                    val += T[i][k-1]
                if k+1 <= j:
                    val += T[k+1][j]

                left = nums[i-1] if i-1 >=0 else 1
                right = nums[j+1] if j+1 < inpLen else 1
                val += left * nums[k] * right
                
                T[i][j] = max(T[i][j], val)

    return T[0][inpLen-1]


if __name__ == '__main__':
    print(burstballons([3, 1, 5, 8]))
