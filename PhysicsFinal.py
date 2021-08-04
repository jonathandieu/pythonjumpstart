import math


def final_3b(B, W, N, R, T):
    A = math.pi * R**2
    answer = abs((N * B * A * W) * math.sin(W*T))
    print("question 3b:", answer)


def question_seven(i1, i2, d):
    answer = (.5*i1)/(i1+i2)

    print("question seven:", answer)
def question_eight(i1, d1, d2):

    answer = (1/2) * (i1 / d1) * d2
    print("question eight:", answer)

def question_nine(k,B,a,t):
     # feesiks q here - quiz 4 q 2
     da=(-2*math.pi*(k**2))/(t**3)
     emf=B*da*math.cos(math.radians(a))
     return -emf

def question_ten(k, r, d):
    mu_0 = 1.26e-6
    r = r * 10**(-3)
    d = d * 10**(-9)
    answer = k*((mu_0*r**2)/2*d)
    print("question ten:", answer)



print("question 1: Divergence of the magnetic field is zero")
print("question 2: When calculating the direction of the mf on a moving charge or when calculating the direction of the magnetic field generated from a line of current")
print("question 3: Magnetic flux is the measure of how many magnetic field lines are passing through a given area enclosed by a loop")
print("question 4: The current produced travels in a direction such that it produces a secondary magnetic field/flux which opposes the original change in the magnetic flux")
print("question 5: The current is maximal at the frequency where the capacitive reactance is equal to the inductive reactance")

final_3b(.23, 12.7, 64, .83, 13.3)
