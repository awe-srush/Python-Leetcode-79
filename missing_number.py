def missing_number(nums):
    return sum(range(len(nums) +1)) - sum(nums)

nums = [3,0,1,2]
print(missing_number(nums))