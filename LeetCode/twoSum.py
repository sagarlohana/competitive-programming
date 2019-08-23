def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    sortedNums = list(nums)
    sortedNums.sort()
    i = 0
    j = len(nums) - 1
    while i < j:
        if sortedNums[i] + sortedNums[j] == target:
            i = nums.index(sortedNums[i])
            print(nums)
            j = nums.index(sortedNums[j])
            print(nums)
            return [i,j]
        elif sortedNums[i] + sortedNums[j] > target:
            j = j-1
        else:
            i = i+1
    return [i, j]
    
print(twoSum([3, 2, 4], 6))