def main():
    
    number = int(input("Enter a number: "))

    maxx = float("-inf")
    minn = float("+inf")

    if number > maxx:
        maxx = number
    
    elif number < minn:
        minn = number

    print(f"Maximum is {maxx}")
    print(f"Minimum is {minn}")
    
main()