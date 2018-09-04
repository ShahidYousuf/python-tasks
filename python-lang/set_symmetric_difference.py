m = int(input())
M = set(list(map(int, input().split()))[:m])
n = int(input())
N = set(list(map(int, input().split()))[:n])
d = M ^ N
for item in sorted(d):
    print(item)
