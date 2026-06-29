equation=input("Type your equation   ")
x=int(equation.split()[0])
op=equation.split()[1]
y=int(equation.split()[2])

match op:
    case "+":
        print(float(x+y))
    case "-":
        print(float(x-y))
    case "*":
        print(float(x*y))
    case "/":
        print(float(round((x/y), 1)))