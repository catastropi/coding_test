import math

A, B, V = map(int, input().split())

AV = V-A

print(math.ceil(AV/(A-B))+1)