import keyword

# 读取文件
with open('random_int.py', 'r') as f:
    content = f.readlines()

# 处理每一行内容
new_content = []
for line in content:
    words = line.split()
    new_words = []
    for word in words:
        # 判断是否为保留字
        if keyword.iskeyword(word):
            new_words.append(word)
        else:
            # 非保留字的小写字母转为大写
            new_words.append(word.upper())
    # 重组行内容
    new_line = ' '.join(new_words) + '\n'
    new_content.append(new_line)

# 保存到新文件
with open('random_int_converted.py', 'w') as f:
    f.writelines(new_content)
