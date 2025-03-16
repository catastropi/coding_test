k = input()

array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
array2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
array3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if k in array:
  for z in range(0, len(array)):
    if k == array[z]:
      print(z+65)
      break
elif k in array2:
  for z in range(0, len(array2)):
    if k == array2[z]:
      print(z+97)
      break  
elif k in array3:
  for z in range(0, len(array3)):
    if k == array3[z]:
      print(z+48)
      break  
