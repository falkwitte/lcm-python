# lcm algorithm written in python3 

def gcd(a, b):
    while(b != 0):
        h  = a % b
        a = b
        b = h
    return a

def lcm(a, b):
    if a==0 or b==0:
        return 0
    return (a*b) / gcd(a, b)


