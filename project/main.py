from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QListWidget, QLineEdit, QTextEdit
import json


app = QApplication([])
window = QWidget()

# countries = {
#     'Россия': 'Самая большая страна в мире',
#     'Китай': 'Самая населенная страна в мире'
# }

# with open('countries.json', 'w', encoding='utf-8') as file:
#     json.dump(countries, file)

list_countries = QListWidget()
text_countries = QTextEdit()
name_countries = QLineEdit()
add_country_button = QPushButton('Добавить страну')
del_country_button = QPushButton('Удалить страну')
edit_country_button = QPushButton('Изменить страну')

main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
right_layout = QVBoxLayout()
layout_button = QHBoxLayout()

#Постройка лэйаутов
layout_button.addWidget(add_country_button)
layout_button.addWidget(del_country_button)
layout_button.addWidget(edit_country_button)

left_layout.addWidget(list_countries)
right_layout.addWidget(text_countries)
right_layout.addWidget(name_countries)
right_layout.addLayout(layout_button)

main_layout.addLayout(left_layout, 3)
main_layout.addLayout(right_layout, 7)

window.setLayout(main_layout)

with open('countries.json', 'r', encoding='utf-8') as file:
    countries = json.load(file)
    for country in countries:
        list_countries.addItem(country)


#Стайлинг окна
window.setWindowTitle('Путеводитель')
window.resize(800, 600)
window.setStyleSheet("border: 2px solid; border-color:black; background-color:red; font-size: 18px; font-family: Georgia; font-style: italic; color: white")
name_countries.setPlaceholderText('Введите страну...')

def info_country():
    country = list_countries.selectedItems()[0].text()
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    text_country = countries[country]
    text_countries.setText(text_country)

    
def add_country():
    country = name_countries.text()
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    countries[country] = ''
    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(countries, file)
    list_countries.clear()
    for country in countries:
        list_countries.addItem(country)
    name_countries.clear()

    
def del_country():
    if list_countries.selectedItems():
        country = list_countries.selectedItems()[0].text()
        with open('countries.json', 'r', encoding='utf-8') as file:
            countries = json.load(file)
        del countries[country]
        list_countries.clear()
        for country in countries:
            list_countries.addItem(country)
        with open('countries.json', 'w', encoding='utf-8') as file:
            json.dump(countries, file)


def edit_country():
    if list_countries.selectedItems():
        country = list_countries.selectedItems()[0].text()
        with open('countries.json', 'r', encoding='utf-8') as file:
            countries = json.load(file)
        text_country = text_countries.toPlainText()
        countries[country] = text_country
        with open('countries.json', 'w', encoding='utf-8') as file:
            json.dump(countries, file)

add_country_button.clicked.connect(add_country)
del_country_button.clicked.connect(del_country)
edit_country_button.clicked.connect(edit_country)
list_countries.itemClicked.connect(info_country)


window.show()
app.exec()