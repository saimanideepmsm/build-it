def f(x):
    print(x,"---------")
    def g(y):
        print(y,"---------")
        return y
    return g#returning the funtion when f(x) is called
a=5
b=1
h=f(a)# f(x) funtion is assinged to h
print(h(b))# now we are calling f(g(b)) as h(b) ella ardam chesko..