def nums_smaller_than(nums):
    temp = sorted(nums)
    result = []
    hash_map = {}
    for i, num in enumerate(temp):
        if num not in hash_map:
            hash_map[num] = i
    
    for num in nums:
        result.append(hash_map[num])
    return result


nums = [1,8,4,3,4]
print(nums_smaller_than(nums))