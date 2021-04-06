#py2
import string
import random
from secret import flag,b_char

def encode(s):
    res=''
    binstr=[ bin(ord(s[i])).replace('0b','').zfill(8) for i in range(len(s))]
    p1=len(binstr) // 3
    p2=len(binstr) % 3
    part1 = binstr[0:3*p1]
    
    for i in range(p1):
        str_p1=binstr[i*3]+binstr[i*3+1]+binstr[i*3+2]
        tmp_str = [str_p1[x: x + 6] for x in [0, 6, 12, 18]]
        tmp_res = [b_char[int(x,2)]for x in tmp_str]
        res+=''.join(tmp_res)

    if p2:
        part2 = binstr[3*p1:]
        str_p2 = ''.join(part2)+(3-p2)*'0'*8
        tmp_str = [str_p2[x: x + 6] for x in [0, 6, 12, 18]][:p2+1]
        tmp_res = [b_char[int(x,2)]for x in tmp_str]
        res+=''.join(tmp_res)
        res +='='*(3-p2)
    return res
 
m1=random.sample(list(b_char),50)
print ''.join(m1)
print encode(m1)
print encode(flag)
# rTcb1BR8YVW2EOUjweXpIiLt5QCNg7ZAsD9muq3ylMhvofnx/P
# 2Br9y9fcu97zvB2OruZv0D3Bwhbj0uNQnvfdtC2TwAfPrdBJ3xeP4wNn0hzLzCVUlRa=
# tCvM4R3TzvZ7nhjBxSiNyxmP28e7qCjVxQn91SRM3gBKzxQ=