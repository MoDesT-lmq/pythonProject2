import random

weishu = 1
suijishu = []
shuliang = input("请输入数量：")
while not shuliang.isdigit():
    shuliang = input("输入错误，请重新输入数量（只能是数字）：")
shuliang = int(shuliang)
weishu = input("请输入位数：")
while not weishu.isdigit():
    weishu = input("输入错误，请重新输入位数（只能是数字）：")
weishu = int(weishu) #这是多少位
for i in range(shuliang):
    for j in range(weishu):
        suijishu.append(random.choice(range(10)))
        while suijishu[j] == suijishu[j - 1] and j > 0:
            suijishu[j] = random.choice(range(10))
        print(suijishu[weishu * i + j], end="")
    print("")
