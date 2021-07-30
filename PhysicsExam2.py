import math

def question_seven(i1, i2, d):
    answer = (2*i1 * d) / (i1 + i2)
    print(answer)
def question_eight(i1, i2, d1, d2):
    answer = 2
    print(answer)

def question_nine(k,B,a,t):
     # feesiks q here - quiz 4 q 2
     da=(-2*math.pi*(k**2))/(t**3)
     emf=B*da*math.cos(math.radians(a))
     return -emf


question_seven(12.9, 16, 1.4)
print(question_nine(.17, .2, 46.4, .91))