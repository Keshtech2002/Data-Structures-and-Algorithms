def threeSum(nums: list[int]) -> list[list[int]]:
    res = set()
    nums.sort()

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    res.add(tuple(temp))
    return [list(i) for i in res]


if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))