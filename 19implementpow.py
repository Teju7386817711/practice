print("Hello world")
class py_pow:
    def por(self,x,n):
        if x==0 or x==1 or n==1:
            return x
            
        if x==-1:
            if n%2==0:
                return 1
            else:
                return -1
            if n==0:
                return 1
            if n<0:
                return 1/self.powr(x,-n)
            val =self.powr(x,n/2)
            if n%2==0:
                return val*val
            return val*val*x
x=int(input("enter x value:"))
n=int(input("enter n value:"))
print("pow(x,n) value is:",py_pow().powr(x,n));