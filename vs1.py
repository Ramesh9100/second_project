'''L=[-1,1,2,3,1]
c=0
for i in range(len(L)):
      for j in range(i+1,len(L)):     
        if L[i]+L[j]<2:
            c+=1
print(c)

L=[1,2,3,1,1,3]
c=0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]==L[j]:
           c+=1
print(c)

s=input('enter a string:')
sum=0
for i in s:
    if i.isdigit():
       sum+=(int(i)**2)
print(sum)

N=int(input())
l=[]
l.insert(0,N)
l.insert(1,3)
l.append(2)
print(l)

class Cubes():
    def __init__(self,sv,ev,up=1):
        self.sv=sv
        self.ev=ev
        self.updation=up

    def __iter__(self):
        self.i=self.sv
        return self
    def __next__(self):
        if self.i<self.ev:
            dummy=self.i**3
            self.i+=self.updation
            return dummy
        raise StopIteration
S=Cubes(1,10)
for i in S:
    print(i)

class Fibo:
    def __init__(self,Fn,Ln,N):
        self.Fn=Fn
        self.Ln=Ln
        self.number=N
    def __iter__(self):
        self.count=1
        return self
    def __next__(self):
        if self.count<self.number:
            dummy=self.Fn
            self.Fn=self.Ln
            self.Ln=self.Fn+dummy
            self.count+=1
            return dummy
        raise StopIteration
a=Fibo(1,2,10)
for i in a:
    print(i)

def is_prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def primegenerator(limit):
    n=1
    count=0
    while count<limit:
        if is_prime(n):
            yield n
            count+=1
        n+=1
pg=primegenerator(10)
for i in pg:
    print(i)'''

a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
d=int(input('d:'))
if a>b:
    if a>c:
        if a>d:
           print('a is max')
        else:
           print('d is max')
    else:
        if c>d:
            print('c is max')
        else:
            print('d is max')
else:
    if b>c:
        if b>d:
            print('b is max')
        else:
            print('d is max')
    else:
        if c>d:
            print('c is max')
        else:
            print('d is max')