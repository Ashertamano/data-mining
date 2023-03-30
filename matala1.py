#1
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
   
    
my_func("e",0,0)
            

