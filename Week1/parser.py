from hashlib import new
from lib2to3.pgen2.token import NEWLINE
from operator import ne
from re import T


source = []

# 读取所有含有 sleep 的行
with open ("json.txt", encoding='utf-8') as f:
    for line in f:
        if 'sleep' in line:
            source.append(line.strip())

# 按照HTTP标记格式逐行解析
has = True
cnt = 0
while has:
    cnt = cnt + 1
    has = False
    for i in range(len(source)):
        line = source[i]
        
        new_line = ''
        j = 0
        while j < len(line):
            str = line[j:j+3]
            if line[j] == '%':
                if str == '%25':
                    new_line = new_line + '%'
                    has = True
                    j = j + 3
                elif str == '%20':
                    new_line = new_line + ' '
                    has = True
                    j = j + 3
                elif str == '%2F':
                    new_line = new_line + '/'
                    has = True
                    j = j + 3
                elif str == '%3A':
                    new_line = new_line + ':'
                    has = True
                    j = j + 3
                elif str == '%3D':
                    new_line = new_line + '='
                    has = True
                    j = j + 3
                elif str == '%22':
                    new_line = new_line + '"'
                    has = True
                    j = j + 3
                elif str == '%23':
                    new_line = new_line + '#'
                    has = True
                    j = j + 3
                elif str == '%26':
                    new_line = new_line + '&'
                    has = True
                    j = j + 3
                elif str == '%28':
                    new_line = new_line + '('
                    has = True
                    j = j + 3
                elif str == '%29':
                    new_line = new_line + ')'
                    has = True
                    j = j + 3
                elif str == '%2B':
                    new_line = new_line + '+'
                    has = True
                    j = j + 3
                elif str == '%2C':
                    new_line = new_line + ','
                    has = True
                    j = j + 3
                elif str == '%0d':
                    j = j + 3
                    new_line = new_line + '\r'
                    has = True
                elif str == '%0a':
                    j = j + 3
                    new_line = new_line + '\n'
                    has = True
                elif str == '%27':
                    j = j + 3
                    new_line = new_line + "'"
                    has = True
                else:
                    print(str)
            else:
                new_line = new_line + line[j]
                j = j + 1
        source[i] = new_line

for line in source:
    if 'sleep' in line:
        print(line)




