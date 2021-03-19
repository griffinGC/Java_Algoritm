import sys
input = sys.stdin.readline
n = int(input())
rope = [int(input()) for i in range(n)]
rope.sort(reverse=True)
weight = 0
for i in range(len(rope)):
    weight = max(weight, rope[i] * (i + 1))
print(weight)