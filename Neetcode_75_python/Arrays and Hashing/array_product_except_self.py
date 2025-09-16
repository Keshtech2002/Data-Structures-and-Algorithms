# an array [1, 2, 3, 4] ==> [24, 12, 8, 6] as a result of [2*3*4, 1*3*4, 1*2*4, 1*2*3]
# A brute force solution is to iterate through all the elements in the array one by one 
# For every iteration multiply every number in the array and divide by the current iteration element of the array
# Example is [1, 2, 3, 4] for the last iteration i.e iteration for element 4 => 1*2*3*4 / 4
#  
# But at the moment the constraint given is to not use a division operator

# Another brute force solution O(n**2) 
def productExceptSelf(nums: list[int]) -> list[int]:
    product_list = [1] * len(nums) # Initialize the list of products with 1 and the length must be equal to the length of the initial list
    for i in range(len(nums)): # i to iterate the list first time and it serves as a pointer to which element we are not multiplying
        for j in range(len(nums)): # j is to iterate the list after i and j serves as the iterator to multiply
            if i != j: # Here whenever i = j it means that they are pointing to the same number on the array and that is the number j does not want to multiply but it wants to multiply the rest
                product_list[i] *= nums[j]
    return product_list


def productExceptSelf_2(nums: list[int]) -> list[int]:
    """
    Return an array answer such that answer[i] is the product of all elements in nums
    except nums[i], WITHOUT using division and in O(n) time.
    
    Approach summary:
      - Build left_array where left_array[i] = product of all nums before index i (prefix product)
      - Build right_array where right_array[i] = product of all nums after index i (suffix product)
      - The answer for index i is left_array[i] * right_array[i]

    Time complexity: O(n) — single loop of length n plus one more linear comprehension to multiply arrays.

    Space complexity: O(n) extra — two auxiliary arrays left_array and right_array
    
    Example:
      nums = [1, 2, 4, 6]
      left_array  (prefix products)  = [1, 1, 2, 8]
      right_array (suffix products)  = [48, 24, 6, 1]
      result = [48, 24, 12, 8]
    """
    # running product of numbers to the right (used to fill right_array)
    multiply_right = 1

    # running product of numbers to the left (used to fill left_array)
    multiply_left = 1

    # length of input
    n = len(nums)

    # initialize arrays with 1s. these will store the prefix and suffix products.
    # They must be length n so we can later multiply them elementwise.
    left_array = [1] * n   # left_array[i] will become product of nums[0..i-1]
    right_array = [1] * n  # right_array[i] will become product of nums[i+1..n-1]

    # single loop that fills both left_array (forward) and right_array (backward) simultaneously.
    # Using negative indexing for the backward side:
    #   j = -i - 1 maps i=0 -> j=-1 (last index), i=1 -> j=-2 (second last), etc.
    for i in range(n):
        j = -i - 1

        # store the current left-side running product into left_array[i]
        # At this moment multiply_left is product of all nums before index i
        left_array[i] = multiply_left

        # store the current right-side running product into right_array[j]
        # multiply_right is product of all nums after index j (which corresponds to the mirrored index)
        right_array[j] = multiply_right

        # update running products for next iterations:
        # multiply_left accumulates product from the left moving forward
        multiply_left *= nums[i]

        # multiply_right accumulates product from the right moving backward
        multiply_right *= nums[j]

    # multiply corresponding prefix and suffix products to get final result
    # zip(left_array, right_array) pairs the two arrays elementwise
    return [l * r for l, r in zip(left_array, right_array)]


def productExceptSelf_optimized(nums: list[int]) -> list[int]:
    """
    Return an array 'res' such that res[i] is the product of all elements in nums
    except nums[i], without using division and in O(n) time.
    
    Time Complexity: O(n) — two linear sweeps (forward + backward).
    Space: O(1) extra (excluding the output array).
    Approach:
      1. Write prefix products into res: res[i] = product(nums[0..i-1])
      2. Use a single right-product variable R to multiply res[i] by product(nums[i+1..n-1])
    
    Example:
      nums = [1, 2, 4, 6] -> returns [48, 24, 12, 8]
    """
    n = len(nums)

    # Edge-case: if the list is empty, return empty list
    if n == 0:
        return []

    # Step 0: prepare the output list.
    # We'll store prefix products in res first, then multiply in-place by suffix products.
    res = [1] * n  # res[i] will hold the final result at the end

    # ---------- Forward pass: write prefix products into res ----------
    # After this loop: res[i] == product of all nums before index i (nums[0..i-1])
    left_running = 1  # running product of all elements to the left of current index
    for i in range(n):
        # At this moment left_running == product(nums[0..i-1])
        res[i] = left_running

        # Update left_running to include nums[i] for the next index
        left_running *= nums[i]

    # ---------- Backward pass: multiply suffix products using one variable ----------
    # We'll walk from right to left and keep a running product of elements to the right.
    right_running = 1  # running product of all elements to the right of current index
    for i in range(n - 1, -1, -1):
        # Multiply res[i] (which currently holds the left-product) by right_running
        # right_running == product(nums[i+1..n-1])
        res[i] *= right_running

        # Update right_running to include nums[i] so it becomes product(nums[i..n-1])
        right_running *= nums[i]

    # res now contains the product of all elements except the one at each index
    return res

if __name__ == '__main__':
    print(productExceptSelf([1,2,4,6]))
    print(productExceptSelf_2([1,2,4,6]))
    print(productExceptSelf_optimized([1,2,4,6]))