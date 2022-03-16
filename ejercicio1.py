class lista:
    def __init__(self,list):
        self.list=list
    def tamaño(self):
        for i in range(len(self.list)):
            print(f'{i+1}- {self.list[i]}')
        print(len(self.list))


lista1=[1,2,3,4,5]
lista(lista1).tamaño()