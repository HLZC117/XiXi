import os
path = os.listdir('img')
head = open('head.txt', 'r')
tail = open('tail.txt', 'r')
txt = head.read()
for i in path:
    txt = txt + '                    ' + "'img/" + i + "',\n"
txt = txt + tail.read()
head.close()
tail.close()
test = open('X.html', 'w', encoding='utf-8') # 若是'wb'就表示写二进制文件
test.write(txt)
test.close()