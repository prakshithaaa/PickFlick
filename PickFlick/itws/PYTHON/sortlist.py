#sort acc to last digit

def last(x):
    return x%10

list = [11,40,26,75,99]

list.sort(key = last)
print(list)