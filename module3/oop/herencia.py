# Herencia simple
class A1:
    pass
class B1(A1):
    pass

# Herencia multiple
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

# Herencia de varios niveles
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)