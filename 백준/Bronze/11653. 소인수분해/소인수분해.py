array = []

i = int(input())

if i == 1:
  print('')
else:
  while True:
    if i == 1:
      break
    else:
      for z in range(2, i+1):
        if i % z == 0:
          array.append(z)
          i //= z
          break
        

for k in array:
  print(k)