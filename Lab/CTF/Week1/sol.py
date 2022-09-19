from codeop import CommandCompiler
from operator import eq
from unicodedata import numeric


set = {}

with open("final.txt", encoding='utf-16') as f:
    for line in f:
        comma_idx = []
        quote_idx = []
        for i in range(len(line)):
            if line[i] == ',':
                comma_idx.append(i)
            elif line[i] == "'":
                quote_idx.append(i)
        if comma_idx == []:
            continue
        idx = int(line[comma_idx[0] + 1: comma_idx[1]])
        number = int(line[quote_idx[0] + 1: quote_idx[1]])
        if idx not in set:
            set[idx] = number
        else:
            if number > set[idx]:
                set[idx] = number
for key, value in set.items():
    print(chr(value), end="")