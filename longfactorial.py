


if __name__=='__main__':
    n = int(input())
    fact = lambda x: 1 if x == 0 else x * fact(x-1)
    print(fact(n))