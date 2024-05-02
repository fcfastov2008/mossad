result = 0
operand = None
operator = None
wait_for_number = True
num = 0

while True:
                      
    if wait_for_number :

        try:
            num = float(input("N: "))
        except ValueError:
            print(f"{operator} is not a number.Try again")
            continue      
        else:
             operand = num
             wait_for_number = False
             
    else:
        operator = input("")
        if operator not in ['+', '-', '*', '/','=']:
            print(f"{operator} is not ['+', '-', '*', '/','=', Try again")
            continue

        wait_for_number = True

        if operand is not None and operator is not None:           
       
            if operator == "+":
                result = result + operand 
            elif operator == "-":
                result = result - operand 
            elif operator == "*":
                result = result * operand 
            elif operator == '/':
                result /= operand 
            
            
           
        if operator == '=':
            print("Результат:",result )
            break
            

            
          
            
