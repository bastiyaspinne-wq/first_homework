nums = [1,2,3,4,5,6]
middle_index = len(nums)//2
if len (nums) != 0:
    middle_index += 1
part1 =nums[:middle_index]
part2 =nums[middle_index:]
print(part1)
print(part2)
result = [part1,part2]
print(result)
