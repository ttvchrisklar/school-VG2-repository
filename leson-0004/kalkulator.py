# program som fungerer som en kalkulator
calculatorInpute = []
print("plise note this is a work in progres project, there is a cople of things to note:")
print("1: after doing a number input you will need a function before inputing a new number, you can delite the last input")

def askifwantmoreinpute(a):
    askformoreinpute = a
    while askformoreinpute == True:
        print("do you want a functuoin or a new number? or stopp")
        choise = input("new number(1)/Function(2)/delite last insertet number/diget(3)/calculate(4)/stopp(5): ")
        x = int(choise)
        if x == 1:
            print("new number.")
            inputenewnumberintoarray()
        elif x == 2:
            print("function.")
            functionsinpute()
        elif x == 3:
            print("deliting last insertetd item")
            calculatorInpute.pop() 
            print(calculatorInpute)  
        elif x == 4:
            print("now calculating")  
            askformoreinpute = False
            mathfunction()       
        elif x == 5: 
            print("now stopping.")
            aksifwanttorerun()
        else:
            print("error, try agen")

def inputenewnumberintoarray():
    x= input("whats the number: ")
    a = float(x)
    calculatorInpute.append(a)
    print(calculatorInpute)

def functionsinpute():
    a = input("input one of these: (/), (*), (-), (+): ")
    if a == "/" or a == "*" or a == "-" or a == "+":
        calculatorInpute.append(a)
        print(calculatorInpute)

def mathfunction():
    a=0
    i=0
    while i < 3:
        if len(calculatorInpute) == 1:
            print("done")
            print(calculatorInpute)
            break
        if calculatorInpute[i] == '/' or calculatorInpute[i] == '*' or calculatorInpute[i] == '-' or calculatorInpute[i] == '+':
            if calculatorInpute[i] == '/':
                a = calculatorInpute[i-1]/calculatorInpute[i+1]
            elif calculatorInpute[i] == '*':
                a = calculatorInpute[i-1]*calculatorInpute[i+1]
            elif calculatorInpute[i] == '-':
                a = calculatorInpute[i-1]-calculatorInpute[i+1]
            elif calculatorInpute[i] == '+':
                a = calculatorInpute[i-1]+calculatorInpute[i+1]
            print(a)
            calculatorInpute.pop(i+1)
            calculatorInpute.pop(i)
            calculatorInpute.pop(i-1)
            calculatorInpute.insert(0,a)
            i = 0
        i+=1
def runtheprogram():
    askifwantmoreinpute(True)

def aksifwanttorerun():
    print("do you want to stop the calculator?")
    a = input("y/n: " )
    if a == "y":
        exit()
    if a == "n":
        rerunthecalculator(True)
                
def rerunthecalculator(a):
    askifwantmoreinpute(a)

runtheprogram()
