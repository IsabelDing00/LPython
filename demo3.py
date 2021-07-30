# -*- Coding = utf-8 -*-
# @Time:6/15/2021 2:08 AM
# @Author: Isabel Ding
# @File: demo3.py
# @Software: PyCharm

testlist = [1, "测试"]   #列表中可以储存混合类型，如这里的int 和str
print(testlist[0])
print(testlist[1])
print("**********************")

'''

'''
print("用for loop直接打印出来list里的东西，但是用while可以结合下标来做更多的动作")
print("**********************")
namelist = ["小张", "小王", "小李"]
for name in namelist:
    print(name)

print("用while")
length = len(namelist)
i = 0
while i < length:
    print(namelist[i])
    i += 1

'''
增删改查
'''
# 增： [append] 在末尾增加一个元素
print("------增加前，名单数据列表------")
for name in namelist:
    print(name)

'''
nametemp = input("请增加学生的姓名： ")
namelist.append(nametemp)

print("------增加后，名单数据列表------")
for name in namelist:
    print(name)
'''

'''
增： [append] 末尾加入；
    [extend] 扩展；
    [insert] 插入
'''
# 增： [append] 末尾加入
a = [1, 2]
b = [3, 4]
a.append(b)   # 结果是[1, 2, [3, 4]], 因为将b列表作为一个新的元素加入列表 **整体加入**
print(a)

# 增： [extend] 扩展
a.extend(b)   # 扩展的意思，[1, 2, [3, 4], 3, 4]，将b列表里的元素一次加入  **拆开一次加入**
print(a)

# 增：[insert] 插入
a = [0, 1, 2]
a.insert(1, 3)  # insert(下标,元素)
print(a)        # 在指定下标插入元素，结果为[0, 3, 1, 2]

'''
删： [del] 指定删除；
    [pop] 弹出末尾元素；
    [remove] 移除元素内容
'''
# 删： [del]
movieName = ["加勒比海盗", "黑客帝国", "Harry Potter", "指环王", "Zootopia"]
print("------删除前，电影表------")
for name in movieName:
    print(name)

# del movieName[2]          # 在指定下标删除元素
# movieName.pop()           # 弹出末尾最后一个元素
movieName.remove("指环王")   # 直接删除指定内容的元素(不会删掉重复的元素，只会删掉重读中的第一个） **列表可以有重复的元素，但会用下标区分

print("------删除后，电影表------")
for name in movieName:
    print(name)

'''
改： 
'''
print("------修改前，名单数据列表------")
for name in namelist:
    print(name)

namelist[1] = "小红"     # 指定下标修改
print("------修改后，名单数据列表------")
for name in namelist:
    print(name)

'''
查： 
'''