array = []
counta = 0

for i in range(1, 21):  
  subject, st, sc = input().split()
  if sc == 'P':
    continue
  elif sc == 'A+':
    array.append(float(st)*4.5)
    counta += float(st)
  elif sc == 'A0':
    array.append(float(st)*4.0)
    counta += float(st)
  elif sc == 'B+':
    array.append(float(st)*3.5)
    counta += float(st)
  elif sc == 'B0':
    array.append(float(st)*3.0)
    counta += float(st)
  elif sc == 'C+':
    array.append(float(st)*2.5)
    counta += float(st)
  elif sc == 'C0':
    array.append(float(st)*2.0)
    counta += float(st)
  elif sc == 'D+':
    array.append(float(st)*1.5)
    counta += float(st)
  elif sc == 'D0':
    array.append(float(st)*1.0)
    counta += float(st)
  elif sc == 'F':
    array.append(float(st)*0.0)
    counta += float(st)

if counta == 0:
  counta += 1

total = sum(array)
print(float(total/counta))