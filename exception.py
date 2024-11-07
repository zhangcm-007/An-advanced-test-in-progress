"""编写程序，让用户输入两个整数start和end,然后输出这两个整数之间的一个随机数。
要求考虑用户输入不是整数的情况，以及start>end的情况。
根据实际情况进行适当提示或输出。"""
import random


def random_num():
    start = input("请输入开始的数字：")
    end = input ("请输入结束的数字：")
    try:
        if int(start) > int(end):
            raise ValueError("开始值不能大于结束值")
        res = random.randint(int(start), int(end))

    except ValueError as err:
        print(f"输入的值不对{err}")
    except UnboundLocalError as err:
        print(f"不能输入小数{err}")
    try:
        print(res)
    except UnboundLocalError as err:
        print(f"输入错误{err}")

"""
编写一个Python程序，可以执行加法、减法、乘法和除法操作。
用户可以输入两个数字和运算符，然后计算并输出结果。
实现计算器的功能（+、-、*、/），并处理异常情况，
比如：输入的不是数字、除数为0等。"""

def Reckoner(start,operator,end):
   if operator == "+":
       return start + end
   elif operator == "-":
       return start - end
   elif operator == "*":
       return start * end
   else:
       print("输入有误")



if __name__ == '__main__':
    # random_num()
    Reckoner()