#计算1到1000之间所有指数的和
sum = 0 #定义变量存储结果
for i in range(2,1001): #i的值从2到1000
    temp=0 #定义变量，临时存储值；
    for j in range(2,1001):
        if (i % j == 0) and (j < i) :
            temp = 0 #如果除余为0，则将临时变量从新赋值为0
            break #跳出for循环
        else:
            temp = i
    sum = sum + temp #求和
#以下是print语句的基本使用方法
print("1到100之间所有质数的和为：",format(sum))
print('和为：'+str(sum))
print("1到100之间所有质数的和为：{0}".format(sum))
result = 3.1415926
print('{},小数 类型,{}'.format(result,type(result)))