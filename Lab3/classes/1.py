class Console:
    def __init__(self):
        self.string = ""  # атрибут экземпляра

    def getstring(self):
        self.string = input("Введите строку: ")

    def printstring(self):
        print(self.string)
