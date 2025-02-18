def two_sum(nums, target):
    hash_map = {}
    for i,v in enumerate(nums):
        if (target - v) in hash_map:
            return i, hash_map[target - v]
        else:
            hash_map[v] = i


nums = [2,11,6,7,5]
target = 9

print(two_sum(nums, target))

