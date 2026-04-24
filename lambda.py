#câua
f = lambda n: abs(n)
print(f(-5))  

#câub 
f = lambda n: n + 15
print(f(10))  

#câuc 
f = lambda x, y: x * y
print(f(3, 4))  

#câud 
f = lambda n: n % 13 == 0 or n % 19 == 0
print(f(26))  

#câue 
import math
f = lambda r: math.pi * r**2 if r >= 0 else "Invalid" 
print(f(2))  # ~12.57
print(f(-1))  # Invalid

#câuf 
f = lambda d, r: 2 * (d + r)
print(f(3, 4))  

#câug 
f = lambda n: int(math.sqrt(n))**2 == n
print(f(16))  

#câuh 
import math
f = lambda n: n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))
print(f(7))  
print(f(8))  

#câui
f = lambda a,b,c: (
    "Không phải tam giác" if a <= 0 or b <= 0 or c <= 0 or a+b<=c or a+c<=b or b+c<=a else
    "Đều" if a==b==c else
    "Cân" if a==b or b==c or a==c else
    "Vuông" if sorted([a,b,c])[0]**2 + sorted([a,b,c])[1]**2 == sorted([a,b,c])[2]**2 else
    "Thường"
)
print(f(3,4,5))  
print(f(2,2,2))  
print(f(1,2,3))  