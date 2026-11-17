A, B, C = map(int, input().split())
k = (A // C) * (B // C)
print(k, A * B - k * C * C)