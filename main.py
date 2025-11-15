import keyword
import re

def convert_case(input_file, output_file):
    # 读取原文件内容
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 正则表达式匹配单词（考虑字母、数字、下划线组成的标识符）
    pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    
    def replace_word(match):
        word = match.group()
        # 保留字不转换，其他单词转为大写
        if keyword.iskeyword(word):
            return word
        else:
            return word.upper()
    
    # 替换所有符合规则的单词
    converted_content = re.sub(pattern, replace_word, content)
    
    # 保存转换后的内容
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted_content)

# 执行转换：读取random_int.py，输出到converted_random_int.py
convert_case('random_int.py', 'converted_random_int.py')
