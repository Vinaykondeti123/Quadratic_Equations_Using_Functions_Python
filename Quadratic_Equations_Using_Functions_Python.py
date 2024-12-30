# solving quadratic equations using functions
def cal(a,b,c):
   d=b*b-4*a*c
   r1=(-b+(d**(0.5)))/2*a
   r2=(-b-(d**(0.5)))/2*a
   print(f"Roots: {r1,r2}")

x=int(input("Enter a value: "))
y=int(input("Enter b value: "))
z=int(input("Enter c value: "))
cal(x,y,z)
