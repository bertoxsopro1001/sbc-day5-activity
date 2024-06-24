range_list,l = int(input("Enter how many number inserted :")),[]
[l.append(input("Enter Number :"))for i in range(range_list)]
while len(l) > 0:
        user = input("enter wala or naa : ").lower()
        if user == "naa": l.pop(0),print(l)
        elif user == "wala":l.pop(),print(l)      
else : print(f"List is empty - {l}" ) 

