def prime(n):
    if n<2:
        return False
    a=0
    for i in range(1,n+1):
        if n%i==0:
            a+=1
    if a>2:
        return False
    else:
        return True
def main():
    n=input("Enter a number:")
    print(prime(n))
main()

