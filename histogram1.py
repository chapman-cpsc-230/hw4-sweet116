ls = [4, 9, 13, 5]

def bar(n):

    st = ''

    for i in range(n):

        st += '*'
    return st


for i in range(len(ls)):

    print bar(ls[i])

print ls
