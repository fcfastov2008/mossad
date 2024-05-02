result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        try:
            operand1 = int(input("Input number: "))
        except:
            print(f"{operand1} is not a number. Try again.")
            continue
        wait_for_number = False
        if result and operator:
            if operator == '+':
                result += operand1
            elif operator == '-':
                result -= operand1
            elif operator == '*':
                result *= operand1
            elif operator == '/':
                if operand1 == 0:
                    print("Error: division by 0")
                else:
                    result /= operand1
        else:
            result = operand1    
    else:
            operator = input("Input operaor (+, -, *, /,=): ")
            if operator not in ['+', '-', '*', '/','=']:
                print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")
                continue        
            wait_for_number = True
            if operator == '=':
                print(f'Result: {result}')
                break

    
 