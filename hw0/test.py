# -*- coding: utf-8 -*-

with open('words.txt', 'r') as f:
    instr = f.read()
    instr = instr.split()
    d = dict()
    l = list()  # 额外的list存储字符串的顺序信息
    for i in instr:
        if i not in l:
            l.append(i)
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    cnt = 0
    # #打印出来
    # for item in l:
    #     print(item,cnt,d[item])
    #     cnt+=1
    with open('Q1.txt', 'w') as w:
        for item in l:
            tmp = item + " " + str(cnt) + " " + str(d[item]) + "\n"
            w.write(tmp)

1+1