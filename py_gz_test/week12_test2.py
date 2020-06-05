class DTError(Exception):  #没有这个类定义 下面的DTError就会报错
    pass

def devide(x,y):
    try:
        ans=x/y
        if (not isinstance(x,int) or not isinstance(y,int)):  #如果两个数类型不同，抛出异常
            raise DTError
    except ZeroDivisionError:   #抛出除数为0的异常
        return 'division by zero!'
    except DTError:   #类型不同的异常
        print ('The two nums may be one or two is not int')  #先提示类型不同
        try:
            #将x,y强制转换成int，需要捕捉异常
            x=int(x)
            y=int(y)
            if(type(x)!=int or type(y)!=int):
                raise Exception
        except:
            pass
        else:
            devide(x,y)
            return ans
    except:
        return '不是数值数据，两个无法进行相除操作'  #
    else:
        return ans
x=input("请输入一个数：")
y=input("请输入一个数：")
print(devide(x,y))