import re
'''
https://blog.csdn.net/guo_qingxia/article/details/113979135
'''
ret = re.match('.', "M")
print(ret) # 打印的是一个对象
print(ret.group())

ret = re.match('h', 'hello python')
print(ret.group())

ret = re.match('\d', '7hello python')
print(ret.group())


ret = re.match('[A-Z][a-z]*', 'Aaa')
print(ret.group())
ret = re.match('[A-Za-z]{1,8}', 'Aaar8wtd')
print(ret.group())


ret = re.match('[\w]{4,20}@163\.com$', '.com.xiaowang@163.com')
# print(ret.group())

ret = re.match('[\w]{4,20}@(126|163)\.(com|edu)$', 'test@163.com')
print(ret.group())
print(ret.group(1))
print(ret.group(2))



# 一个常见的提取坐标的例子，元素符号后面有三个数字表示坐标
ret = re.match('[A-Z][a-z]?\s+(\d*\.\d*)\s+(\d*\.\d*)\s+(\d*\.\d*)$', 'C 1.    20.0000001\t.33')
print(ret.group())
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))

# 一个常见的提取坐标的例子，元素符号后面有三个数字表示坐标
ret = re.findall('[A-Z][a-z]?\s+(\d*\.\d*)\s+(\d*\.\d*)\s+(\d*\.\d*)$', 'C 1.    20.0000001 .33\nCa 2.1    20.0000001 1.33\n', re.MULTILINE)
print(ret[0][0])
print(ret[1][1])


ret = re.findall('[A-Z][a-z]?\s+(.*\..*)\s+(.*\..*)\s+(.*\..*)$', 'C 1.    20.0\n000001 .33\n', re.S)
print(ret[0])
# print(ret[1][1])