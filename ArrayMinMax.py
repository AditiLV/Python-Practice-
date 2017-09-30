a = []
while True:
    i = input("Enter")
    if(i != "done"):
        a.append(int(i))
        print(a)
    else:
        print(a)
        print("max:",max(a))
        print("min:",min(a))
        
    
