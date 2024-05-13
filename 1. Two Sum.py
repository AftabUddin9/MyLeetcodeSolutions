class Solution:
    def twoSum (self, nums, target):
        prevMap = {}                        # value : index

        for i, n in enumerate(nums):        
            diff = target - n
            if diff in prevMap:             # if first value exists
                return [prevMap[diff], i]   # return solution
            prevMap[n] = i                  # otherwise add n to map
        return