def square(s):
    return s*s
def rect(l,b):
    return l*b
def circle(r):
    return 3.14*r*r
def tri(b,h):
    return ((b*h)/2)
a=float(input("enter side: "))
b=float(input("enter breadth: "))
l=float(input("enter length: "))
r=float(input("enter radius: "))
h=float(input("enter height: "))
print("area of square = %.2f" % square(a))
print("area of rectangle = %.2f" % rect(l,b))
print("area of circle = %.2f" %circle(r))
print("area of triangle = %.2f" %tri(b,h))



