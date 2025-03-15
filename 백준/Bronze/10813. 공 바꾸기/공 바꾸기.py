N, M = input().split()

array = []


for I in range(1, int(N)+1):
  array.append(I)

array2 = array.copy()

for I in range(1, int(M)+1):
  i, j= input().split()
  array2 = array.copy()
  array[int(i)-1] = array2[int(j)-1]
  array[int(j)-1] = array2[int(i)-1]
  #for m in range(int(i), int(j)+1):
    #array[m-1] = array2[(int(i)-1) + (int(j)-1)-m+1]
    

for o in array:
  print(o, end = " ")