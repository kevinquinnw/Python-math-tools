# An abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself. The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4, and 6 for a total of 16. 


def abundant(n): 
    factor_sum = sum([factor for factor in range(1, n) if n % factor == 0])
    return factor_sum > n 
print(abundant(12))
print(abundant(453))