f = open('file.txt', 'w')
f.write('')
f.close()

s = ''
while True:
    s = input('Введите строку: ')

    if s == '/read':
        f = open('file.txt')
        for line in f:
            print(line[:len(s)-1])
        break

    if s != '/exit':
        f = open('file.txt', 'a')
        f.write(s + '\n')
        f.close()
    else:
        break
