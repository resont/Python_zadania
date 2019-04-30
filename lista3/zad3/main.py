class fib:
    def __init__(self, index):
        self.index = index
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.b

        if temp >= self.index:
            raise StopIteration
        
        self.b = self.a + self.b
        self.a = temp

        return temp
        
print("\nIterator ciągu Fibonacciego")
liczba = fib(15)
print(list(liczba))

def fib_gen(n=None):
    a, b = 0, 1
    inf = n is None
    while inf or b <= n:
        yield b
        a, b = b, a + b

print("\nGenerator ciągu Fibonacciego")
print(list(fib_gen(15)))

class fib_inf:
    def __init__(self,start,finish):
        self.start = start
        self.finish = finish
    def __iter__(self):
        a = 0
        gen_it = iter(fib_gen())

        while a < self.start:
            next(gen_it)
            a+=1
        while a < self.finish:
            yield next(gen_it)
            a+=1
        
        return
f = open("dane.txt","w+")
x = 0
for i in fib_inf(100000, 100020):
    f.write(f"{i}\n")
    if x == 0:
        print(f"F(100000) ma:{len(str(i))} liczb")
        x = 1
f.close()
