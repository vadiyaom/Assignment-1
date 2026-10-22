# Given the following code, identify which variables are local and which are global, and explain what will be printed when you call outer() and then print(x) at the end:python
# x = 'global'
# def outer():
# x = 'outer'
# def inner():
# nonlocal x
# x = 'inner'
# inner()
# print('Inside outer:', x)
# outer()
# print('Outside:', x)
# Focus on the scope of x inside and outside the functions.

x = 'global'

def outer():
    x = 'outer'

    def inner():
        nonlocal x
        x = 'inner'

    inner()
    print('Inside outer:', x)

outer()
print('Outside:', x)