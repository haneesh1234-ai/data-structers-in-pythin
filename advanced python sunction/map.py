def myfunc(a, b):
    return a + ':' + b

x = map(myfunc, ('dog','cat','cherry'),('barks','meow','blossom'))

print(x)

print(list(x))