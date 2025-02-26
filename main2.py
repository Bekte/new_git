# str, int, float, bool, ячейка-пренменн, коробка

# a = 7
# b = 2
# print(a // b)

# + - * / // %

# бесконечный
# i = 0
# while i <= 4:
#     i+=1
#     print('Hello world')

# перебирающий
# временное переменное - i
# for i in range(1, 6):
#     print(i)
#
# empty_lst = []
# for i in range(1, 100):
#     empty_lst.append(i)
# print(empty_lst)

# word = 'Hello'
# for i in word:
#     print(i)
# срезы
# print(word[1:4])


# if elif else theory &&&&&


# number = int(input('Enter a number '))
#
# if number > 0:
#     print('seloe')
# elif number < 0:
#     print("neseloe")
# else:
#     print('It is 0')


# home work

# set
# frozenset
# none
# register
# parol * 2 raza
# 996
# while
#

# register


# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# signs = ['"', "'", '@', '#', '*', '&', '&','?']
# name = input('Enter your name: ')
# for i in name:
#     if i in numbers:
#         print('Please enter only letters!')
#
# mobile = input('Enter your number:')
# if not mobile.startswith('996'):
#     print('It must start with "996"! ')
# elif len(mobile) != 12:
#     print("The number's length is incorrect.")
# elif mobile[3] not in ['7', '9', '5', '2']:
#     print("The number is incorrect.")
# # for i in mobile:
# #     if i not in numbers:
# #         print("Please enter only numbers!.")
#
# else:
#     print('не корректные данные')


# lambda - анонимная функция
# def name():
# def index():
#     print(1234)
#
# index()
#
# print(1234)

# num = {'asa','asa',1,1,1,12345}
# num.add('asa')
# print(num)
#
# num = frozenset([])

# users = ('alsan','aza','oppa')
# users_list = list(users)
# users_list.append(('Ainagul'))
# users = tuple(users_list)
# print(users)


# names = ['jhc']
# 1 f"His name is{i}" в чем функция???? конкантинация
# 2

# 1 абстракция - базовый класс - Car
# 2 полиморфизм -
# 3 наследование - родительные, дочерные
# 4 инкапсуляция -
# init
# что такое класс?
# обьект,

# user
# account

# метеды строк, for inside for 3*

class Bank:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        print(f"Name: {self.name}, ID of the institution: {self.id}")


class Customer(Bank):

    def __init__(self, name, id, status, balance):
        super().__init__(name, id)
        self.__balance = balance
        self.status = status
    # public , private , zashishe obhod

    def get_info(self):
        print(f"Name: {self.name}, ID of the institution: {self.id}, Balace:{self.__balance}")


    def __get_status(self):
        print(self.status)




    def add(self, number):
        self.__balance += number
    # доп. атрибут метода number

    def out(self, number):
        if number > self.__balance:
            print("You don't have enough money")
        else:
            self.__balance -= number


Asan = Customer('Asan', 1, True, 120)
# Asan.get_info()
# print(Asan.add(50))
# print(Asan.get_info())
# Asan.out(180)

print(Asan.get_info())
print(Asan._Customer__get_status())




# декомпозиция
# скрипты не требует venv
# venv изучать!
# инкапсуляция
# полиморфизм
# множество














