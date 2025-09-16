# A brute force solution would be to check every pair of numbers in the array. This would be an O(n^2)
def twoSum(nums: list[int], target: int) -> list[int]:
    for x in range(len(nums)):
        for y in range(1, len(nums)):
            if nums[y] + nums[x] == target:
                return [x, y]

# Optimal Solution
# we can iterate through nums with index i. Let difference = target - nums[i] 
# and check if difference exists in the hash map as we iterate through the array, 
# else store the current element in the hashmap with its index and continue. We use a hashmap for O(1) lookups.
def twoSum_2(nums: list[int], target: int) -> list[int]:
    holder_map = {} # stores elments that has been iterated against the index {number: index}
    for index, number in enumerate(nums):
        difference = target - number
        if difference in holder_map.keys():
            return [holder_map[difference], index]
        holder_map[number] = index
        



if __name__ == '__main__':
    print(twoSum([1, 8, 5, 7, 3, 9, 2, 0], 9))
    print(twoSum_2([1, 8, 5, 7, 3, 9, 2, 0], 9))