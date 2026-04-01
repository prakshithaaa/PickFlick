list = [1,4,7,22,10]
seen = False
for i in list:
    if (i == 10):
        seen = True

if (seen == False):
    print("10 is not in the list")
else:
    print("Found 10!")