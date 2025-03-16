s = str(input())

array = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
t = len(s)

if 'dz=' in s:
  for i in range(0, len(s)-2):
    if s[i] == 'd':
      if s[i+1] == 'z':
        if s[i+2] == '=':
          t -= 2
      else:
        if s[i+1] == '-':
          t -= 1
    else:
      if s[i] == 'c':
        if s[i+1] == '=' or s[i+1] == '-':
          t -= 1
      elif s[i] == 'l':
        if s[i+1] == 'j':
          t -= 1
      elif s[i] == 'n':
        if s[i+1] == 'j':
          t -= 1
      elif s[i] == 's':
        if s[i+1] == '=':
          t -= 1
      elif s[i] == 'z':
        if i == 0:
          if s[i+1] == '=':
            t -= 1
        else:
          if s[i+1] == '=':
            if s[i-1] == 'd':
              continue
            else:
              t -= 1
  for o in array:
    if s[len(s)-2:len(s)] == o:
      if s[len(s)-2:len(s)] == 'z=' and s[len(s)-3] == 'd':
        continue
      else:
        t -= 1
else:
  for i in range(1, len(s)):
    if s[i] == '=':
      if s[i-1] == 'c' or s[i-1] == 's' or s[i-1] == 'z':
        t -= 1
    elif s[i] == '-':
      if s[i-1] == 'c' or s[i-1] == 'd':
        t -= 1
    elif s[i] == 'j':
      if s[i-1] == 'l' or s[i-1] == 'n':
        t -= 1

print(t)