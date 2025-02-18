def find_all_missing_nums(nums):
    all_nums = set(range(1,len(nums)+1))
    result = []
    for num in all_nums:
        if num not in nums:
            result.append(num)
    return result

nums = [1,2,4,4,4,6,7,8]

print(find_all_missing_nums(nums))
