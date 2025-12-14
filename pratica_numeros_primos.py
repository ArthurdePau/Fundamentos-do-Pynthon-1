def ePrimo(n):
    if n <= 1:
        return 'não é primo, somente 1 divisor.'
    import math
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 'não é primo.'
    return 'é primo'


#     for i in range(2, n //2):
#         if n % i == 0:
#             return 'não é primo.'
#     return 'é primo'

num = int(input('Descubra se um número é primo! \nNúmero: '))
resp = ePrimo(num)
print( num , resp )