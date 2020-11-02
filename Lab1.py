"""
print(3 + 2 * 2)
name = 'Lizz'
print(name[0:2])
var = '01234567'
print(var[::2])
print('1'+'2')
myvar = 'hello'
print(myvar.upper())
Numbers="0123456"
print(Numbers[::2] )
print("0123456".find('1'))

A=(0,1,2,3)
print(A[-1])
print(A[3])
B=["a","b","c"] 
print(B[1:])
S={'A','B','C'}
U={'A','Z','C'}
print(U.union(S))
print(U.intersection(S))

D={'a':0,'b':1,'c':2}
print(D.values())
print(D['b'])

A=('a','b','c')
print(A[0])

L=['1','2','3']
L.append(['a','b'])
print(L)

thisset = {"apple", "banana", "cherry"}
thisset.add("apple")
print(thisset)
thisset.add("apple")
print(thisset) 
Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
print( Dict["D"])

x='a'
if(x!='a'):
    print("this is not a")
else:
    print("this is a")

i=100000000
if(i!=0):
    print("this is not a")
else:
    print("this is a")

A=[3,4,5]
for a in A:
    print(a)

x=3
y=1
while(y!= x):
    print(y)
    y=y+1
a=1
def add(b):
    return a+b
c=add(10)
print(c)
"""
Class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1

car_info("Honda","Accord","blue")






