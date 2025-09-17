def threeSum(nums: list[int]) -> list[list[int]]:
    """
    Problem:
      Given an integer array nums, return all unique triplets [a,b,c] such that:
        a + b + c == 0.

    Approach:
      - Sort the array to make it easier to handle duplicates.
      - Use three nested loops to try every possible triplet (i,j,k).
      - If their sum == 0, add them to a set (using tuple) to avoid duplicates.
      - Convert the set back to a list of lists before returning.

    Time Complexity: O(n^3) — three nested loops.
    Space Complexity: O(k) for storing the results.

    Example:
      nums = [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]
    """
    res = set()             # use a set to store unique triplets (no duplicates)
    nums.sort()             # sort the array so that duplicates line up

    # Try every combination of three different indices i,j,k
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:  # check if sum is zero
                    temp = [nums[i], nums[j], nums[k]]
                    res.add(tuple(temp))             # add as tuple to the set

    # Convert the set of tuples back to a list of lists for the final answer
    return [list(i) for i in res]

def threeSum_2(nums: list[int]) -> list[list[int]]:
    """
    Optimized solution using sorting + two pointers.

    Problem:
      Find all unique triplets in nums where the sum is zero.

    Approach:
      1. Sort nums.
      2. Fix one element nums[i] at a time (the 'first' number).
         - If nums[i] > 0, break early because the rest are positive (no sum=0).
         - Skip duplicates of nums[i] to avoid repeated triplets.
      3. Use two pointers (low and high) to find two other numbers that sum
         to -nums[i]:
         - If sum == 0: record the triplet, move both pointers inward, and skip
           duplicates for low and high.
         - If sum < 0: move low pointer up to increase the sum.
         - If sum > 0: move high pointer down to decrease the sum.

    Time Complexity: O(n^2) — outer loop n, inner two-pointer n.
    Space Complexity: O(k) for storing results.

    Example:
      nums = [-1,0,1,2,-1,-4]
      → [[-1,-1,2],[-1,0,1]]
    """
    nums.sort()             # sort to enable two-pointer technique
    n = len(nums)
    answer = []             # store resulting triplets

    for i in range(n):
        # Early exit: once nums[i] > 0, all subsequent numbers are >= 0 → no sum 0
        if nums[i] > 0:
            break
        # Skip duplicate values for nums[i] to avoid duplicate triplets
        elif i > 0 and nums[i] == nums[i-1]:
            continue

        # Two pointers to find the other two numbers
        low, high = i + 1, n - 1

        while low < high:
            summ = nums[i] + nums[low] + nums[high]

            if summ == 0:
                # Found a valid triplet
                answer.append([nums[i], nums[low], nums[high]])
                # Move pointers inward
                low, high = low + 1, high - 1

                # Skip duplicate numbers for low pointer
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
                # Skip duplicate numbers for high pointer
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1

            elif summ < 0:
                # Sum too small → move low up to increase sum
                low += 1
            else:
                # Sum too large → move high down to decrease sum
                high -= 1

    return answer


if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))
    print(threeSum_2([-1,0,1,2,-1,-4]))