## Brute force solution: compare each element with all other elements in the array n^2 time complexity
def hasDuplicate(nums: list[int]) -> bool:
    for i in range(len(nums)): # iterate through the list from a certain point
        for j in range(i + 1, len(nums)): # iterate through the list from a number after that first point
            if nums[i] == nums[j]:
                return True
    return False
## Another solution: sort the list and compare numbers side by side nlogn time complexity
def hasDuplicate_2(nums: list[int]) -> bool:
    nums.sort() # nlogn time complexity
    for n in range(len(nums)-1): #stop at second to last element
        if nums[n] == nums[n+1]:
            return True
    return False

## Optimal solution: Use a hash map or a hash set and compare  and store elements
def hasDuplicate_3(nums: list[int]) -> bool:
    checked_numbers = set() # a hash set which makes it time complexity of O(n)
    # and space complexity of O(n) if the list contains n elements
    for num in nums:
        if num in checked_numbers:
            return True
        checked_numbers.add(num) # add this iteration to the set and then move to the next iteration
    return False


if __name__ == '__main__':
    print(hasDuplicate_3([1, 8, 5, 7, 3, 9, 2, 0]))