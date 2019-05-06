
def timeconv(s):
    m = s.rstrip('PMAM').split(':')
    p = [list(i) for i in s]
    n = len(p)
    val = p[n-2][0]
    if val == 'P':
        if m[0] == '12':
            print(str(m[0])+':'+str(m[1])+':'+str(m[2]))
        else:
            m[0]=int(m[0])+12
            print(str(m[0])+':'+str(m[1])+':'+str(m[2]))
    elif val == 'A':
        if m[0] == '12':
            print('00'+':'+str(m[1])+':'+str(m[2]))
        else:
            print(str(m[0])+':'+str(m[1])+':'+str(m[2]))
    


if __name__ == '__main__':
    s = input()
    timeconv(s)