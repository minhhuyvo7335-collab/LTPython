#bài vii
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
lst = [int(x) for x in input("Nhập các số:").split()]
# Câu A 
primes = [x for x in lst if is_prime(x)]
print("Số nguyên tố:", primes)
# Câu B 
soam = [x for x in lst if x < 0]
trungbinhcongsoam=sum(soam)/len(soam) if soam else 0 
soduong = [x for x in lst if x > 0]
trungbinhcongsoduong=sum(soduong)/len(soduong) if soduong else 0
print("Trung Bình Cộng Số Âm:", trungbinhcongsoam)
print("Trung Bình Cộng Số Dương:", trungbinhcongsoduong)
# Câu C
print("MAX:", max(lst))
print("MIN:", min(lst))
# Câu D cách 1 
print("List tăng dần:", all(lst[i] <= lst[i+1] for i in range(len(lst)-1)))
# Câu D cách 2(dùng lambda + comprehension)
print("List tăng dần:", (lambda l: all(l[i] <= l[i+1] for i in range(len(l)-1)))(lst))
