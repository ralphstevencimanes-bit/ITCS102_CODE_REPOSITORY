def taga_triangle(number):
    for a in range(number, 0, -1):
        for b in range(1, a+1):
            print("*", end=" ")
        print()

def sum(a, b):
    return a+b

def box(size):
    for a in range(size+1):
        for b in range(size+1):
            if b == 0 or a == 0 or a == size or b == size :
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def my_factorial(number):
    fact = 1
    for a in range(number, 0, -1):
        fact *= a
    return fact

print(my_factorial(4))

box(5)
box(20)
taga_triangle(9)

taga_triangle(7)
taga_triangle(12)
taga_triangle(5)
taga_triangle(6)

print(sum(10,25))
print(sum(23,3) * 50)