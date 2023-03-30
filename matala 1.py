#Q1
def my_func(x1,x2,x3):
    lst=[x1,x2,x3]
    count=0
    for i in lst:
        s=str(i)
        if type(i)!=type(s):
            if sum(lst)!=0:
                f=float(i)
                if type(i)==type(f): 
                    count+=1
                    if count<len(lst):
                        continue
                    else:
                        solv=((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
                        print(solv)
                else:
                    print("Erorr:parameters should be float")
                    break 
            else:
               print("Not a number – denominator equals zero”")
               break
        else:
            return(None)
            break
   



#Q 2
def Revword(lst):
   lst1=[]
   lst2=[]
   for i in lst:
       for j in i:
           w=j[::-1].lower()
           lst1.append(w)
       lst2.append(lst1)
       lst1=[]
   return(lst2)




def count():
    file_name=open("text.txt")
    data=file_name.readlines()  
    lst=[]
    for line in data:
        lst.append(line.rstrip().split(" "))
    word=lst[0][0]
    lst=lst[1:]
    correct_text=Revword(lst)
    count=0
    for i in correct_text:
        for j in i:
            if j=="first":
                count+=1
            else:
                continue

    print(count+1)
    
        
  
    

count()