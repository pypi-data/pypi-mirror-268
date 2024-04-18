
# 欧几里得算法
def gcd(a:int,b:int)->int:
    if a==0:
        return b
    elif b==0:
        return a
    while not b==0:
        a,b=b,a%b
    return a
# 扩展欧几里得算法
def exGcd(a:int, b:int)->tuple[int,int,int]:
    if b == 0:
        return 1, 0
    x1, x2 = 1, 0

    y1, y2 = 0, 1

    while True:
        if b == 0:
            break
        q = a // b
        tmp1, tmp2, tmp3 = y1, y2, b
        y1, y2, b = (x1 - q * y1), (x2 - q * y2), (a - q * b)
        x1, x2, a = tmp1, tmp2, tmp3
    return (a, x1, x2)


# 求逆元
def modInverse(a, m) -> int:
    g, x, _ = exGcd(a, m)
    if not g==1:
        return "Input values are not prime to each other"
    return x % m


# 模意义下快速取幂
def modQuickPow(a:int, b:int, m:int)->int:
    a = a % m
    n = 1
    while b > 0:
        if b & 1:#二进制展开
            n = (n * a) % m
        a = (a * a) % m
        b >>= 1#b右移一位
    return n
