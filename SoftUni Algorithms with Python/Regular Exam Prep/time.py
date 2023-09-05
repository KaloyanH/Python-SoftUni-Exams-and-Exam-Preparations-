def longest_common_subsequence(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    common_length = dp[n][m]
    common_timeline = []

    i, j = n, m
    while i > 0 and j > 0:
        if arr1[i - 1] == arr2[j - 1]:
            common_timeline.append(arr1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    common_timeline.reverse()

    return common_timeline, common_length

timeline1 = list(map(int, input().split()))
timeline2 = list(map(int, input().split()))

common_timeline, common_length = longest_common_subsequence(timeline1, timeline2)

print(" ".join(map(str, common_timeline)))
print(common_length)
