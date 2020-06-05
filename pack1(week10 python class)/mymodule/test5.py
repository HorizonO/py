def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def main():
    for i in range(1,100):
        if prime(i) and prime(i+2):
            print(i,i+2)

