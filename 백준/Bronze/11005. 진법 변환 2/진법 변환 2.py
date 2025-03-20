dicty = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}

a, b = map(int, input().split())

array,z = [],0

while a > 0:
    if b ** z > a:
      z -= 1
      for key, value in dicty.items():
        if key * (b ** z) > a:
          array.append(dicty[key-1])
          a -= (key-1) * (b ** z)
          break
        elif key * (b ** z) == a:
          array.append(dicty[key])
          for k in range(z):
            array.append('0')
          a = 0
          break
        else:
          if key == 35:
            array.append('Z')
            a -= 35 * b ** z
            break
    elif b ** z == a:
      if z > 0:
        array.append('1')
        for v in range(z):
          array.append('0')
        a = 0
      else:
        array.append('1')
        a = 0
    else:
      if len(array) == 0:
        z += 1

print(''.join(array))