# import re

# string = "hello\tworld \n I am xiaoming this is 2019 _time_"

#.匹配 ,匹配任意非换行字符
# result = re.findall(r"...",string)
# print(result)

#\w 匹配所有数字,字母,下划线
# result = re.findall(r"\w",string)
# print(result)

#\W 匹配所有非数字,非字母.非下划线
# result = re.findall(r"\W",string)
# print(result)

#\d匹配数字
# result = re.findall(r"\d\d",string)
# print(result)

#\D 非数字
# result = re.findall(r"\D\D",string)
# print(result)

#[] 返回中括号当中任意一个字符
# result = re.findall(r"[hl]",string)
# print(result)

#[^] 返回非中括号中的任意字符
# result = re.findall(r"[^hl]",string)
# print(result)

# | 匹配两边任意一边的字符
# result = re.findall(r"h|l",string)
# print(result)

#() 组匹配,就是将组外的匹配作为条件匹配
# result = re.findall(r"h(\w)",string)
# print(result)

# string= "123 323 536 646"
#() 命名组匹配 给组起名字,然后调用
# result = re.findall(r"(?P<id>\d)\d(?P=id)",string)
# print(result)
