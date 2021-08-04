import math


def final_3b(B, W, N, R, T):
    A = math.pi * R**2
    answer = abs((N * B * A * W) * math.sin(W*T))
    print("question 3b:", answer)

def final_6c(q1, q2, d):
    answer = d / (1 + math.sqrt(q2/q1))
    print("question 6c:", answer)

def final_7c(q, m, z, r):
    answer = ((m * 9.8 * 2 * 8.85e-12 * (r**2 + z**2)**(3/2)) / (r * z * q)) * 10000000

    print("question 7c:", answer)

def final_10c():
    mu_0 = 1.26e-6

    answer = (1/2) * (mu_0 / (4 * math.pi))

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



print("question 1: Vector pointing in the direction of the decrease in potential")
print("question 2: Kirchoffs law comes from conservation of energy and conservation of charge")
print("question 3:The divergence of the electric field is non-zero")
print("question 4: The current produced travels in a direction such that it produces a secondary magnetic field/flux which opposes the original change in the magnetic flux")
print("question 5: The current is maximal at the frequency where the capacitive reactance is equal to the inductive reactance")
# print("question 6: The voltage across the capacitor is equal to the current times the capacitive reactance")
final_6c(13.6, 5.2, 1.33)
final_7c(1.9, 12.2, 45.2, 13.7)
