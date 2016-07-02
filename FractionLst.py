# Print the fraction of numbers in the list that are positive, negative, or zero.

arr = [10, -5, 6, 20, 11, 100]

def fractionList(arr):
  n = len(arr)

  sumPos = 0
  sumNeg = 0
  sumZ = 0

  for i in range(0, n):
    if arr[i] > 0:
      sumPos += 1
    elif arr[i] < 0:
      sumNeg += 1
    else:
      sumZ += 1

  print(sumPos/n)

  print(sumNeg/n)

  print(sumZ/n)

fractionList(arr)
