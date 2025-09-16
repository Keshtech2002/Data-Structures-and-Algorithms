import heapq
from collections import Counter

# Returns the top k most frequents elements from a list of numbers

# Brute force Solution is a dictionary solution or hash map that is sorted by values
# [1, 1, 1, 2, 2, 3], k=2 find the 2 most occuring elements
# A dictionary {1:3, 2:2, 3:1} O(n) then sort by its values {1:3, 2:2, 3:1} O(nlog n)


# Slightly Optimized solution uses heap
# A data structure that sorts a binary tree
def topKFrequent(nums: list[int], k: int) -> list[int]:
    counter = Counter(nums) # [1, 1, 1, 2, 2, 3] -> {num: freq, 1:3, 2:2, 3:1}

    heap = []

    for num, freq in counter.items():
        if len(heap) < k: # We need just k elements in the heap = [(freq, num), (freq, num)] when k = 2
            heapq.heappush(heap, (freq, num)) # Will sort based on the freq when k is still less than 2 else:
        
        else:
            heapq.heappushpop(heap, (freq, num)) # Will add it to the list and remove the current minimum

    return [h[1] for h in heap] # Returns the number in (freq, num)
    # Time: O(n * log n) Space: O(n)


# A more optimized solution at O(n)
def topKFrequent_1(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    counter = Counter(nums) # [1, 1, 1, 2, 2, 3] -> {num: freq, 1:3, 2:2, 3:1}
    buckets = [0] * (n+1) # [1, 2, 3, 4] => [0, 0, 0, 0, 0]

    for num, freq in counter.items():
        if buckets[freq] == 0:
            buckets[freq] = [num] #[1, 2, 3, 4] => [0, 0, 0, 0, 0] => [0, [1], 0, 0, 0] means 1 already occurs once
            # {num: freq, 1:3, 2:2, 3:1} => [0, [3], [2], [1]]
        else:
            buckets[freq].append(num) # {num: freq, 1:3, 2:2, 3:1, 4:1} => [0, [3, 4], [2], [1]] num 4 is appended to the list where 3 is
        
    return_list = []
    for i in range(n, -1, -1): # Iterate from the last element of the list to the first element of the list
        if buckets[i] != 0: # Check if that iteration is not 0
            return_list.extend(buckets[i]) # [1, 2].extend([3, 4]) => [1, 2, 3, 4] 

        if len(return_list) == k:
            break

    return return_list # Time O(n) Space O(n)


if __name__ == '__main__':
    print(topKFrequent([1,2,2,3,3,3], 2))
    print(topKFrequent_1([1,2,2,3,3,3], 2))