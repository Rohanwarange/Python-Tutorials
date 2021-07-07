# dictionary_compenhension
# square={1:1,2:4,3:9}

# square={f"square of {num}":num**2 for num in range(1,11)}
# for k,v in square.items():
#     print(f'{k}:{v}')
string="RohanSanjayWarange"
WordCount={char:string.count(char) for char in string}
print(WordCount)