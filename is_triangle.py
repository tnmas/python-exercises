def is_triangle(x, y, z):
    if(x>y+z or y>x+z or z>x+y):
        print("No")
    else:
        print("Yes")
def triangle():
    a=int(input())
    b=int(input())
    c=int(input())
    is_triangle(a, b, c)

triangle()
