def bhnum(start,end):
    '''����n��ʾ���ֵ�λ��������n=3ʱ����495��n=4ʱ����6174'''
    #����������Χ�����ͽ���ֵ

    #���β���ÿ����
    for i in range(start, end):
        #���⼸��������ɵ����������С��
        big = ''.join(sorted(str(i),reverse=True))
        little = ''.join(reversed(big))
        big, little = map(int,(big, little))
        if big-little == i:
            print(i)
n=int(input("please input:"))
start= 10**(n-1)
end = 10**n
bhnum(start,end)
