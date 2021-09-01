def es_primo(num: int) -> bool:
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

def run():
    es_primo(10)

if __name__ == '__main__':
    run()