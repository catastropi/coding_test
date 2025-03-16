Str = input().split()

array = []
l = []

for t in range(1, len(Str)):
  if '*' not in Str[t] and '&' not in Str[t] and '[' not in Str[t]:
    array.append(Str[0]+" "+Str[t][0:len(Str[t])-1]+";")
  else:  
    for z in range(0, len(Str[t])-1):
      if Str[t][z] == '*' or Str[t][z] == '[' or Str[t][z] == '&':
        x = z
        break
    for y in range(x, len(Str[t])):
      l.append(Str[t][x+len(Str[t])-1-y])
    l.remove(l[0])
    for i in range(0, len(l)):
      if l[i] == ']':
        l[i] = '['
      elif l[i] == '[':
        l[i] = ']'
    r = ''.join(l)
    l.clear()
    array.append(Str[0]+r+" "+Str[t][0:x]+";")

for n in array:
  print(n)