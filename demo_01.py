# -*- Coding = utf-8 -*-
# @Time:6/12/2021 1:10 AM
# @Author: Isabel Ding
# @File: demo_01.py
# @Software: PyCharm

print('hello world')

'''
这个打三个单引号就会自动出来后面的三个
上面的 line 1是为了打出来的中午不会显示为乱码
'''

print('我要吃定python')

'''
加入字符串
'''

a = 10
print('This is my a: ', a)

'''
在CMD 里面输入
import keyword
keyword.kwlist
之后回车就可以看到当前你有的python keyword包里有的所有的关键字， 比如'False', 'None', 'True', '__peg_parser__', 'and', 'as'
'''

'''
字符串格式化学习
'''
age = 10.1
print("I am %d years old this year" % age)  # d 是给整数，f 是给小数点

name = "Isabel"
print("My name is %s, I am %d years old" % (name, age))  # 这里name age的顺序不能换

print("www","baidu","com", sep=".")
print("hello", end="")  # 让这个后面的字符串不换行
print("world", end="\t")  # 让后面的字符串 之间有间隔
print("python",end="\n")  # 让后面的字符串换行
print("end")


