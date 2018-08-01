import numpy as np

path_file = r"C:\Users\lenovo\Desktop\HW0\words.txt"
f = open(path_file, "r", encoding='utf-8')

lines = f.readlines()  # 读取全部内容

for i in range(0, lines.__len__(), 1):  # (开始/左边界, 结束/右边界, 步长)

	list_words = []  # 空列表, 将第i行数据存入list中
	for word in lines[i].split():  # 将lines中的元素以空格‘ ’分开去，并且遍历每个词
		word = word.strip()  # 每个词去除前后多余符号
		list_words.append(word)
	print(list_words)  # 组成列表

counter = []  # 空列表，将词频放入
j = 0
num = []
for i in set(list_words):

	counter.append(list_words.count(i))  # 将每个词的词频放入列表
	num.append(j)
	j = j+1
result = np.zeros(((len(set(list_words))), 3))

set_words = set(list_words)
X = np.array([set_words])
Y = np.array([num])
Z = np.array([counter])


result[:, [0]] = X
result[:, [1]] = Y
result[:, [2]] = Z
1+1