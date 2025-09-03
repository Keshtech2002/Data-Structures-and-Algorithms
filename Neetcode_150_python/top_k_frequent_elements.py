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


if __name__ == '__main__':
    print(topKFrequent([1,2,2,3,3,3], 2))