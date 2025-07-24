print('Задание №1')
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def calculate_area(self):
        return self.width * self.length
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
    

rectangle1 = Rectangle(5, 7)
rectangle2 = Rectangle(4, 2)
rectangle3 = Rectangle(6, 6)

print(f'Area is {rectangle1.calculate_area()} and Perimeter is {rectangle1.calculate_perimeter()}')
print(f'Area is {rectangle2.calculate_area()} and Perimeter is {rectangle2.calculate_perimeter()}')
print(f'Area is {rectangle3.calculate_area()} and Perimeter is {rectangle3.calculate_perimeter()}')



print('\nЗадание №2')
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def addition(self):
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")

    def multiplication(self):
        result = self.a * self.b
        print(f"Умножение: {self.a} * {self.b} = {result}")

    def division(self):
        if self.b:
            result = self.a / self.b
            print(f"Деление: {self.a} / {self.b} = {result}")
        else:
            print("Ошибка: деление на ноль!")

    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")
        

math_operations = Math(10, 5)
math_operations.addition()
math_operations.multiplication()
math_operations.division()
math_operations.subtraction()

math_zero = Math(10, 0)
math_zero.division()     
    
    
print('\nЗадание №3')
class SidebarButton:
    
    type: str = 'Кнопка'
    
    def __init__(self, text, loc = ""):
        self.text = text
        self.loc = loc

    def click(self):
        return f'Клик по кнопке {self.text}'
    

buttons = [
    SidebarButton('Text Box'),
    SidebarButton('Check Box'),
    SidebarButton('Radio Button'),
    SidebarButton('Web Tables'),
    SidebarButton('Buttons'),
    SidebarButton('Links'),
    SidebarButton('Broken Links - Images'),
    SidebarButton('Upload and Download'),
    SidebarButton('Dynamic Properties')
]

for button in buttons:
    print(f'Текст кнопки: {button.text}')
    print(f'Тип элемента: {button.type}')
    print(f'Локатор: {button.loc}')

print('\n') 

for button in buttons:
    print(button.click())