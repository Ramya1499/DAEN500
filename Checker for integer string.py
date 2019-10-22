a = input()
count = 0

for i in range(0, lan(a)):
          if(a[i]== "," or a[i]=="." or a[i]=="!"):
                   print("no")
                   break
          else:
               count=count+1
if(count==len(a)):
        print("yes")
