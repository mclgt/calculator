import expression_parser
import memory_handler
memory=memory_handler.Memory()
parser=expression_parser.ExpressionParser(memory)
while(True): 
    print("Insert your expression here:")
    expression=input()
    result=parser.parse(expression)  
    print("Result:", result)
    if isinstance(result, (int, float)):
        memory.save(expression,result)