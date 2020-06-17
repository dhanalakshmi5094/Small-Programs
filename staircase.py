def fib(k):
    k1 = 0
    k2 = 1
    k3 = 1
    sum = 0
    if k <= 1:
        return k
    else:
        for i in range(2, k + 1):
            sum = k1 + k2 +k3
            k1 = k2
            k2 = k3
            k3 = sum
    return k3


def solution(n):
    # Type your solution here
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2) + fib(n - 3)


print(solution(3))
