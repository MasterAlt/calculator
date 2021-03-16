# Objective: create a calculator
a = int(input('enter first  number:'))
b = int(input('enter second number:'))

def main():
    print("This is calculator app")
    ans=mul()
    print("the product is",ans)
    ans=div()

def mul():
    prod=a*b
    return prod

def div():
	try:
		div=a/b
		print("division is",div)
	except :
		print("cannot be divided by zero")
    
if __name__ == "__main__":
    main()
