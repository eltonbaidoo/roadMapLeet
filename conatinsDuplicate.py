def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    #Solution 1 O(n^2)
    '''
    m = 0  
    
    for i in range(m, len(nums)):

        for j in range(m + 1, len(nums)):
            if nums[m] == nums[j]:
                return True
        m += 1
        
    return False
    '''
    #Solution 2 O(n)
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    
    return False
