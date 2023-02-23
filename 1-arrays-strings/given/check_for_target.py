def check_for_target(nums: list[int], target :int) -> bool:
    left = 0
    right = len(nums) - 1

    while right > left:
        current_sum = nums[left] + nums[right]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            return True

    return False

