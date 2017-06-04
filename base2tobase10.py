#convert base 2 to decimal
def foo(num):
    # a small program that takes in the string representation of a bitwise number and prints it out using decimal
    
    #This can also be done using the 0b notation in Java: https://github.com/annehuang/Data-structures-and-Programming-Fundamentals-in-Java/blob/master/BitwiseManipulation.java
    j = 0
    sum1 = 0
    for i in range(len(num) -1, -1, -1):
        sum1 += int(num[i]) * 2**j # adds the value of each bit
        print('{:d}: {:d}'.format(j, sum1)) # sum so far
        j+= 1
    print('{:x}'.format(sum1))
