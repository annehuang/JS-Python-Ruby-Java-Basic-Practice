a = [[9, 44, 9], [99, 3, 9], [10, 3, 2]]

n = len(a)

sumA = 0
for i in range(0, n):
    sumA += a[i][i]
sumB = 0

for i in range(0, n):
    sumB += a[i][n-1-i]

print(abs(sumA - sumB))
