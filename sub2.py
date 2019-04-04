import random

print("Type \"q + Enter\" to Quit")
print("Start!")
print()

while True:
    b = random.randrange(1, 10000)
    keta = random.randrange(1, 4)
    if b < 9:
        a = random.randrange(10, 10000)
    elif b < 99:
        a = random.randrange(100, 10000)
    elif b < 999:
        if keta == 1:
            tmp = str(b)
            a = 1000 + int(tmp[len(tmp) - 1])
        elif keta == 1:
            tmp = str(b)
            a = 1000 + int(tmp[len(tmp) - 1]) + 10*int(tmp[len(tmp) - 2])
        else:
            a = 1000
    else:
        tmp = str(b)
        if keta == 1:
            a = 1000*(int(tmp[0]) + 1) + 10*int(tmp[2]) + int(tmp[3])
        elif keta == 2:
            a = 1000*(int(tmp[0]) + 1) + int(tmp[3])
        else:
            a = 1000*(int(tmp[0]) + 1)
            
    print(' ' + str(a))
    print('-' + str(b).rjust(len(str(a))))
    c = input('=')
    if c == 'q':
        break
    while not c.isdecimal():
        print("数値を入力してください!")
        c = input("=")
    c = int(c)
    if (a - b) == c:
        print('せいかい!')
    else:
        print('ざんねん')
    while (a - b) != c:
        c = input('=')
        while not c.isdecimal():
            print("数値を入力してください!")
            c = input("=")
        c = int(c)
        if (a - b) == c:
            print('せいかい!')
        else:
            print('ざんねん')
    print()
    print()
