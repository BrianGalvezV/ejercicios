def clousor():
    def f():
        print('hello')
    return f

def run():
    f = clousor()
    f()

if __name__ == '__main__':
    run()