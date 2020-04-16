#
import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
#
# user_data_dir = ("/Users/suyayan/Library/Application Support/Google/Chrome")
# # 加载配置数据
# option = webdriver.ChromeOptions()
# option.add_argument(user_data_dir)
# # 启动浏览器配置
# driver = webdriver.Chrome(chrome_options=option,
#                           executable_path="/Applications/Google Chrome.app")
# # driver.get("https://aminoapps.com")

# s="  hello i am     yayan     "
# l=s.split(' ')
#
# l2=[i for i in l if i]
# l_res=l2[::-1]
#
# s2=' '.join(l_res)
#
# print(l_res)
# print(s2)\
# dict={'name':'1a','':'2b'}
# a=[1,2,3,4,'a']

# print(dict['name'])

# 1.两数相加nums = [3,3]
# target = 6
# def twosum(nums,target):
#     for i in nums:
#         sub=target-i
#         num2=nums[nums.index(i)+1:]
#         if sub in num2:
#             return [nums.index(i),num2.index(sub)-]
# print(twosum(nums,target))

# def twosum(nums,target):
#     d={}
#     for i in range(len(nums)):
#         num=nums[i]
#         if num in d.keys():
#             return [d[num],i]
#         d[target-num]=i
#         print(d)
#
# print(twosum(nums,target))

# 7.整数反转
# num=-10023000
#
# def intreverse(num):
#     s = str(num)
#     s2=''
#     if s[0]=='-':
#         syb=-1
#         s=s[:0:-1]
#     else:
#         syb=1
#         s=s[::-1]
#     for i in s:
#         s2=s2+i
#         strips2=s2.strip('0')
#         print(strips2)
#
#     return syb*int(strips2)
#
# print(intreverse(num))

# 从数组中找出重复次数最多的字母
# a=['a','b','c','c','a','b','b','d','d','d','d']
# dic={}
# for i in a :
#     j=dic.get(i,None)
#     if j is None:
#         dic[i]=1
#     else:
#         dic[i]=dic[i]+1
#
# b=sorted(dic.items(),key=lambda x:x[1],reverse=True)
#
# print(b[0][0],b[0][1])
#
#
# 生成器函数
# def yyg():
#     b=0
#     while True:
#         b=b+1
#         yield b
# 创建生成器yg,这个生成器使用next方法，可以执行yyg函数，遇到yield就暂停并返回当前yield，yg再使用next方法会从上次暂停的地方继续执行yyg函数
# yg=yyg()
# print(next(yg))
# print(next(yg))
# print(next(yg))
# print(next(yg))
# print(next(yg))
# print(next(yg))
# print(next(yg))


# 闭包和装饰器
# w1就是一个闭包，接收一个函数名，内部函数inner来添加需要给每个函数前后添加的代码

# def w1(func):
#     def inner():
#         #添加的代码
#         func()
#         # 添加的代码
#
#     return inner
#
# @w1 的作用： f1=w1(f1)
# @w1
# def f1():
#     print('f1')
#
# def f2():
#     print('f2')
#
# def f3():
#     print('f3')
#
# def f4():
#     print('f4')

# driver.get('http://localhost:5000')
#
# # logo1=driver.find_element_by_xpath("//*[@id='banner_logo']")
# # ActionChains(driver).move_to_element(logo1).perform()
# # time.sleep(1)
#
# logo2=driver.find_element_by_xpath("//*[contains(text(),'logotext')]")
# ActionChains(driver).move_to_element(logo2).perform()
# time.sleep(1)
#
# driver.quit()


#
# for i in range(1,11):
#     print(i)

# s='   yayan   am i    '
# l=s.split(' ')
# l2=[]
#
# for i in l:
#     if bool(i)==True:
#         l2.append(i)
#
# print(l2)
# l2=l2[::-1]
# print(l2)
# s2=l2.join(' ')
#

s = ' hello woddrld    '
def fun(s):
    l1 = s.split(' ')
    l2 = []
    for i in l1:
        if bool(i) == True:
            l2.append(i)
    lw= l2[len(l2) - 1]
    return len(lw)

print(fun(s))