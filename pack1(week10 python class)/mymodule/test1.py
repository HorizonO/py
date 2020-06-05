from random import randint
_value=10
def guess(maxValue=100, maxTimes=5):
    #�������һ������
    value = randint(1,maxValue)
    for i in range(maxTimes):
        prompt = 'Start to GUESS:' if i==0 else 'Guess again:'
        #ʹ���쳣����ṹ����ֹ���벻�����ֵ����
        try:
            x = int(input(prompt))
        except:
            print('Must input an integer between 1 and ', maxValue)
        else:
            #�¶���
            if x == value:
                print('Congratulations!')
                break
            elif x > value:
                print('Too big')
            else:
                print('Too little')
    else:
        #�������껹û�¶ԣ���Ϸ��������ʾ��ȷ��
        print('Game over. FAIL.')
        print('The value is ', value)
