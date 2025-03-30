x, y, w, h = map(int, input().split())

array = []

array.append(w-x)
array.append(x-0)
array.append(h-y)
array.append(y-0)

print(min(array))