a1, a = map(int, input().split())
c = int(input())
n0 = int(input())

n = n0

#7n + 7 <= 8n, n >= n0
while True:
  if a1 < c:
    if a <= 0:
      print(1)
      break
    else:
      if (a % (c-a1)) != 0:
        if n0 <= ((a // (c-a1))):
          print(0)
          break
        else:
          print(1)
          break
      else:
        if n0 <= ((a // (c-a1))-1):
          print(0)
          break
        else:
          print(1)
          break
  elif a1 == c:
    if a <= 0:
      print(1)
      break
    else:
      print(0)
      break
  else:
    print(0)
    break