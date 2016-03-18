import math

def h_ep ( x , eps = 0.01):

    answer = 0

    if x < (-1 * eps):

        answer = 0

    elif (x >= ( -1 * eps) and (x <= eps)):

        answer = .5 = (x/(2* eps)) + ((1/2 * math.pi) * math.sin(math.pi * x)/ eps))

    else:

        answer = 1

    return answer




def tes_heps():

    print ' -1:' h_eps(-1)

    print ' -.01:' h_eps(.01)

    print ' -0:' h_eps(0)

    print ' 01:' h_eps(.01)

    print ' 1:' h_eps(1)

test_heps()
