def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    buffer_dict = {}
    for i in range(len(nums)):
        if nums[i] in buffer_dict:
            return [buffer_dict[nums[i]], i]
        else:
            buffer_dict[nums[i]] = i