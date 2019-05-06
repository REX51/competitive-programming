import sys

if __name__=='__main__':
    c = input().upper()
    lst = ['A','C','G','T','U']
    change = {'A':'U','T':'A','C':'G','G':'C'}
    if c not in lst:
        print('Invalid input')
        sys.exit()
    else:
        print(change[c])

        