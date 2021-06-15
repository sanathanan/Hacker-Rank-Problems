
def diwali_lights(n):
    return (2**n-1)%10**5

n = int(input())
for _ in range(n):
    num=int(input())
    print(diwali_lights(num))
