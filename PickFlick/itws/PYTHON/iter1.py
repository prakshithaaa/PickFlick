n = int(input("Input="))
roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

i=0
total=0

while i < len(n):
    if i+1 < len(n) and roman[n[i]] < roman[n[i+1]]:
        total += roman[n[i+1]] - roman[n[i]]
        i += 2
    else:
        total += roman[n[i]]
        i += 1
        
print("Output=", total)