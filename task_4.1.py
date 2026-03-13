nums = [0, 1,0,12,3]
zeros_count = 0
while 0 in nums:
    nums.remove(0)
    zeros_count += 1
nums.extend([0]*zeros_count)
print(nums)
