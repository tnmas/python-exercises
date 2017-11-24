def check_fermat(a, b, c, n):
    if(n>2):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work!")

def fun():
    print("enter the four numbers: ")
    x=int(input())
    y=int(input())
    z=int(input())
    m=int(input())
    check_fermat(x, y, z, m)

fun()
    
