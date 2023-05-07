n=int(input('escriba numero'))
def fib(n):
    if int(n) < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
for i in range(99999999999999):
    print(fib(i))

    
















    