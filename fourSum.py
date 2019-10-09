def fourSum(nums, target):
    def threeSum(nums, target):
        if len(nums) < 3:
            return []
        res = set()
        for i, n in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            t = target - n
            while l < r:
                if nums[l] + nums[r] > t:
                    r -= 1
                elif nums[l] + nums[r] < t:
                    l += 1
                else:
                    res.add((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
        return list(map(list, res))

    results = []
    nums.sort()
    for i in range(len(nums)-3):
        if i == 0 or nums[i] != nums[i-1]:
            threeSumResult = threeSum(nums[i+1:], target-nums[i])
            print(threeSumResult)
            for item in threeSumResult:
                results.append([nums[i]] + item)
    return results

nums = [1,0,-1,0,-2,2]

print(fourSum(nums, 0))
