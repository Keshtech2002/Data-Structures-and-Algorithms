def maxArea(heights: list[int]) -> int:
    result = 0

    for l in range(len(heights)):
        for r in range(l+1, len(heights)):
            area = (r - l) * min(heights[l], heights[r])
            result = max(area, result)
    
    return result


def maxArea_2(heights: list[int]) -> int:
    result = 0

    l, r = 0, len(heights) - 1 

    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        result = max(result, area)

        if heights[l] < heights[r]:
            l += 1
        elif heights[l] > heights[r]:
            r -= 1
        else:
            r -= 1

    return result



if __name__ == '__main__':
    print(maxArea([1,7,2,5,4,7,3,6]))
    print(maxArea_2([1,7,2,5,4,7,3,6]))
    print(maxArea_2([2,2,2]))