battery = 100
while True:
    if (battery < 5):
        break
    elif (battery <= 20):
        print("Low Battery:", battery)
    
    else:
        print(battery)
    battery -= 1