age=input("Please Enter Your Age")
age=int(age)

if 0<age<=3:
    print("ticket price : Free")
elif 3<age<=10:
    print("ticket price : 200")
elif 10<age<=18:
    print("ticket price : 400")
elif 18<age<=30:
    print("ticket price : 600")
elif 30<age<=200:
    print("ticket price : 100")
elif 0>=age<=0:
    print("please entaer coreeact age")
        