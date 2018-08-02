
path_file = r"C:\Users\40664\Desktop\NTU-EXP-CODE-PYTHON\NTU-ML-HW\hw0\words.txt"
f = open(path_file, "r", encoding='utf-8')

lines = f.readlines()  # 读取全部内容

for i in range(0, lines.__len__(), 1):  # (开始/左边界, 结束/右边界, 步长)

    list_words = []  # 空列表, 将第i行数据存入list中
    for word in lines[i].split():  # 将lines中的元素以空格‘ ’分开去，并且遍历每个词
        word = word.strip()  # 每个词去除前后多余符号
        list_words.append(word)


counter = []  # 空列表，将词频放入
j = 0
num = []
for i in set(list_words):

    counter.append(list_words.count(i))  # 将每个词的词频放入列表
    num.append(j)
    j = j+1

set_words = set(list_words)
lists = list(set_words)
for i in range(0, set_words.__len__(), 1):
    print(lists[i], i, counter[i])