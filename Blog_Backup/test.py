import redis
# 1026
def add(a, b):
    sum = a+b
    return sum

def mu(a ,b):
    result = a*b
    return result

def debug():
    sum = add(1,2)
    result = mu(3,4)
    return sum,result

debug()