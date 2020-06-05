def bhnum(start,end):
    '''参数n表示数字的位数，例如n=3时返回495，n=4时返回6174'''
    #待测试数范围的起点和结束值

    #依次测试每个数
    for i in range(start, end):
        #由这几个数字组成的最大数和最小数
        big = ''.join(sorted(str(i),reverse=True))
        little = ''.join(reversed(big))
        big, little = map(int,(big, little))
        if big-little == i:
            print(i)
n=int(input("please input:"))
start= 10**(n-1)
end = 10**n
bhnum(start,end)
