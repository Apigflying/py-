# 内置函数 
# abs - 取绝对值 
# int - 取整 
# float - 转换小数 
# str - 转换成字符串
# bool - 转换成布尔值
import math

# def quadratic(a, b, c):
#   culp = ((-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a))
#   print(culp)
#   return culp
# # 测试:

# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')
# print('a')

def fn(arg = []):
    arg.append('abc')
    return arg
print(fn()) #['abc']
print(fn()) #['abc','abc']
print(fn()) #['abc','abc','abc']