nums = [0,1,7,2,4,8]
if len(nums) == 0:
    result = 0
else :
    total_sum = 0
for i in range(len(nums)):
    if i % 2 == 0:
        total_sum += nums[i]
last_element = nums[-1]
result = total_sum * last_element
print(result)

