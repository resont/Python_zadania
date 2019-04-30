class fib:
    def __init__(self,n):
        self.n = n
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        temp = self.b

        if temp >= self.n:
            raise StopIteration
        
        self.b += self.a
        self.a = temp
        return temp

print("\nIterator ciągu Fibonacciego")
print(list(fib(30)))

def gen_fib(n = None):
    a,b = 0,1
    i = n is None
    
    while i or b < n:
        yield b
        temp = b
        b,a = a+b,temp

print("\nGenerator")
print(list(gen_fib(30)))

class it_fib:
    def __init__(self,start,finish):
        self.start = start
        self.finish = finish
    def __iter__(self):
        a = 0
        gen_it = iter(gen_fib())

        while a < self.start:
            next(gen_it)
            a += 1
        while a < self.finish:
            yield next(gen_it)
            a += 1
        return    
f = open("dane2.txt","w+")
x = 0
for i in it_fib(200,220):
    f.write(f"{i}\n")
    if x == 0:
        print(f"F(200) ma {len(str(i))} liczb")
        x = 1

f.close()