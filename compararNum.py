def comparar(n):
    if n >= 1 and n <= 100:
        if n % 2 != 0:
            print("Weird")
        elif n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6  and n <= 20:
            print("Not Weird")
        elif n % 2 ==0 and n > 20:
            print("Not Weird")
    else:
        print("Numero incorrecto")
   


if __name__ == '__main__':
    n = int(input().strip())
    comparar(n)