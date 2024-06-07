# Global scope
my_global = 10


def fn1():
    local_v = 5  # Enclosed scope

    def fn2():
        double = 2  # local scope
        print(local_v)
        print(double)

        fn2()


fn1()

print(my_global)  # Integrado scope
