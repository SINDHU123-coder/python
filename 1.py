#write a function to calculate 2nd power of a number
#using** (exponent operator)
def power_2(a:int):
    return a**2
print(power_2(6))

#write function to calculate a**n
def exponentiate(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result
base = 2
power = 4
result = exponentiate(base, power)
print(result)