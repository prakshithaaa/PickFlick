blocked = ["Adarsh","Shimshi","Vasu"]
contact = ["Navn","Adarsh","Shimshi","Vasu","Kvk"]

for i in contact:
    if i in blocked:
        print(i, "is blocked, skipping...")
        continue
    print("Sending message to",i)
    