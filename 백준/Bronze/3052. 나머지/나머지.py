array = [] # 0 0 4 4 0 0 4 0 0 4

for i in range(1, 11):
  k = int(input())
  array.append(k%42)

total = 1
array2 = []

array2.append(array[0])

for k in range(2, 11):
  if array[k-1] not in array2:
    array2.append(array[k-1])
    total += 1
 
print(total)