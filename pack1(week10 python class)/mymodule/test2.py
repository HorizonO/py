def hannoi(num, src, dst, temp=None):
    #����������¼�ƶ������ı���Ϊȫ�ֱ���
    global times
    #ȷ�ϲ������ͺͷ�Χ
    assert type(num) == int, 'num must be integer'
    assert num > 0, 'num must > 0'
    #ֻʣ����ֻ��һ��������Ҫ�ƶ�����Ҳ�Ǻ����ݹ���õĽ�������
    if num == 1:
        print('The {0} Times move:{1}==>{2}'.format(times, src, dst))
        times += 1
    else:
        #�ݹ���ú�������
        #�Ȱѳ����һ������֮������������ƶ�����ʱ������
        hannoi(num-1, src, temp, dst)
        #�����һ������ֱ���ƶ���Ŀ��������
        hannoi(1, src, dst)
        #�ѳ����һ������֮����������Ӵ���ʱ�������ƶ���Ŀ��������
        hannoi(num-1, temp, dst, src)
#������¼�ƶ������ı���
times = 1
#A��ʾ����������ӵ����ӣ�C��Ŀ�����ӣ�B����ʱ����

