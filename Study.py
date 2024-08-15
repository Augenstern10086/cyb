# -*- coding:UTF-8 -*-
"""
editor:ChangYingbo
date:2024年 07月 16日
"""
#2024.8.13
# print("1 + 1 = ",1 + 1)
# print("2 - 1 = ",2 - 1)
# print("3 * 3 = ",3 * 3)
# print("4 / 2 = ",4 / 2)
# print("11 // 2 = ",11 // 2)
# print("9 % 2 = ",9 % 2)
# print("2 ** 2 = ",2 ** 2)
# """
# number = 1 + 2 * 3
# """
#复合运算符
# num = 1
# num += 1
# print("num +=1: ", num)
# num -= 1
# print("num -=1: ", num)
# num *= 2
# print("num *=2: ", num)
# num **= 2
# print("num **=2: ", num)
# num /= 2
# print("num /=2: ", num)
#单引号定义法
# name = '黑马程序员'
# print(type(name))
# name = "黑马程序员"
# print(type(name))
# """
# 黑马程序员
# """
# print(type(name))
# name = "\"马程序员"
# print(name)
# print("学it来黑马" + "月薪过万")
# name = "黑马程序员"
# address = "河南开封"
# tel = "15137772146"
# print("我是:" + name + ",我的地址是" + address+",我的电话是: " + tel)
# message = "学it来：%s" %name
# print(message)
# class_num = 57
# avg_salary = 16781.28
# message = "大数据学科，北京%d期，毕业平均工资：%.1f" %(class_num, avg_salary)
# print(message)
#2024.8.14
# name = "常英波"
# address = "河南开封"
# price = 20
# print(f"我是{name}，我在{address}，我的价格是{price}")
# print("1 * 1 的结果是: %d" % (1 * 1))
# print(f"1 * 1 的结果是: {1 * 1}")
# print("字符串在python中的类型名是: %s" %type("字符串"))
# name = "传智播客"
# stock_price = 19.99
# stock_code = "003032"
# stock_price_daily_growth_factor = 1.2
# growth_days = 7
# print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
# print("每日增长系数是：%.1f,经过%d天的增长后，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))
# name = input("请告诉我你是谁？")
# print("我知道了，你是：%s"%name)
# num = input("请告诉我你的银行卡密码：")
# num = int(num)
# print("你的银行卡密码的类型是：",type(num))
#获取的数据永远都是字符串
#2024.8.15
# bool_1 = True
# bool_2 = False
# print(f"bool_1变量的内容是：{bool_1},类型是：{type(bool_1)}")
# print(f"bool_2变量的内容是：{bool_2},类型是：{type(bool_2)}")
# #== != > < >= <=
# num1 = 10
# num2 = 10
# print(f"10 == 10的结果是：{num1 == num2}")
# name1 = "cyb"
# name2 = "changyingbo"
# print(f"name1 == name2的结果是：{name1 == name2}")
# num1 = 10
# num2 = 5
# print(f"10 != 5的结果是：{num1 != num2}")
# print(f"10 <= 5的结果是：{num1 <= num2}")
# age = 22
#
# if age >= 18:
#     print(f"我已经{age}岁了，已经成年了")
#     print("即将步入大学生活")
# print("时间过的真快啊")
# print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
# age = int(input("请输入你的年龄:"))
# if age >= 18:
#     print("您已成年，游玩需要补票10元。")
# print("祝您游玩愉快。")
# print("欢迎来到黑马动物园。")
# length = int(input("请输入你的身高(cm):"))
# if length >= 120:
#     print("您的身高超出120cm,游玩需要购票10元。")
# else:
#     print("您的身高未超过120cm,可以免费游玩。")
# print("祝您游玩愉快。")
if int(input("请输入你的身高(cm):")) < 120:
    print("你的身高小于120cm,可以免费。")
elif int(input("请输入你的VIP等级(1-5):")) > 3:
    print("你的VIP等级大于3，可以免费。")
elif int(input("请告诉我今天几号:")) == 1:
    print("今天是1号免费日，可以免费。")
else:
    print("不好意思，条件都不满足，需要买票10元。")