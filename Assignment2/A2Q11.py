def evaluate(expr):
    result=eval(expr)
    print(result)

def main():
    expr=input('enter an expression: ')
    evaluate(expr)

if __name__=='__main__':
    main()
