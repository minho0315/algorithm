# n = 1260
# count = 0

# coin_types = [500,50,10]

# for coin in coin_types:
#   count += (n // coin)
#   n %= coin

# print(count)


# # 큰수의 법칙
# n,m,k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# result = 0

# while True:
#   for i in range(k):
#     if m == 0:
#       break
#     result += first
#     m -= 1
#   if m == 0:
#     break
#   result += second
#   m -= 1

# print(result)

# # 숫자 카드 게임
# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#   data = list(map(int, input().split()))
#   min_value = min(data)

#   result = max(result, min_value)

# print(result)

# 1이 될 때까지
n, k = map(int, input().split())
result = 0

while n >= k:
  while n % k != 0:
    n -=1
    result += 1
  n //= k
  result += 1

while n > 1:
  n -= 1
  result += 1


print(result)