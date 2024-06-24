l = []
range_list = int(input("Enter how many number inserted :"))
[l.append(input("Enter Number"))for i in range(range_list)]
for x in range(0,range_list):
    while len(l) > x:
        user = input("enter wala or naa : ").lower()
        if user == "naa": l.pop(x),print(l)
        elif user == "wala":l.pop(),print(l)      
    else: break
 
    

                
      
        



    
     