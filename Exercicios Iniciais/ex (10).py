def main(a=0,b=0):
    if a <= b:
        for i in range(a,b+1):
            print(i)
    else:
        for i in range(b,a+1):
            print(i)

if __name__ == '__main__':
    main(1,10)
    