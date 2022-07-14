class PrintList():
    fruits = ['Mango', 'Manzana', 'Pera', 'Melon']
    fruits = [fruit.upper() for fruit in fruits]
    print(fruits)

    def suma(self):
        sum = 1+1
        print(sum)
        

a= PrintList()
a.fruits
a.suma()