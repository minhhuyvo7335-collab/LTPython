#câu1 
def tong_chu_so(n):
    if n < 10:
        return n
    return n % 10 + tong_chu_so(n // 10)

# test
print(tong_chu_so(345)) 

#câu2
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

# test
print(giai_thua(5))  

#câu3 
def luy_thua(a, b):
    if b == 0:
        return 1
    return a * luy_thua(a, b - 1)

# test
print(luy_thua(2, 3))  

#câu4 
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# test
print(gcd(12, 18)) 

#câu5 
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(50)) 