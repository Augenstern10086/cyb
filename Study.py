# -*- coding:UTF-8 -*-
"""
editor:ChangYingbo
date:2024年 07月 16日
"""
import time


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
#
# student_age = [21, 25, 21, 23, 22, 20]
#
# student_age.append(31)
# print(f"追加数字31后，列表为:{student_age}")
#
# student_age.extend([29, 33, 30])
# print(f"追加新列表后，列表为:{student_age}")
#
# number1 = student_age.pop(0)
# print(f"取出的第一个元素为{number1}")
#
# number2 = student_age.pop(-1)
# print(f"取出的最后一个元素为{number2}")
#
# index = student_age.index(31)
# print(f"元素31在列表中的位置是{index}")
# def list_while_func():
#     index = 0
#     list1 = ["敦煌四中", "南街小学", "酒泉市"]
#     while index < len(list1):
#         element = list1[index]
#         print(f"列表的元素:{element}")
#         index += 1
#
#
# list_while_func()


# def list_for_func():
#     list1 = ["敦煌四中", "南街小学", "酒泉市"]
#     for element in list1:
#         print(f"列表的元素:{element}")
#
#
# list_for_func()

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def list_while_func(list_1):
#     index = 0
#     list_2 = []
#     while index < len(list_1):
#         if list_1[index] % 2 == 0:
#             list_2.append(list_1[index])
#         index += 1
#     print(f"通过while循环，从列表：{list_1}中取出偶数，组成新列表：{list_2}")
#
#
# list_while_func(my_list)
#2024.08.29
# t1 = (1, "hello", True)
# t2 = ()
# t3 = tuple()
# print(f"t1的类型是{type(t1)},内容是{t1}")
# print(f"t2的类型是{type(t2)},内容是{t2}")
# print(f"t3的类型是{type(t3)},内容是{t3}")
#
# t4 = ("hello",)
# print(f"t4的类型是{type(t4)},内容是{t4}")
#
# t5 = ((1, 2, 3), (4, 5, 6), ())
# print(f"t5的类型是{type(t5)},内容是{t5}")
#
# num = t5[1][2]
# print(f"从嵌套元组中取出的数据是{num}")
#
# t6 = ("传智教育", "黑马程序员", "Python")
# index = t6.index("黑马程序员")
# print(f"在元组t6中查找黑马程序员的下标是:{index}")
# t7 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
# num = t7.count("黑马程序员")
# print(f"在元组t7中查找黑马程序员的数量有{num}个")
# num1 = len(t7)
# print(f"t7中的元素有:{num1}个")
# index = 0
# while index < len(t7):
#     print(f"元组的元素有:{t7[index]}")
#     index += 1
#
# for element in t7:
#     print(f"2元组的元素有:{element}")
#
# t9 = (1, 2, ["itheima", "itcast"])
# print(f"t9的内容是：{t9}")
# t9[2][0] = "1"
# print(f"t9的内容是：{t9}")
# t1 = ("周杰伦", 11, ["football", "music"])
#
# num = t1.index(11)
# print(f"年龄所在位置:{num}")
#
# name = t1[0]
# print(f"学生的姓名是:{name}")
#
# t1[2].remove("football")
# print(f"删除football后，t1为：{t1}")
#
# t1[2].append("coding")
# print(f"增加coding后，t1为：{t1}")
#2024.8.30
# my_str = "itheima and itcast"

# value = my_str[2]
#
# value2 = my_str[-16]
#
# print(f"从字符串{my_str}取下标为2的元素，值为：{value}")
# print(f"从字符串{my_str}取下标为-16的元素，值为：{value2}")

# my_str[2] = "H"

# value = my_str.index("and")
# print(f"在字符串{my_str}中查找and,其起始下标是:{value}")
#
# new_my_str = my_str.replace("it", "程序")
# print(f"将字符串{my_str},进行替换后得到：{new_my_str}")

# my_str = "hello python itheima itcast"
# my_str_list = my_str.split(" ")
# print(f"将字符串{my_str}进行split切分后得到：{my_str_list}")

# my_str = "12itheima and itcast21"
# new_my_str = my_str.strip("12")
# print(f"字符串{my_str}被strip(12)后，结果：{new_my_str}")
# number1 = my_str.count('1')
# number2 = len(my_str)
# print(f"字符串{my_str}中‘1’出现的次数是{number1}")
# print(f"字符串{my_str}的长度是是{number2}")

# my_str = "黑马程序员"
# index = 0
# while index < len(my_str):
#     print(my_str[index])
#     index += 1
# my_str = "黑马程序员"
# for index in my_str:
#     print(index)
# my_str = "itheima itcast boxuegu"
# number_it = my_str.count("it")
# new_my_str = my_str.replace(" ","|")
# new_my_str_list = new_my_str.split("|")
# print(f"字符串{my_str}中有:{number_it}个it字符")
# print(f"字符串{my_str},被替换空格后，结果：{new_my_str}")
# print(f"字符串{new_my_str},被|分隔后，得到:{new_my_str_list}")
# my_list = [0, 1, 2, 3, 4, 5, 6]
# result1 = my_list[1:6:2]
# print(f"结果1:{result1}")
#
# my_tuple = (0, 1, 2, 3, 4, 5, 6)
# result2 = my_tuple[::2]
# print(f"结果2:{result2}")
#
# my_str = ("012345670")
# result3 =my_str[::3]
# print(f"结果3:{result3}")
#
# my_str = ("012345670")
# result4 =my_str[::-1]
# print(f"结果4:{result4}")
#
# my_list = [0, 1, 2, 3, 4, 5, 6]
# result5 = my_list[3:1:-1]
# print(f"结果5:{result5}")
#
# my_tuple = (0, 1, 2, 3, 4, 5, 6)
# result6 = my_tuple[::-2]
# print(f"结果6:{result6}")

# my_str = "万过薪月，员序程马黑，nohtyP学"
# new_my_str = my_str[-9:-14:-1]
# print(new_my_str)
#
# my_str_list = my_str.split("，")
# new_my_str_1 = my_str_list[1][::-1]
# print(new_my_str_1)
# 2024.8.31
# my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima",}
# set_empty = set()
# print(f"my_set的内容是：{my_set},类型是:{type(my_set)}")
# print(f"set_empty的内容是：{set_empty},类型是:{type(set_empty)}")
#
# my_set.add("Python")
# my_set.add("传智教育")
# print(f"my_set添加元素后的结果是:{my_set}")
#
# my_set.remove("黑马程序员")
# print(f"my_set移除元素后的结果是:{my_set}")
#
# my_set = {"传智教育", "黑马程序员", "itheima"}
#element = my_set.pop()
# print(f"集合被取出来的元素是{element},取出元素后:{my_set}")
# my_set.clear()
# print(f"集合被清空了，结果是：{my_set}")

# set1 = {1, 2, 3}
# set2 = {1, 5, 6}
# set3 = set1.difference(set2)
# print(f"取出差集后的结果是:{set3}")
# print(f"消除差集后，原有集合1的结果:{set1}")
# print(f"消除差集后，原有集合2的结果:{set2}")
# set1.difference_update(set2)
# print(f"消除差集后，集合1的结果:{set1}")
# print(f"消除差集后，集合2的结果:{set2}")

# set3 = set1.union(set2)
# print(f"2集合合并后的结果：{set3}")
# print(f"合并后集合1：{set1}")
# print(f"合并后集合2：{set2}")
# set1 = {1, 2, 3, 4, 5, 5, 6}
# num = len(set1)
# print(f"集合内的元素有:{num}个")
# set1 = {1, 2, 3, 4, 5, 6}
# for element in set1:
#     print(f"集合的元素有:{element}")
#
# my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
#
# set_1 = set()
#
# for element in my_list:
#     set_1.add(element)
# print(f"有列表:{my_list}")
# print(f"存入集合后的结果是：{set_1}")
# 2024.9.1
# my_dict1 = {'常英波':99, '赵佳楠':88, '宋昊哲':77}
# my_dict2 = {}
# my_dict3 = dict()
# print(f"字典1的内容是：{my_dict1},类型是：{type(my_dict1)}")
# print(f"字典2的内容是：{my_dict2},类型是：{type(my_dict2)}")
# print(f"字典3的内容是：{my_dict3},类型是：{type(my_dict3)}")
#
# score_1 = my_dict1['常英波']
# score_2 = my_dict1['赵佳楠']
# print(f"常英波的成绩是：{score_1}")
# print(f"赵佳楠的成绩是：{score_2}")
# stu_score_dict = {
#     '常英波':{
#         '语文':100,
#         '数学':90,
#         '英语':80
#     },
#     '赵佳楠':{
#         '语文':70,
#         '数学':60,
#         '英语':80
#     },
#     '宋昊哲':{
#         '语文':86,
#         '数学':40,
#         '英语': 90
#     }
# }
# print(f"学生的考试信息是：{stu_score_dict}")
# print(f"常英波的语文成绩是：{stu_score_dict['常英波']['语文']}")
# my_dict1 = {'常英波': 99, '赵佳楠': 88, '宋昊哲': 77, '杨耀森': 100}
#
# print(f"字典经过新增元素后，结果：{my_dict1}")
# my_dict1['常英波'] = 90
# print(f"字典经过新增元素后，结果：{my_dict1}")
# score = my_dict1.pop('常英波')
# print(f"字典中被移除了一个元素，结果是：{my_dict1},常英波的分数是：{score}")
# my_dict1.clear()
# print(f"字典被清空了，结果是：{my_dict1}")
#2024.9.4
# keys = my_dict1.keys()
# print(f"字典的全部keys是：{keys}")
# for key in keys:
#     print(f"字典的key是{key}")
#     print(f"字典的value是{my_dict1[key]}")
# for key in my_dict1:
#     print(f"字典的key是{key}")
#     print(f"字典的value是{my_dict1[key]}")
#
# number = len(my_dict1)
# print(f"字典一共有{number}个元素")
#
# my_dict1 = {
#     '王力宏': {
#         '部门': '科技部',
#         '工资': 3000,
#         '级别': 1
#     },
#     '周杰伦': {
#         '部门': '市场部',
#         '工资': 5000,
#         '级别': 2
#     },
#     '林俊杰': {
#         '部门': '市场部',
#         '工资': 7000,
#         '级别': 3
#     },
#     '张学友': {
#         '部门': '科技部',
#         '工资': 4000,
#         '级别': 1
#     },
#     '刘德华': {
#         '部门': '市场部',
#         '工资': 6000,
#         '级别': 2
#     }
# }
# print(f"全体员工当前信息如下:{my_dict1}")
#
# for key in my_dict1:
#     if my_dict1[key]['级别'] == 1:
#         my_dict1[key]['级别'] = 2
#         my_dict1[key]['工资'] += 1000
# print(f"全体级别为1的员工完成升职加薪后:{my_dict1}")
# my_list = [1, 2, 3, 4, 5]
# my_tuple = (1, 2, 3, 4, 5)
# my_str = "abcdefg"
# my_set = {1, 2, 3, 4, 5}
# my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
#
# print(f"列表 元素个数有:{len(my_list)}")
# print(f"元组 元素个数有:{len(my_tuple)}")
# print(f"字符串 元素个数有:{len(my_str)}")
# print(f"集合 元素个数有:{len(my_set)}")
# print(f"字典 元素个数有:{len(my_dict)}")
#
# print(f"列表 元素最大值:{max(my_list)}")
# print(f"元组 元素最大值:{max(my_tuple)}")
# print(f"字符串 元素最大值:{max(my_str)}")
# print(f"集合 元素最大值:{max(my_set)}")
# print(f"字典 元素最大值:{max(my_dict)}")
#
# print(f"列表 元素最小值:{min(my_list)}")
# print(f"元组 元素最小值:{min(my_tuple)}")
# print(f"字符串 元素最小值:{min(my_str)}")
# print(f"集合 元素最小值:{min(my_set)}")
# print(f"字典 元素最小值:{min(my_dict)}")
#
# print(f"列表 转列表的结果:{list(my_list)}")
# print(f"元组 转列表的结果:{list(my_tuple)}")
# print(f"字符串 转列表的结果:{list(my_str)}")
# print(f"集合 转列表的结果:{list(my_set)}")
# print(f"字典 转列表的结果:{list(my_dict)}")
#
# print(f"列表 转元组的结果:{tuple(my_list)}")
# print(f"元组 转元组的结果:{tuple(my_tuple)}")
# print(f"字符串转元组的结果:{tuple(my_str)}")
# print(f"集合 转元组的结果:{tuple(my_set)}")
# print(f"字典 转元组的结果:{tuple(my_dict)}")
#
# print(f"列表 转字符串结果:{str(my_list)}")
# print(f"元组 转字符串结果:{str(my_tuple)}")
# print(f"字符串转字符串结果:{str(my_str)}")
# print(f"集合 转字符串结果:{str(my_set)}")
# print(f"字典 转字符串结果:{str(my_dict)}")
#
# print(f"列表 转集合结果:{set(my_list)}")
# print(f"元组 转集合结果:{set(my_tuple)}")
# print(f"字符串转集合结果:{set(my_str)}")
# print(f"集合 转集合结果:{set(my_set)}")
# print(f"字典 转集合结果:{set(my_dict)}")
#
# print(f"列表 排序结果:{sorted(my_list,reverse=True)}")
# print(f"元组 排序结果:{sorted(my_tuple,reverse=True)}")
# print(f"字符串排序结果:{sorted(my_str,reverse=True)}")
# print(f"集合 排序结果:{sorted(my_set,reverse=True)}")
# print(f"字典 排序结果:{sorted(my_dict,reverse=True)}")
# def test_return():
#     return 1, 2, 3
# x, y, z =test_return()
# print(x)
# print(y)
# print(z)
# def user_info(name, age, gender):
#     print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")
#
# user_info('小明', 20 , '男')
#
# user_info(name='小王', age=11, gender='女')
# user_info(age=10, gender='女', name='潇潇')
# user_info('甜甜', gender='女',age=9)
# def user_info(name, age, gender='男'):
#     print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")
# user_info('小天',13)
# user_info('小天',13,gender='女')
# def user_info(*args):
#     print(f"args参数的类型是：{type(args)},内容是：{args}")
#
# user_info(1, 2, 3, '小明', '男孩')
#
# def user_info(**kwargs):
#     print(f"args参数的类型是：{type(kwargs)},内容是:{kwargs}")
#
# user_info(name = '小王', age = 11, gender = '男')
# def test_func(compute):
#     result = compute(1, 2)
#     print(f"compute参数的类型是:{type(compute)}")
#     print(f"计算结果：{result}")
#
# def compute(x, y):
#     return x + y
# test_func(compute)
# test_func(lambda x,y:x+y)
# f = open("text.txt", "r", encoding="UTF-8")
# # print(type(f))
# #
# # print(f"读取10个字节的结果:{f.read(10)}")
# # print(f"read方法读取全部内容的结果是:{f.read()}")
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是:{line1}")
# print(f"第二行数据是:{line2}")
# print(f"第三行数据是:{line3}")
# f.close()
# count = 0
# with open("text.txt", "r", encoding="UTF-8") as f:
# #     content = f.read()
# #     count = content.count('itheima')
# #     print(count)
#     for line in f:
#         list1 = line.strip()
#         words = line.split()
#         for index in words:
#             if index == 'itheima':
#                 count += 1
# print(count)
# f = open("D:/test.txt", "a", encoding="UTF-8")
# f.write("学Python最佳选择\n")
# f.close()
# fr = open("D:/bill.txt", "r", encoding="UTF-8")
# fw = open("D:/bill.txt.bak", "w", encoding="UTF-8")
# for line in fr:
#     line = line.strip()
#     if line.split(",")[4] == "测试":
#         continue
#
# try:
#     f = open("D:/abc.txt", "r", encoding="UTF-8")
# except:
#     print("程序出现异常了，因为文件不存在，我将open的模式，改为w模式去打开")
#     f = open("abc.txt", "w", encoding="UTF-8")
# try:
#     f = open("123.txt", "r", encoding="UTF-8")
# except Exception as e:
#     print("出现异常了")
#     f = open("123.txt", "w", encoding="UTF-8")
#     print(e)
# else:
#     print("好高兴，没有异常")
# finally:
#     print("我是finally,有没有异常我都要执行")
#     f.close()
#2024.9.11
# def func1():
#     print("func1 开始执行")
#     num  = 1 / 0
#     print("func1 结束执行")
#
# def func2():
#     print("func2 开始执行")
#     func1()
#     print("func2结束执行")
#
# def main():
#     try:
#         func2()
#     except Exception as e:
#         print(f"出现异常了，异常的信息是：{e}")
# main()
# from time import sleep as sl
# print("你好")
# sl(5)
# print("我好")
# from ssd import test2
# test2(1, 2)
#2024.9.12
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LegendOpts,ToolboxOpts,VisualMapOpts
# line = Line()
# line.add_xaxis(["中国", "美国", "英国"])
# line.add_yaxis("GDP", [30, 20, 10])
# line.set_global_opts(
#     title_opts= TitleOpts(title = "GDP展示",pos_left="center",pos_bottom="1%"),
#     legend_opts = LegendOpts(is_show=True),
#     toolbox_opts= ToolboxOpts(is_show=True),
#     visualmap_opts = VisualMapOpts(is_show=True)
# )
# line.render()
# import json
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LegendOpts,ToolboxOpts,VisualMapOpts,LabelOpts
# f_us = open("D:/美国.txt", "r", encoding="UTF-8")
# us_data = f_us.read()
# f_jp = open("D:/日本.txt", "r", encoding="UTF-8")
# jp_data = f_jp.read()
# f_in = open("D:/印度.txt", "r", encoding="UTF-8")
# in_data = f_in.read()
#
# us_data = us_data.replace("jsonp_1629344292311_69436(","")
# us_data = us_data[:-2]
# jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
# jp_data = jp_data[:-2]
# in_data = in_data.replace("jsonp_1629350745930_63180(","")
# in_data = in_data[:-2]
#
# us_dict = json.loads(us_data)
# jp_dict = json.loads(jp_data)
# in_dict = json.loads(in_data)
#
# us_trend_data = us_dict['data'][0]['trend']
# jp_trend_data = jp_dict['data'][0]['trend']
# in_trend_data = in_dict['data'][0]['trend']
#
# us_x_data = us_trend_data['updateDate'][:314]
# us_y_data = us_trend_data['list'][0]['data'][:314]
# jp_x_data = jp_trend_data['updateDate'][:314]
# jp_y_data = jp_trend_data['list'][0]['data'][:314]
# in_x_data = in_trend_data['updateDate'][:314]
# in_y_data = in_trend_data['list'][0]['data'][:314]
#
# line = Line()
# line.add_xaxis(us_x_data)
# line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
# line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
# line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))
#
# line.set_global_opts(
#     title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图",pos_left="center",pos_bottom="1%")
# )
# line.render()
# f_us.close()
# f_jp.close()
# f_in.close()
# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts
#
# map = Map()
#
# data = [
#     ("北京市",99),
#     ("上海市",199),
#     ("湖南省",299),
#     ("台湾省",399),
#     ("广东省",499)
# ]
# map.add("测试地图", data, "china")
# map.set_global_opts(
#     visualmap_opts= VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
#             {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
#             {"min":100,"max":500,"label":"100-500","color":"#990033"}
#         ]
#     )
# )
# map.render()
# import json
# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts, TitleOpts
#
# f = open("D:/疫情.txt", "r", encoding="UTF-8")
# data = f.read()
# f.close()
# data_dict = json.loads(data)
# province_data_list = data_dict["areaTree"][0]["children"]
# data_list = []
# for province_data in province_data_list:
#     province_name = province_data["name"]
#     provice_confirm = province_data["total"]["confirm"]
#     data_list.append((province_name, provice_confirm))
#
# map = Map()
# map.add("中国疫情地图", data_list, "china")
# map.set_global_opts(
#     title_opts=TitleOpts(title="全国疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":1,"max":99,"label":"1-9人","color":"#CCFFFF"},
#             {"min":100,"max":999,"label":"100-999人","color":"#FFFF99"},
#             {"min":1000,"max":4999,"label":"1000-4999人","color":"#FF9966"},
#             {"min":5000,"max":9999,"label":"5000-9999人","color":"#FF6666"},
#             {"min":10000,"max":99999,"label":"10000-99999人","color":"#CC3333"},
#             {"min":100000,"max":999999,"label":"100000-999999人","color":"#990033"},
#         ]
#     )
# )
# map.render("全国疫情地图.html")
#
# import json
# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts, TitleOpts
#
# f = open("D:/疫情.txt", "r", encoding="UTF-8")
# data = f.read()
# f.close()
# data_dict = json.loads(data)
# henan_data = data_dict["areaTree"][0]["children"][3]["children"]
# data_list = []
# for province_data in henan_data:
#     province_name = province_data["name"]
#     province_confirm = province_data["total"]["confirm"]
#     data_list.append((province_name,province_confirm))
# map = Map()
# map.add("河南疫情地图", data_list, "河南")
# map.set_global_opts(
#     title_opts=TitleOpts(title="河南疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":1,"max":99,"label":"1-9人","color":"#CCFFFF"},
#             {"min":100,"max":999,"label":"100-999人","color":"#FFFF99"},
#             {"min":1000,"max":4999,"label":"1000-4999人","color":"#FF9966"},
#             {"min":5000,"max":9999,"label":"5000-9999人","color":"#FF6666"},
#             {"min":10000,"max":99999,"label":"10000-99999人","color":"#CC3333"},
#             {"min":100000,"max":999999,"label":"100000-999999人","color":"#990033"},
#         ]
#     )
# )
# map.render("河南疫情地图.html")
# from pyecharts.charts import Bar,Timeline
# from pyecharts.options import LabelOpts
# from pyecharts.globals import ThemeType
# bar1 = Bar()
# bar1.add_xaxis(["中国", "美国", "英国"])
# bar1.add_yaxis("GDP",[30, 20, 10] ,label_opts=LabelOpts(position="right"))
# bar1.reversal_axis()
# bar1.render("基础柱状图.html")

# bar2 = Bar()
# bar2.add_xaxis(["中国", "美国", "英国"])
# bar2.add_yaxis("GDP",[50, 30, 50] ,label_opts=LabelOpts(position="right"))
# bar2.reversal_axis()
# bar2.render("基础柱状图.html")
#
# bar3 = Bar()
# bar3.add_xaxis(["中国", "美国", "英国"])
# bar3.add_yaxis("GDP",[70, 50, 60] ,label_opts=LabelOpts(position="right"))
# bar3.reversal_axis()
# bar3.render("基础柱状图.html")

# # timeline = Timeline(
# #     {
# #         "theme":ThemeType.LIGHT
# #     }
# # )
# # timeline.add(bar1,"点1")
# # timeline.add(bar2,"点2")
# # timeline.add(bar3,"点3")
# # timeline.add_schema(
# #     play_interval = 1000,
#     is_timeline_show = True,
#     is_auto_play = True,
#     is_loop_play = True
# )
# timeline.render("时间线.html")
# my_list = [["a", 33], ["b", 55], ["c", 11]]
#
# my_list.sort(key=lambda element:element[1], reverse=True)
# print(my_list)
# from pyecharts.charts import Bar, Timeline
# from pyecharts.options import *
# from pyecharts.globals import ThemeType
#
# f = open("D:/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
# data_lines = f.readlines()
# f.close()
# data_lines.pop(0)
# data_dict = {}
# for line in data_lines:
#     year = int(line.split(",")[0])
#     country = line.split(",")[1]
#     gdp = float(line.split(",")[2])
#     try:
#         data_dict[year].append([country, gdp])
#     except KeyError:
#         data_dict[year] = []
#         data_dict[year].append([country, gdp])
#
# timeline = Timeline({"theme": ThemeType.LIGHT})
# sorted_year_list = sorted(data_dict.keys())
#
# for year in sorted_year_list:
#     data_dict[year].sort(key=lambda element: element[1], reverse=True)
#     year_data = data_dict[year][0:8]
#     x_data = []
#     y_data = []
#     for country_gdp in year_data:
#         x_data.append(country_gdp[0])
#         y_data.append(country_gdp[1] / 100000000)
#     bar = Bar()
#     x_data.reverse()
#     y_data.reverse()
#     bar.add_xaxis(x_data)
#     bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
#     bar.reversal_axis()
#     bar.set_global_opts(
#         title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
#     )
#     timeline.add(bar, str(year))
#
# timeline.add_schema(
#     play_interval=1000,
#     is_timeline_show=True,
#     is_auto_play=True,
#     is_loop_play=False
# )
# timeline.render("动态数据图.html")
# class Student:
#     name = None
#     gender = None
#     nationality = None
#     native_place = None
#     age = None
#
# stu_1 = Student()
# stu_1.name = "常英波"
# stu_1.gender = "男"
# stu_1.nationality = "中国"
# stu_1.native_place = "河南省"
# stu_1.age = 22
#
# print(stu_1.name)
# print(stu_1.gender)
# print(stu_1.nationality)
# print(stu_1.native_place)
# print(stu_1.age)
#2024.9.14

# class Student:
#     name = None
#
#     def say_hi_1(self):
#         print(f"大家好！我是{self.name},很高兴认识大家！")
#
#     def say_hi_2(self,msg):
#         print(f"大家好！{self.name},{msg}")
#
# stu1 = Student()
# stu1.name = "常英波"
# stu1.say_hi_1()
# stu1.say_hi_2("欢迎大家来到敦煌！")
#
# stu2 = Student()
# stu2.name = "王墨涵"
# stu2.say_hi_1()
# stu2.say_hi_2("欢迎大家来到瓜洲！")
# class Clock:
#     id = None
#     price = None
#
#     def ring(self):
#         import winsound
#         winsound.Beep(1000,3000)
#
# clock1 = Clock()
# clock1.id = "003032"
# clock1.price = 19.99
# clock1.ring()
# print(f"闹钟id:{clock1.id},闹钟价格:{clock1.price}")
#
# clock2 = Clock()
# clock2.id = "003033"
# clock2.price = 29.99
# clock2.ring()
# print(f"闹钟id:{clock1.id},闹钟价格:{clock1.price}")
# class Student:
#
#     def __init__(self,name, age, tel):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         print("学生类创建了一个类对象")
# stu1 = Student("杨耀森", 22,"15137772146")
# print(stu1.name)
# print(stu1.age)
# print(stu1.tel)
# class Student:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#
# list_student = []
# for index in range(0, 10):
#     print(f"当前录入第{index+1}位学生信息,总共需要录入10位学生信息")
#     name = input("请输入学生姓名:")
#     age = input("请输入学生年龄:")
#     address = input("请输入学生地址:")
#     student = Student(name, age, address)
#     list_student.append(student)
#     print(f"学生{index+1}信息录入完成，信息为【学生姓名：{list_student[index].name},"
#           f"年龄：{list_student[index].age},地址：{list_student[index].address}】")
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Student类对象，name:{self.name}, age:{self.age}"
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __le__(self, other):
#         return self.age <= other.age
#
#     def __eq__(self, other):
#         return self.age == other.age
# stu1 = Student("周杰伦", 31)
# stu2 = Student("林俊杰", 31)
# print(stu1 == stu2)
# class Phone:
#     __current_voltage = 0.5
#
#     def __keep_single_core(self):
#         print("让CPU以单核模式运行")
#
#     def call_by_5G(self):
#         if self.__current_voltage > 1:
#             print("5G通话已开启")
#         else:
#             self.__keep_single_core()
#             print("电量不足，无法使用5G通话，并已设置为单核模式进行省电。")
#
#
# iPhone = Phone()
# iPhone.call_by_5G()
print("Hello World!")