def answer_queries(nums: list[int], queries: list[list[int]], limit: int ) -> list[bool]:
    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[-1])

    answer = []
    for x, y in queries:
        current = prefix_sum[y] - prefix_sum[x] + nums[x]
        answer.append(current < limit)

    return answer