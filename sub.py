import random

print("Type \"q + Enter\" to Quit")
print("Start!")
print()

while True:
    a = random.randrange(1, 10000)
    b = random.randrange(1, 10000)
    if b > a:
        a, b = b, a
    print(' ' + str(a))
    print('-' + str(b).rjust(len(str(a))))
    c = input('=')
    if c == 'q':
        break
    c = int(c)
    if (a - b) == c:
        print('せいかい!')
    else:
        print('ざんねん')
    while (a - b) != c:
        c = int(input('='))
        if (a - b) == c:
            print('せいかい!')
        else:
            print('ざんねん')
    print()
    print()
