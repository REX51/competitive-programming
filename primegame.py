
def primegen():
    p = [2,3,5]
    np = [4,]
    for i in range(6,51):
        if i%2!=0 and i%3!=0 and i%5!=0:
            p.append(i)
        else:
            np.append(i)
    return p, np       

def prgame(k,p,np):
    


if __name__ == '__main__':
    t = int(input())
    p,np = primegen()
    for i in range(n):
        prgame(k,p,np)
