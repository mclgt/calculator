import expression_parser
import memory_handler
memory=memory_handler.Memory()
parser=expression_parser.ExpressionParser(memory)
while(True): 
    print ("\nSelect an operation:\n1.Evaluate Expression\n2.See history\n")
    choice=input()
    if choice=='1':
        print("Insert your expression here:\n(Use ans to refer to the last result)\n")
        expression=input()
        result=parser.parse(expression)  
        print("Result:", result)
        if isinstance(result, (int, float)):
            memory.save(expression,result)
    elif choice=='2': 
        print(memory.show_history())
    else: 
        print("Invalid choice")