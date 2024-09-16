
while True:
    op= input("what operation do you want to do? (*,/,+,-,**)")
    num1= float(input("what is the first number in the equation? "))
    num2= float(input("what is the second number in the equation? "))
    if op== "+":
        awnswer= num1 + num2
    elif op == "-":
        awnswer= num1 - num2
    elif op == "*":
        awnswer= num1 * num2
    elif op == "/":
        awnswer= num1 / num2
    elif op == "**":
        awnswer= num1 ** num2

    print( num1, op, num2, "=", awnswer)

    con= input("calculate again?(y/n)")
    if con=="n":
        break

