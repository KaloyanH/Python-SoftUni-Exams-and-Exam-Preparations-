def find_valid_subsets(nums, target):
    def backtrack(start, subset, current_sum):
        if current_sum <= target:
            result.append(subset[:])
        for i in range(start, len(nums)):
            subset.append(nums[i])
            current_sum += nums[i]
            backtrack(i + 1, subset, current_sum)
            subset.pop()
            current_sum -= nums[i]

    result = []
    backtrack(0, [], 0)
    return result


nums = list(map(int, input().split(", ")))
target = int(input())

subsets = find_valid_subsets(nums, target)

for subset in subsets:
    if subset:
        print(" ".join(map(str, subset)))
