def divisors(start, end, n):
    counter = 0
    for i in range(start, end + 1):
        if i % n == 0:
            counter += 1
              print(i, end=', ')
    print()
    print('There are {} such integers.'.format(counter))
    print()

newdivisor = input('Do you want to enter a range or a divisor? ')

while newdivisor == 'range':
    start = eval(input('Start value: '))
    end = eval(input('End value: '))
    newdivisor = input('Do you want to enter a range or a divisor? ')
    while newdivisor == 'divisor':
        n = eval(input('Divisor: '))
        divisors(start, end, n)
        newdivisor = input('Do you want to enter a range or a divisor? ')
