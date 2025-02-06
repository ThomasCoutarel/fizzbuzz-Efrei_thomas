def fizzbuzz(n):
    result=[]
    for i in range (n):
        if i%5==0 and i%3==0 :
            result.append("fizzbuzz")
        elif i%3==0:
            result.append("fizz")
        elif i%5==0:
            result.append("buzz")
        else:
            result.append(i)
    return result

def main():
    resultat=fizzbuzz(101)
    print(resultat)

if __name__ == '__main__':
    main()


