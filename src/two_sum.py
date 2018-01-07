def two_sum(nums, target):
    current_index = 0
    while len(nums) > 1:
        num1 = nums[0]
        num2 = target - num1
        nums.remove(num1)
        if num2 in nums:
            return [current_index, nums.index(num2) + current_index + 1]
        current_index = current_index + 1
    return []


nums = [3, 2, 4]
target = 6

print(two_sum(nums, target))
