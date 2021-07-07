fruits=['graps','mango','apple']
print(sorted(fruits))

# dictionary sorting
guitars=[
    {"model":"uwueu","price":12314},
    {"mode2":"udsdgwueu","price":32314},
    {"mode3":"uwu33eu","price":123314},
    {"mode4":"uwueweeeu","price":452314}

]
print(sorted(guitars,key=lambda d:d["price"]))