class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0 and (self.getIntbyIndex(x, self.getIntLength(x)-1 )!= 0 or self.getIntLength(x) == 0) and x == self.reverseInt(x): #проверка чтобы (либо число не оканчивалось на 0, либо его длина больше 1), было положительным, и равно самому себе перевёрнутому
            return True
        else:
            return False
    def reverseInt(self, x) -> int: #переворачивает число
        self.__output = 0
        self.__x = x
        self.__len = self.getIntLength(self.__x)

        for i in range(self.__len):
            self.__output += self.getIntbyIndex(x, i) * (10**i)
        return self.__output
    def getIntLength(self, x): #возвращает длину числа
        self.__x = x
        self.__out = 0

        while self.__x != 0:
            self.__x //= 10
            self.__out += 1
        return self.__out
    def getIntbyIndex(self, number, index): #возвращает цифру из числа, по индексу
        self.__number = number
        self.__index = index

        #отсекаем часть числа правее искомой цифры
        self.__k = self.getIntLength(self.__number) - 1 - self.__index
        self.__number //= 10 ** self.__k

        #получаем искомую цифру простым остатком от деления на 10
        self.__output = self.__number % 10
        return self.__output

s = Solution()
print(s.isPalindrome(101101))
