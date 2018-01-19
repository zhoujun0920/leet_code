def max_area(height):
    max_area = 0
    i = 0
    j = len(height) - 1
    while i < j:
        h = min(height[j], height[i])
        area = (j - i) * h
        if max_area < area:
            max_area = area
        while height[i] <= h and i < j:
            i = i + 1
        while height[j] <= h and i < j:
            j = j - 1
    return max_area
