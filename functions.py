# def create_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = create_name("stepan","sokolov")
# print(full_name)

#deffault args
# def net_price(list_price,discount=0,tax=0.05):
#     return list_price * (1-discount) * (1+tax)

# print(net_price(500))

# import time

# def count(end,start=0): #def args must follow custom args, so user doesn't need to input them
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")

# count(5)

#keyword args
# def hello(greeting,title,first,last):
#     print(f"{greeting} {title}{first} {last}")

# hello("Hello",first="Spongebob",last="Sqarepants",title="Mr.")

# def get_phone(country,area,first,last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=1,area=123,first=456,last=7890)
# print(phone_num)

#arbitrary args

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1,2,3,4,5,6))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr.","Stepan","Sokolov")

# def print_adress(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_adress(street="123 Fake St.",apt="100",city="Detroit",state="MI",zip="12345")

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print(value,end=" ")
shipping_label("Dr.","Spongebob","Sqarepants","III",street = "123 Fake St.",apt="100",state="MI",zip="12345")