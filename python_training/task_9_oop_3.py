class Soda:
    def __init__(self, sup=None):
        self.sup = sup
        
    def show_my_drink(self):
        if self.sup:
            print(f'Газировка и {self.sup}')
        else:
            print('Обычная газировка')
            
default = Soda()
orange = Soda('Orange')

default.show_my_drink()
orange.show_my_drink()