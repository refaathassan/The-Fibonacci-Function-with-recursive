user_num=int(input("enter the number please:   "))
fib_ls=[]
def fibonacci_re(num):
    if num==1 or num==2:
        return 1
    return fibonacci_re(num-1)+fibonacci_re(num-2)
print(fibonacci_re(user_num))