def missingNumbers(nums):
    # Write your code here.
    missing_nums=[]
    # nums=sorted(nums)
    i=0
    current=1
    while i<(len(nums)+2):
        if current not in nums:
            missing_nums.append(current)
        current +=1
        i +=1
    return missing_nums