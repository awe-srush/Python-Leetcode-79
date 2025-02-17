def containsduplicate(nums):
    seen = set()
    for num in nums:
        seen.add(num)
    if(len(seen) == len(nums)):
        return False
    return True

nums = [3,5,6,7]
print(containsduplicate(nums))