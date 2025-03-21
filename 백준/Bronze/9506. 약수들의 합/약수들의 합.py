array, k, marray = 10000 * [0], 0, []


while True:
  i = int(input())
  if i == -1:
    break
  else:
    for u in range(1, i+1):
      if i % u == 0:
        array[k] = u
        k += 1
    if sum(array)-i == i:
      for t in array:
        marray.append(str(t))
        if array.index(t) == array.index(i)-1:
          break
        else:
          marray.append(" + ")
      print("{} = {}".format(i, ''.join(marray)))
      array = 10000 * [0]
      k = 0
      marray = []
    else:
      print("{} is NOT perfect.".format(i))
      array = 10000 * [0] 
      k = 0
      marray = []