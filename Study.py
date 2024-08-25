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
# if int(input("请输入你的身高(cm):")) < 120:
#     print("你的身高小于120cm,可以免费。")
# elif int(input("请输入你的VIP等级(1-5):")) > 3:
#     print("你的VIP等级大于3，可以免费。")
# elif int(input("请告诉我今天几号:")) == 1:
#     print("今天是1号免费日，可以免费。")
# else:
#     print("不好意思，条件都不满足，需要买票10元。")
# number = 5
# if int(input("请输入第一次猜想的数字:")) == number:
#     print("你猜对了！")
# elif int(input("不对，再猜一次:")) == number:
#     print("你猜对了！")
# elif int(input("不对，再猜最后一次:")) == number:
#     print("你猜对了！")
# else:
#     print(f"Sorry,全部猜错啦，我想的是:{number}")
# if int(input("你的身高是多少：")) > 120:
#     print("身高超出限制，不可以免费")
#     print("但是，如果vip等级大于3，可以免费")
#
#     if int(input("你的vip等级是多少:")) > 3:
#         print("恭喜你，vip等级达标，可以免费")
#     else:
#         print("Sorry 你需要买票10元")
# else:
#     print("欢迎小朋友，免费游玩.")
#2024.8.16
# import random
# num = random.randint(1,10)
# num1 = int(input("请猜一个数字(1-10):"))
# if num1 > num:
#     print("你猜大了")
#     num2 = int(input("请再猜一个数字(1-10):"))
#     if num2 > num:
#         print("你猜大了")
#         num3 = int(input("请最后再猜一个数字(1-10):"))
#         if num3 > num:
#             print("你猜大了，你的机会用完了！")
#         elif num3 < num:
#             print("你猜小了，你的机会用完了！")
#         else:
#             print("恭喜你，猜对了！")
#     elif num2 < num:
#         print("你猜小了")
#         num3 = int(input("请最后再猜一个数字(1-10):"))
#         if num3 > num:
#             print("你猜大了，你的机会用完了！")
#         elif num3 < num:
#             print("你猜小了，你的机会用完了！")
#         else:
#             print("恭喜你，猜对了！")
#     else:
#         print("恭喜你，猜对了！")
# elif num1 < num:
#     print("你猜小了")
#     num2 = int(input("请再猜一个数字(1-10):"))
#     if num2 > num:
#         print("你猜大了")
#         num3 = int(input("请最后再猜一个数字(1-10):"))
#         if num3 > num:
#             print("你猜大了，你的机会用完了！")
#         elif num3 < num:
#             print("你猜小了，你的机会用完了！")
#         else:
#             print("恭喜你，猜对了！")
#     elif num2 < num:
#         print("你猜小了")
#         num3 = int(input("请最后再猜一个数字(1-10):"))
#         if num3 > num:
#             print("你猜大了，你的机会用完了！")
#         elif num3 < num:
#             print("你猜小了，你的机会用完了！")
#         else:
#             print("恭喜你，猜对了！")
#     else:
#         print("恭喜你，猜对了！")
# else:
#     print("恭喜你，猜对了！")
# import random
# num = random.randint(1,10)
# num_guess = int(input("请输入你要猜测的数字(1-10):"))
# if num == num_guess:
#     print("恭喜你，猜对了！")
# else:
#     if num > num_guess:
#         print("你猜小了！")
#     else:
#         print("你猜大了！")
#     num_guess = int(input("请再次输入你要猜测的数字(1-10):"))
#     if num == num_guess:
#         print("恭喜你，猜对了！")
#     else:
#         if num > num_guess:
#             print("你猜小了！")
#         else:
#             print("你猜大了！")
#         num_guess = int(input("请最后一次输入你要猜测的数字(1-10):"))
#         if num == num_guess:
#             print("恭喜你，猜对了！")
#         else:
#             if num > num_guess:
#                 print("你猜小了！")
#             else:
#                 print("你猜大了！")
# i = 0
# while i < 100:
#     print(f"小美，我喜欢你！{i}")
#     i += 1
#
# i = 1
# sum = 0
# while i<= 100:
#     sum += i
#     i += 1
# import random
# num = random.randint(1,100)
# num_guess = int(input("请输入你猜测的数字(1-100):"))
# count = 1
# while num != num_guess:
#     if num_guess > num:
#         print("你猜大了！")
#     else:
#         print("你猜小了！")
#     num_guess = int(input("请输入你猜测的数字(1-100):"))
#     count += 1
# print(f"恭喜你猜对了！,你总共猜了{count}次  。")
# i = 1
# while i <= 100:
#     print(f"今天是第{i}天，准备表白......")
#     j = 1
#     while j <= 10:
#         print(f"送给小美第{j}朵玫瑰花")
#         j += 1
#     print("小美，我喜欢你！")
#     i += 1
# print(f"坚持到第{i - 1}天，表白成功")
#2024.8.17
# print("Hello",end='')
# print("World",end='')
# print("Hello\tWorld")
# i = 1
# while i <= 9:
#     j = 1
#     while j <=i:
#         print(f"{j}*{i}={j*i}",end="\t")
#         j += 1
#     print("")
#     i += 1
# name = "itheima"
#
# for x in name:
#
#     print(x)
# name = "itheima is a brand of itcast"
# count = 0
# for x in name:
#     if x == 'a':
#         count += 1
# print(f"{name}中共含有：{count}个字母a")
# for x in range(11):
#     print(x)
# for x in range(5,10):
#     print(x)
# for x in range(1,11):
#     print(f"送小美第{x}朵玫瑰花")
# num = 100
# count = 0
# for x in range(1,num):
#     if x % 2 == 0:
#         count += 1
# print(f"1到{num}(不含{num}本身)范围内，有{count}个偶数")
# i = 0
# for i in range(5):
#     print(i)
# print(i)
#2024.8.18
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}",end=" ")
#     print("")
#2024.8.20
# money = 10000
# for i in range(1,21):
#     import random
#     score = random.randint(1,10)
#
#     if score < 5:
#         print(f"员工{i}绩效分:{score}，不满足，不发工资，下一位")
#         continue
#     if money >= 1000:
#         money -= 1000
#         print(f"员工{i}绩效分:{score},满足条件发工资1000,公司账户余额：{money}")
#     else:
#         print(f"余额不足，当前余额：{money}元，不足以发工资，不发了，下个月再来")
#         break
#函数学习
# def say_hi():
#     print("欢迎来到黑马程序员！")
#     print("请出示您的健康码以及72小时核酸证明！")
# say_hi()
#2024.8.24
# def add(x,y):
#     result = x + y
#     print(f"{x} + {y}的结果是{result}")
#
# add(1,2)
# def temp_ad(temp):
#     print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
#     if temp <= 37.5:
#         print(f"体温测量中，您的体温是：{temp}度，体温正常请进!")
#     else:
#         print(f"体温测量中，您的体温是：{temp}度，需要隔离!")
#
#
# temp_ad(37.6)
# def add(a ,b):
#     """
#     add函数可以接收2个参数，进行两数相加的功能
#     :param a: 形参a表示相加的其中一个数字
#     :param b: 形参b表示相加的另外一个数字
#     :return: 返回值是两数相加的结果
#     """
#     result = a + b
#     return result
#
#
# r = add(5, 6)
# print(r)
# def print_1():
#     print("-----2-----")
#
#
# def print_2():
#     print("-----1-----")
#
#     print_1()
#
#     print("-----3-----")
#
#
# print_2()


# #案例：黑马ATM
# money = 5000000
# name = input("您好！欢迎来到黑马ATM，请输入您的姓名：")
#
#
# def ATM_heima():
#     '''
#     黑马ATM：
#     1.查询余额
#     2.存款
#     3.取款
#     4.退出
#     :return: 0
#     '''
#     print("黑马ATM")
#     print("1.查询余额")
#     print("2.存款")
#     print("3.取款")
#     print("4.退出")
#     choice = int(input("请输入您需要的服务所属的序号："))
#     if choice == 1:
#         ATM_check()
#         ATM_heima()
#     elif choice == 2:
#         ATM_in()
#         ATM_heima()
#     elif choice == 3:
#         ATM_out()
#         ATM_heima()
#     else:
#         print("感谢您的使用！欢迎下次光临！")
#
#
# def ATM_check():
#     """
#     取款服务
#     :return:
#     """
#     print(f"尊敬的{name}先生(女士),您的余额是:{money}", )
#     print()
#
#
# def ATM_in():
#     """
#     存款服务
#     :return:
#     """
#     global money
#     money_in = int(input("请输入您要存入的金额:"))
#     money = money + money_in
#     print(f"尊敬的{name}先生(女士),您成功存入{money_in}元，您的余额是:{money}元")
#     print()
#
#
# def ATM_out():
#     """
#     取款服务
#     :return:
#     """
#     global money
#     money_out = int(input("请输入您要取出的金额:"))
#     money = money - money_out
#     print(f"尊敬的{name}先生(女士),您成功取出{money_out}元，您的余额是:{money}元")
#     print()
#
#
# ATM_heima()

#2024.8.25
# my_list = ["itheima", "itcast", "python"]
# print(my_list)
# print(type(my_list))
#
# my_list = ['itheima', 666, True]
# print(my_list)
# print(type(my_list))
#
# my_list = [[1, 2, 3], [4, 5, 6]]
# print(my_list)
# print(type(my_list))
# my_list = ["Tom", "Lily", "Rose"]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# my_list = [[1, 2, 3], [4, 5, 6]]
# print(my_list[1][1])
# my_list = ["Tom", "Lily", "Rose"]
# index = my_list.index("Tom")
# print(index)
# print(f"Tom元素在列表中的下标索引值是:{index}")
#
# my_list[0] = "cyb"
# print(f"修改后的元素列表是{my_list}")
#
# my_list.insert(1, "best")
# print(f"插入新元素后的元素列表是{my_list}")
#
# my_list.append("high")
# print(f"追加新元素后的元素列表是{my_list}")
#
# my_list.extend([4, 5, 6])
# print(f"追加新一批元素后的元素列表是{my_list}")
#
# del my_list[2]
# print(f"列表删除元素后的结果：{my_list}")
#
# element = my_list.pop(2)
# print(f"通过pop方法取出元素后列表内容：{my_list}, 取出的元素是：{element}")
# my_list = ["itcast", "itheima", "itcast", "itheima", "python"]
# my_list.remove("itheima")
# print(f"通过remove方法移除元素后，列表的结果是：{my_list}")
# my_list.clear()
# print(f"列表被清空了，结果是：{my_list}")
#
# my_list = ["itcast", "itheima", "itcast", "itheima", "python"]
# count = my_list.count("itheima")
# print(f"列表中itheima的数量是:{count}")
#
# my_list = ["itcast", "itheima", "itcast", "itheima", "python"]
# count = len(my_list)
# print(f"列表中的元素数量是:{count}")