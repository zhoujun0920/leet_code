def two_sum(nums, target):
    look_for = {}
    for n, x in enumerate(nums):
        try:
            return look_for[x], n
        except KeyError:
            look_for.setdefault(target - x, n)
            
nums = [3, 2, 4]
target = 6

print(two_sum(nums, target))
