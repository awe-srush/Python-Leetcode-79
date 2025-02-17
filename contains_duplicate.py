def containsduplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [3,5,6,7,3]
print(containsduplicate(nums))