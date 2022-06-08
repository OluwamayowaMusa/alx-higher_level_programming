def multiply_list_map(my_list=[], number=0):
    def f(x): return (x * number)
    return (list(map(f, my_list)))
