def removeDuplicates(nums) -> int:
    last = -1000
    k = 0
    for i in range(len(nums)):
        if nums[i] != last:
            last = nums[i]
            k += 1
        else:
            nums[i] = 1000
    nums.sort()

    return k

# test
nums = [1,1,2]
print(removeDuplicates(nums))
# test 2
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

