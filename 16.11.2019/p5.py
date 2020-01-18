def shorter(s):
    current_letter = ''
    counter = 0
    res = ''

    for i in range(len(s)):
        if (current_letter != s[i]) or (i == len(s)-1):

            if i == len(s) - 1:
                counter = counter + 1

            if counter == 1:
                res = res + current_letter
            if counter > 1:
                res = res + current_letter + str(counter)

            counter = 1
            current_letter = s[i]
        else:
            counter = counter + 1

    return res

print(shorter('AAAAABBBBBYYOOCZGGGGGGGGGG'))
print(shorter('AAG'))