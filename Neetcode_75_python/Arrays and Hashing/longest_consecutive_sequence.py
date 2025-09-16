# Brute force Solution by sorting
def longestConsecutive(nums: list[int]) -> int:
    """
    Problem:
      Given an unsorted list of integers, return the length of the longest consecutive 
      elements sequence (longest run of numbers that appear consecutively, without gaps).

    Example:
      nums = [100, 4, 200, 1, 3, 2]
      The longest consecutive sequence is [1, 2, 3, 4]
      Answer = 4

    Approach (Sorting-based, O(n log n)):
      1. Edge-case: return 0 if nums is empty.
      2. Sort nums so that consecutive numbers are next to each other.
      3. Iterate through nums while tracking:
         - `current`: the expected number in the ongoing streak
         - `streak`: current streak length
         - `result`: maximum streak length found
      4. Handle duplicates by skipping them inside an inner loop.
      5. Reset streak whenever a gap in numbers is found.
      6. Update result at every step.
      
    Time Complexity: O(n log n) (due to sorting).
    Space Complexity: O(1) extra (ignoring sorting storage).
    """

    # Handle empty input
    if not nums:
        return 0

    # Sort the array so consecutive numbers are adjacent
    # Example: [100, 4, 200, 1, 3, 2] -> [1, 2, 3, 4, 100, 200]
    nums.sort()

    # Initialize variables
    result = 0 # Tracks the maximum streak length seen so far
    current, streak, i = nums[0], 0, 0
    # - current: the next expected number in the streak
    # - streak: length of the current streak
    # - i: index pointer for traversing nums

    # Traverse through nums
    while i < len(nums):

        if current != nums[i]:
            # Case 1: A gap in the sequence (nums[i] is not the expected `current`)
            # - Reset streak because consecutive sequence is broken
            # - Reset current to nums[i] (new sequence starts here)
            current = nums[i]
            streak = 0

        # Skip over duplicates of current value
        while i < len(nums) and nums[i] == current:
            i += 1

        # Extend current streak
        streak += 1 # Found one more consecutive number
        current += 1 # Expect the next integer in sequence

        # Update result with the maximum streak so far
        result = max(result, streak)

    # Return the length of the longest streak found
    return result


# Optimized Solution
def longestConsecutive_2(nums: list[int]) -> int:
    """
    Problem:
      Given an unsorted list of integers, return the length of the longest 
      consecutive elements sequence (longest run of numbers without gaps).
      
    Example:
      nums = [100, 4, 200, 1, 3, 2]
      The longest consecutive sequence is [1, 2, 3, 4]
      Answer = 4

    Approach (O(n) HashSet-based):
      1. Insert all numbers into a set (for O(1) average lookup).
      2. Iterate through each number in the set.
         - If (num - 1) is NOT in the set, then `num` is the *start* of a new sequence.
         - Expand forward (num + 1, num + 2, …) until the sequence ends.
         - Count its length.
         - Update the maximum length found.
      3. Return the longest length.

    Why it works:
      - We only expand sequences from their *starting points* (numbers without a predecessor).
      - Each number is visited once in expansion → total O(n) complexity.

    Time Complexity: O(n) on average (HashSet lookups).
    Space Complexity: O(n) for storing the set.
    """

    # Store all numbers in a set for fast O(1) membership checks
    numSet = set(nums)

    # Initialize the longest streak length
    longest = 0

    # Iterate through each unique number in the set
    for num in numSet:
        # Only start a sequence if `num` is the *beginning*
        # i.e., `num - 1` is not in the set → ensures we don't recount from the middle
        if (num - 1) not in numSet:

            # Start of a new sequence
            length = 1   # current sequence length

            # Expand forward while the next consecutive number exists in the set
            # Example: if num = 1 and 2,3,4 are in the set → keep going
            while (num + length) in numSet:
                length += 1

            # Update the longest streak found so far
            longest = max(longest, length)

    # Step 3: Return the maximum streak length
    return longest



if __name__ == "__main__":
    print(longestConsecutive([2,20,4,10,3,4,5]))
    print(longestConsecutive_2([2,20,4,10,3,4,5]))
