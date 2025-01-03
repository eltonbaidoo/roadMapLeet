def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # loop through the length of the array 
    
    num_to_index = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    
    return []
    '''
    m = 1
    for i in range(len(nums)):
        for j in range(m, len(nums)):
            if (nums[i] + nums[j]) == target:
                
                return [i, j]
        m += 1    
    '''