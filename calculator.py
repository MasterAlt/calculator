# Objective: create a calculator
inputVariable1 = int(input('enter first  number:'))
inputVariable2 = int(input('enter second number:'))

def main():
    print("This is calculator app")
    ans=mul()
    print("the product is",ans)
    ans=div()

def mul():
    prod=inputVariable1*inputVariable2
    return prod

def div():
	try:
		div=inputVariable1/inputVariable2
		print("division is",div)
	except :
		print("cannot be divided by zero")
    
if __name__ == "__main__":
    main()
