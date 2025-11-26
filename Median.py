def sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

def Median(n, nums):
    if n % 2 == 0:
        median = nums[n//2 - 1]
    else:
        median = nums[n//2]
    return median

n = int(input())
nums = list(map(int, input().split()))
nums = sort(nums)
print(Median(n, nums))