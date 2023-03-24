def longest_common_substring(strings, start, end):
    if start >= end:
        return ""
    elif start == end - 1:
        return strings[start]
    else:
        mid = (start + end) // 2
        left = longest_common_substring(strings, start, mid)
        right = longest_common_substring(strings, mid, end)
        result = ""
    for i in range(min(len(left), len(right))):
        if left[i] == right[i]:
            result += left[i]
        else:
            break
    return result
strings = ["programmable", "programming", "programmer", "programmatic"
"programmability"]
print(longest_common_substring(strings, 0, len(strings)))

def max_profit_divide_and_conquer(prices):
  if len(prices) <= 1:
    return 0
  mid = len(prices) 
  left_profit = max_profit_divide_and_conquer(prices[:mid])
  right_profit = max_profit_divide_and_conquer(prices[mid:])
  cross_profit = max(prices[mid:]) - min(prices[:mid])
  return max(left_profit, right_profit, cross_profit)

def max_profit_linear(prices):
  min_price = prices[0]
  max_profit = 0
  for price in prices[1:]:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)
  return max_profit

def longest_increasing_subarray(arr):
  n = len(arr)
  dp = [1] * n
  for i in range(1, n):
    for j in range(i-1, -1, -1):
      if arr[j] < arr[i]:
        dp[i] = max(dp[i], dp[j] + 1)
  return max(dp)

print(longest_increasing_subarray([1, 4, 5, 2, 4, 3, 6, 7, 1, 2, 3, 4, 7]))
print(longest_increasing_subarray([1, 2, 3, 4, 1, 2, 3, 5, 2, 3, 4]))
