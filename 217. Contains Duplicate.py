class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()             # initialized a set to store checked number

        for n in nums:
            if n in hashset:
                return True         # duplicate found if number exists in hashset
            else:
                hashset.add(n)      # otherwise number is added to hashset
        return False