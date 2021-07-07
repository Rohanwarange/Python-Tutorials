from csv import DictWriter
with open("file3,csv","w") as wf:
    dict_write=DictWriter(wf,fieldnames=["First_name","Last_name","age"])
    dict_write.writeheader()
    # using WriteRow
    # dict_write.writerow({
    #  "First_name":"Rohan",
    #  "Last_name":"Warange",
    #  "age":24
    # })
    # dict_write.writerow({
    #  "First_name":"sanjay",
    #  "Last_name":"Warange",
    #  "age":56
    # })
    # dict_write.writerow({
    #  "First_name":"jignesh",
    #  "Last_name":"Warange",
    #  "age":20
    # })
    # dict_write.writerow({
    #  "First_name":"sarika",
    #  "Last_name":"Warange",
    #  "age":48
    # })

# using Writerows
    dict_write.writerows([{"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    {"First_name":"Rohan","Last_name":"Warange","age":24},
    
    ])