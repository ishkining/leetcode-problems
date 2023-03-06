class Solution:
    def longest_ones(self, nums: list[int], k: int) -> int:
        left = current = answer = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                current += 1

            while current > k:
                if nums[left] == 0:
                    current -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer
