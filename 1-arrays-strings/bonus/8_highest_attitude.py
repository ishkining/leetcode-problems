def largest_altitude(gain: list[int]) -> int:
    prefix_sum = [0, gain[0]]
    for i in range(1, len(gain)):
        prefix_sum.append(gain[i] + prefix_sum[-1])

    return max(prefix_sum)
