import sys

input = sys.stdin.readline

nums = list(map(lambda x: int(x) ** 2, input().split()))
print(sum(nums) % 10)
