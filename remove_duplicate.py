def removeDuplicates(nums) -> int:
    last = -10
    lst = []
    for i in nums:
        print(i)
        if i != last:
            last = i
        else:
            lst.append(nums.index(i))
            last = i
        print(nums)
    for i in lst[::-1]:
        nums.pop(i)
    print(nums)
    return len(list(set(nums)))

# test
nums = [1,1,2]
print(removeDuplicates(nums))
# test 2
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

