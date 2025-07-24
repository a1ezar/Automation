# class Button:
    
#     type: str = 'Кнопка'
    
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link

# home = Button('Домой', '/home')
# catalog_msk = Button('Каталог', '/msk/catalog')


# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


# class ButtonTwo:
#     def __init__(self, text, link, loc):
#         self.text = text
#         self.link = link
#         self.loc = loc
#     def click(self):
#         return "Клик по локатору - {}".format(self.loc)

# home_two = ButtonTwo('Домой', '/home', 'button#home')
# print(home_two.click())

from task_9_checks import Checks

class Input(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text


class Button(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text


class Title(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text


class Link(Checks):
   def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text


input = Input('Поиск', 'input#search')
button = Button('Поиск', 'button#search')
title = Title('Поиск', 'title#search')
link = Link('Поиск', 'link#search')

print(input.check_text())
print(button.check_text())
print(title.check_text())
print(link.check_text())       
