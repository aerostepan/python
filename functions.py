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

import time

def count(end,start=0): #def args must follow custom args, so user doesn't need to input them
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(5)

