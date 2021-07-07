# in keyword and itteration
user_info={
    'name':'rohan',
    'age':24,
     'fave-movies':['shole','dabang','dil bechAEA'],
    'fave-songs':['shole1234','4567dabang','dil66666 bechAEA']
 }
#  check key exists in dict or not
# if "nameq" in user_info:
#     print("Present")
# else:
#     print("not Present")

# #  check value exists in dict or not
# if 24 in user_info.values():
#     print("Present")
# else:
#     print("not Present")

# loops in dictionaries
# for i in user_info:
#     print(user_info[i])

# items method
# user_items=user_info.items()
# print(user_items)
# print(type(user_items))

for key,value in user_info.items(): 
    print(f"keys in user_info is {key} and values in user_info is {value}")



