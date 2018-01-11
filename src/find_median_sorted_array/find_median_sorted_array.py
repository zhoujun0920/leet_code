# The overall run time complexity should be O(log (m+n)).
def find_median_sorted_arrays(nums1, nums2):
    num = nums1 + nums2
    num.sort()
    m = len(nums1)
    n = len(nums2)
    if (m + n) % 2 == 0:
        return float((num[int((m + n + 1) / 2 - 1)] + num[int((m + n + 1) / 2)]) / 2)
    return float(num[int((m + n) / 2)])

    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """


nums1 = [1, 3]
nums2 = [2]
e1 = 'The median is 2.0'

nums3 = [1, 2]
nums4 = [3, 4]
e2 = 'The median is (2 + 3)/2 = 2.5'

print(find_median_sorted_arrays(nums1, nums2))
print(find_median_sorted_arrays(nums3, nums4))