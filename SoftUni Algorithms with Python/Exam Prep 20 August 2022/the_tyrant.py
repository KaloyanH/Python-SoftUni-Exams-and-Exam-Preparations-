def min_sum_subsequence_with_group_of_four(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i >= 4:
            dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 3], dp[i - 4]) + arr[i - 1]
        elif i == 3:
            dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 3]) + arr[i - 1]
        elif i == 2:
            dp[i] = min(dp[i - 1], dp[i - 2]) + arr[i - 1]
        else:
            dp[i] = dp[i - 1] + arr[i - 1]

    return min(dp[-1], dp[-2], dp[-3], dp[-4])


input_array = [int(x) for x in input().split()]
result = min_sum_subsequence_with_group_of_four(input_array)
print(result)
