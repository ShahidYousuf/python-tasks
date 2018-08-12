# Basic things using functions:

# Fibonacci sequence upto n

def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a + b
    print()

if __name__ == '__main__':
    fibo(50)

