from itertools import accumulate

items_tuples = [
        ("map", 9,150),
        ("compass", 13,35),
        ("water", 153,200),
        ("sandwich", 50,160),
        ("glucose", 15,60),
        ("tin", 68,45),
        ("banana", 27,60),
        ("apple", 39,40),
        ("cheese", 23,30),
        ("beer", 52,10),
        ("suntan cream", 11,70),
        ("camera", 32,30),
        ("T-shirt", 24,15),
        ("trousers", 48,10),
        ("umbrella", 73,40),
        ("waterproof trousers", 42,70),
        ("waterproof overclothes", 43,75),
        ("note-case", 22,80),
        ("sunglasses", 7,20),
        ("towel", 18,12),
        ("socks", 4,50),
        ("book", 30,10)
        ]

volume = 400

def foo(items, volume):
    sorted_items = sorted(items, key=lambda x: x[1]/x[2])
    
    knapsnack = []
    for item in sorted_items:
        if sum([x[1] for x in knapsnack]) + item[1] <= volume:
            knapsnack.append(item) 
    print(knapsnack, sum([x[1] for x in knapsnack]), sum([x[2] for x in knapsnack]))        

def get_items(items, num):
    list_items = []
    i = num
    while i != 0:
        x = items[i % len(items)]
        if x not in list_items:
            list_items.append(x)
        i = i // len(items)
    return list_items

def get_volume(l):
    return sum([x[1] for x in l])

def get_value(l):
    return sum([x[2] for x in l])

def get_keys(items):
    return [x[0] for x in items]

def run_brootforce(items, volume):
    
    num = old_max_value = 0
    while True:
        l = get_items(items, num)
        if get_volume(l) <= volume:
            if get_value(l) > old_max_value:
                old_max_value = get_value(l)
                print(get_keys(l), get_volume(l), get_value(l), num)
        num = num + 1
        if (num % 1000000) == 0:
            print(num)
    return 0


if __name__ == "__main__":
    #foo(items_tuples, volume)
    #for i in range(1000):
        #print(get_items(items_tuples, i))
    run_brootforce(items_tuples, volume)
    #['note-case', 'waterproof overclothes', 'waterproof trousers', 'suntan cream', 'sandwich', 'map', 'water'] 330 805 227576685

















