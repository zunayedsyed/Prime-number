# prime number
def prime_number(n):
   for i in range(2,n):
        if n%i==0:
             print("Prime number")
             break
        else:
            print("Not prime number")
# integer
n=int(input())
# function call
prime_number(n)