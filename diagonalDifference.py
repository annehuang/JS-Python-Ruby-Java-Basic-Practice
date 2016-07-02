a = [[9, 44, 9], [99, 3, 9], [10, 3, 2]]

# pre: a is a 3*3 2-D array of integers
def diagonalDifference(a):
    n = len(a)

    sumA = 0
    for i in range(0, n):
        sumA += a[i][i]
    # find the sum of all the entries in the diagonal that begins in the upper left corner

    sumB = 0
    for i in range(0, n):
        sumB += a[i][n-1-i]
    # find the sume of all the entries in the diagonal that begins in the upper right corner

    print(abs(sumA - sumB))
    # print the absolute difference between the 2 diagonals

diagonalDifference(a)
