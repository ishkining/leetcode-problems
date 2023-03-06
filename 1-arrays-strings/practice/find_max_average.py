class Solution:
    def find_max_average(self, nums: list[int], k: int) -> float:
        current = 0
        for i in range(k):
            current += nums[i]

        answer = current / k

        for i in range(k, len(nums)):
            current += nums[i] - nums[i - k]
            answer = max(current / k, answer)

        return answer
