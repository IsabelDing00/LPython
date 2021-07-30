# -*- Coding = utf-8 -*-
# @Time:6/15/2021 1:36 AM
# @Author: Isabel Ding
# @File: demo2.py
# @Software: PyCharm

word = "字符串"
sentence = "这是一个句子"
paragraph = '''这是一个段落
            可以自由组成'''

print(word)
print(sentence)
print(paragraph)  # '''可以保留原来的格式

my_str = 'I\'m a student'  # 用\这个作为转义字符
print(my_str)

my_str2 = "Jason said \"I like you\""
print(my_str2)

my_str3 = "HI \\"
print(my_str3)  # HI \
print()


'''
字符串的截取
'''
print("***********************")
print("字符串的连接与截取")
print("***********************")
str = "chengdu"
print('str: ',str)
print('[0:5]:', str[0:5])  # [起始位置：结束位置：步进值]
print('[1:7:2]:',str[1:7:2])
print('[:5]', str[:5])
print('[5:]', str[5:])

print(str + ',你好')
print(str * 3)

print("hello\nchengdu")
print()

print("这个是常用的： r的运用")
print(r"hello\nchengdu")  # 这里的r是说把这个“ ”里的所有的\ 都不转义，直接输出，所以结果是 hello\nchengdu

'''
字符串的常见操作
'''
print("***********************")
print("字符串的常见操作")
print("***********************")

print("bytes.decode(encoding = 'utf-8', error='strict'")
print("encode(encoding='utf-8',error='strict',以encoding指定的编码格式编码字符串， 如果出错默认报一个value error的异常，除非error指定的是ignore或者replace")
print("isalnum()")
print("isalpha()")
print("isdigit() 字符串只包含数字，所以‘四’会报False")
print("isnumeric() string只包含数字字符串， 所以‘四’会报True")
print("join(seq)")
print("len(str)")
print("lstrip() 截掉string左边的空格")
print("rstrip() 戒掉string右边的空格")
print("split(str="", num=string.count(str) num=string.count(str))  拆分string")
print("没了！！！")
