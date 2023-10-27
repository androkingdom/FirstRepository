'''
    1
   2 2
 3    3
4      4
'''

txt = '    '
txt2 = ' '
for i in range(1,5):
    print(f'{txt}{i}',end='')
    txt = txt[:-1]
    if i > 1  :
        for j in range(5-i):
            print(f'{txt2}{i}',end=' ')
            txt2 += '  '
            break
    print()