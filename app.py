def gcd(a, b):
    # 用欧几里得算法求最大公约数
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # 利用最大公约数计算最小公倍数
    return a * b // gcd(a, b)


num1 = 12
num2 = 18
print(f"两个数 {num1} 和 {num2} 的最小公倍数是: {lcm(num1, num2)}")
