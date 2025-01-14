class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

##############################################################
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0      
        for i in range(len(nums)):
            if val != nums[i]:
                nums[count]=nums[i]
                count+=1
        return count

        