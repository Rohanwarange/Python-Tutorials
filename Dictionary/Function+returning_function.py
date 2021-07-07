def outer_func():
    def inner_func():
        print("india is my country")
    return inner_func
s=outer_func()
print(s())        