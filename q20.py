#calculator
a=int(input("ENTER FIRST NUMBER:"))
b=int(input("ENTER SECOND NUMBER:"))
op=input("ENTER OPERATION TO BE PERFORMED (+,-,*,/):")
if op=="+":
    print("SUM IS:",a+b)
elif op=="-":
    print("DIFFERENCE IS:",a-b)
elif op=="*":
    print("PRODUCT IS:",a*b)
elif op=="/":
    if b!=0:
        print("QUOTIENT IS:",a/b)
    else:
        print("DIVISION BY ZERO IS NOT ALLOWED")