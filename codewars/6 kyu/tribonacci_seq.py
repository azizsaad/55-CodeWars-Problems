def tribonacci(signature, n):

    if n <= 3:
        return signature[:n]

    for i in range(n-3):
        signature.append(sum(signature[-1:-4:-1]))
        if len(signature) == n:
            return signature

print (tribonacci([1,1,1], 2))


'''
def tribonacci(signature, n):
    if n == 0:
        return []
    if n == 1:
        return [signature[0]]
    if n == 2:
        return signature[:2]
    if n == 3:
        return signature
    for i in range(n-3):
        signature.append(sum(signature[-1:-4:-1]))
        if len(signature) == n:
            return signature
'''
