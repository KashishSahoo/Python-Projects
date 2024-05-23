import os
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)

op={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    n1=float(input("Enter 1st Number="))

    for s in op:
        print(s)
    continue_falg=True 

    while continue_falg:
        op_s=input("Pick An Operartion=")
        n2=float(input("Enter next number="))
        c_func=op[op_s]
        output=c_func(n1,n2)
        print(f"{n1} {op_s} {n2} = {output}") 


        s_c=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation and 'x' to exit=").lower()


        if s_c=='y':
            n1=output
        elif s_c=='n':
            continue_falg=False
            os.system('cls')
            calculator()
        else:
          continue_falg=False
          print( "Bye")

calculator()
        
    
  
        


    
        
       
  

    

 
    



  







