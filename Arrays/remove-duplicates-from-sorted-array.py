class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
################################################################
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)
################################################################
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        r=1
        while r<len(nums):
            if nums[r-1] != nums[r]:
                nums[l]= nums[r]
                l +=1
                r+=1
            else:
                r +=1
        return l