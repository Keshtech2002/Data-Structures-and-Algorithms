def maxArea(heights: list[int]) -> int:
    """
    Problem:
      Given an array of heights where each element represents a vertical line
      on the x-axis, find two lines that together with the x-axis form a container
      that holds the most water. Return the maximum area.

    Approach:
      - Use two nested loops to try every possible pair of lines (l,r).
      - Compute the area for each pair:
          width = r - l
          height = min(heights[l], heights[r]) (the shorter line limits water)
          area = width * height
      - Keep track of the maximum area found.

    Time Complexity: O(n^2) — check all pairs.
    Space Complexity: O(1).

    Example:
      heights = [1,8,6,2,5,4,8,3,7]
      → 49 (between heights 8 and 7 at distance 7)
    """
    result = 0  # store the maximum area found

    # Try every possible pair of lines
    for l in range(len(heights)):
        for r in range(l+1, len(heights)):
            # Compute area formed by lines at l and r
            area = (r - l) * min(heights[l], heights[r])
            # Update max area if current area is larger
            result = max(area, result)

    return result  # return the maximum area


def maxArea_2(heights: list[int]) -> int:
    """
    Optimized two-pointer approach.

    Problem:
      Same as above — find the maximum area of water that can be contained.

    Approach:
      - Place two pointers at the extremes of the array (left and right).
      - Compute the area between them.
      - Move the pointer pointing to the shorter line inward (because moving
        the taller line cannot increase area — width shrinks but height stays limited).
      - Repeat until pointers meet.

    Time Complexity: O(n) — each pointer moves at most n times.
    Space Complexity: O(1).

    Example:
      heights = [1,8,6,2,5,4,8,3,7]
      → 49
    """
    result = 0  # maximum area found so far

    # Initialize pointers at both ends
    l, r = 0, len(heights) - 1 

    # Loop until pointers meet
    while l < r:
        # Compute area with current left and right pointers
        area = (r - l) * min(heights[l], heights[r])
        result = max(result, area)

        # Move the pointer pointing to the shorter line inward:
        if heights[l] < heights[r]:
            l += 1      # left line is shorter → move left inward
        elif heights[l] > heights[r]:
            r -= 1      # right line is shorter → move right inward
        else:
            # both heights equal — can move either pointer; here we move right
            r -= 1

    return result  # return the maximum area found



if __name__ == '__main__':
    print(maxArea([1,7,2,5,4,7,3,6]))
    print(maxArea_2([1,7,2,5,4,7,3,6]))
    print(maxArea_2([2,2,2]))