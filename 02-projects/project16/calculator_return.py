def multiply(a, b):
    return a * b

answer = multiply(7, 8)

print("Answer:", answer)


#---------------------------------
#تست چالش این تمرین   
#---------------------------------


def hello():
    print("Hello")

result = hello() #اینجا تابع اول یک بار اجرا می شه

print(result) # چون خروجی فقط پرینت بوده هیچی نداره 

#اگر تابع return نداشته باشد، به طور پیش‌فرض None برمی‌گرداند.