def print_tkt (total, taken):
    left = total - taken
    print(left, "left")
    return left 

capacity = 50
order = int(input("How many?"))
capacity = print_tkt (capacity, order)