
def main():
    for i in range (0, 101):
        if i%5==0 and i%3==0 :
            print("fizzbuzz")
        if i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)
if __name__ == '__main__':
    main()


