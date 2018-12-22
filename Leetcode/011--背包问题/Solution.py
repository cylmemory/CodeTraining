def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    half_sum = sum(nums)
    if half_sum % 2 == 1:
        return False
    half_sum = half_sum / 2
    d = [[False for x in xrange(half_sum + 1)] for y in xrange(len(nums) + 1)]
    for k in xrange(len(nums) + 1):
        d[k][0] = True

    for i in xrange(1, len(nums) + 1):
        for j in xrange(0, half_sum + 1):
            d[i][j] = d[i - 1][j]
            if j >= nums[i - 1]:
                d[i][j] = d[i][j] | d[i - 1][j - nums[i - 1]]

    return d[len(nums)][half_sum]
