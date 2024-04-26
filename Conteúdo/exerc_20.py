import time 

def power(a, n):
    res = 1
    for i in range(n):
        res *= a
    return res

def rpower(a,n):
    'retorna a à potência n '
    counter = 0      # conta número de multiplicações
    if n==0:
        return 1
    # if n > 0:
    tmp = rpower(a, n//2)
    if n % 2 == 0:
        counter += 1
        return tmp*tmp      # 1 multiplicação
    else: # n % 2 == 1
        counter += 2
        return a*tmp*tmp    # 2 multiplicações
    
def timing(func, n):
    funcIn = int(n)
    start = time.time()
    func(funcIn)
    end = time.time()
    return end - start
def timingAnalysis(func, start, stop, inc,runs):
    for n in range(start, stop, inc):
        acc = 0.0
        for i in range(runs + 1):
            acc += timing(func, n)
        print(f"Tempo de execução de {func.__name__}({n}) é {(acc/runs):.7f}")

def power2(n):
    return power(2,n)

def rpower2(n):
    return rpower(2,n)

def pow2(n):
    return 2**n

timingAnalysis(power2, 20000, 80000, 2000, 10)
timingAnalysis(rpower2, 20000, 80000, 2000, 10)
timingAnalysis(pow2, 20000, 80000, 2000, 10) # Definitivamente o mais rápido entre os outros
