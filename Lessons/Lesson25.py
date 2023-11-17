# def fun1(parametr):
#     return parametr * 2

# def fun2(parametr):
#     return argument *2

# argument = 100
# print(fun1(argument), fun2(argument))

# x = 200
# print(fun1(x), fun2(x))


# create teble arr3 (id int, x int[])
# insert into arr values
# (1, '{1,2,3}'::int[]);
# (2, '{111,222,333,444}');
# select * from arr4
# select id, x[1] as the_first from arr


# select* from author1
# intersect
# select * from author2


# select* from author1
# except
# select * from author2


# # ! PyQt6 - графический модуль:
# from PyQt6.QtWidgets import QApplication, QWidget
# import sys
# app = QApplication(sys.argv)
# window = QWidget()
# window.show()
# app.exec()


# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton
# app = QApplication(sys.argv)
# window = QPushButton('Push me!')
# window.show()
# app.exec()


# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()
# app.exec()


# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle('My App')
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()


# * Кнопки:
# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('My App')
#         button = QPushButton('Press Me Again!')
#         self.setFixedSize(QSize(400, 300))
#         self.setCentralWidget(button)
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()


# * Кнопка которая возвращает Click!
# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('My App')
#         self.button = QPushButton('Press me!')
#         self.button.setCheckable(True)
#         self.button.clicked.connect(self.the_button_was_clicked)  # Fix the typo here
#         self.setCentralWidget(self.button)

#     def the_button_was_clicked(self):
#         print('Clicked!')

# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()


#  * Кнопка меняющая себя!

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('My App')
#         self.button = QPushButton('Press me!')
#         self.button.setCheckable(True)
#         self.button.clicked.connect(
#             self.the_button_was_clicked)  # Fix the typo here
#         self.setCentralWidget(self.button)
#         self.status = '1'

#     def the_button_was_clicked(self):
#         if self.status == '1':
#             print('clicked1')
#             self.button.setText('Other!')
#             self.status = '2'
#         else:
#             print('Clicked2')
#             self.button.setText('Press Me!')
#             self.status = '1'

# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()


# * Окошко и там надпись жирная HELLO:
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle('My App')
#         label = QLabel('Hello!')
#         font = label.font()
#         font.setPointSize(30)
#         label.setFont(font)
#         label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
#         self.setCentralWidget(label)

# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()


# # * Клавиша, а над ней меняющаяся надпись:
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('My App!')

#         button = QPushButton('Press me!')
#         button.setFixedSize(QSize(200, 200))
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)

#         self.label = QLabel('Hello!')
#         font = self.label.font()
#         font.setPointSize(10)
#         self.label.setFont(font)
#         self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

#         layout = QVBoxLayout()
#         widgets = [self.label, button]
#         for w in widgets:
#             layout.addWidget(w)

#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#         self.status = '1'

#     def the_button_was_clicked(self):
#         if self.status == '1':
#             print('Clicked 1')
#             self.label.setText('Push me!')
#             self.status = '2'
#         else:
#             print('Clicked 2')
#             self.label.setText('Touch me!')
#             self.status = '1'

# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()


# # * Окошко для надписи и вовзаращает в терминал 'Text is changing...':
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle('My App')

#         widget = QLineEdit()
#         widget.setMaxLength(25)
#         widget.setPlaceholderText('Enter your text: ')

#         widget.returnPressed.connect(self.return_pressed)
#         widget.selectionChanged.connect(self.selection_changed)
#         widget.textChanged.connect(self.text_changed)
#         widget.textEdited.connect(self.text_edited)

#         self.setCentralWidget(widget)

#     def return_pressed(self):
#         print('Return pressed!')

#     def selection_changed(self):
#         print('Selected changed')

#     def text_changed(self, s):
#         print('Text is changing...')
#         print(s)

#     def text_edited(self, s):
#         print('Text edited...')
#         print(s)


# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()


# * Программу которую я переписал у преподавателя (графический интерфейс):
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QLineEdit, QPushButton, QTextEdit,
    QVBoxLayout, QWidget
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tf = True
        self.text = 'Нажмите Enter!'
        self.setWindowTitle('My app!')
        self.resize(300, 300)

        layout = QVBoxLayout()

        widget0 = QLabel('Введите выражение, ')
        font = widget0.font()
        font.setPointSize(10)
        widget0.setFont(font)
        widget0.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                             Qt.AlignmentFlag.AlignVCenter)

        widget1 = QLabel('Нажмите Enter!')
        font = widget1.font()
        font.setPointSize(10)
        widget1.setFont(font)
        widget1.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                             Qt.AlignmentFlag.AlignVCenter)

        self.widget2 = QLineEdit()
        self.widget2.setMaxLength(20)

        self.widget2.returnPressed.connect(self.return_pressed)
        self.widget2.selectionChanged.connect(self.selection_changed)
        self.widget2.textChanged.connect(self.text_changed)
        self.widget2.textEdited.connect(self.text_edited)
        self.widget2.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        button = QPushButton('Результат!')
        button.setCheckable(True)
        button.setStyleSheet(
            'background: rgb(127, 255, 0); color: rgb(0, 128, 128);')  # Здесь изменения
        button.clicked.connect(self.the_button_was_clicked)

        self.label_result = QLabel()

        self.qte = QTextEdit()
        self.qte.append('Здесь будет результат')

        widgets = [widget0, widget1, self.widget2,
                   button, self.label_result, self.qte]
        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def return_pressed(self):
        print('Return pressed!')
        self.text = self.widget2.text()

    def selection_changed(self):
        print('Selection changed')

    def text_changed(self, s):
        print('Text changed...')
        print(s)

    def text_edited(self, s):
        print('Text edited...')
        print(s)

    def the_button_was_clicked(self):
        print('Clicked!')
        self.label_result.setText(self.text)

        try:
            res = str(eval(self.text))
            self.qte.append(res)
        except:
            self.qte.append('Ошибка')

        if self.tf:
            self.setWindowTitle('Result')
            self.tf = False
        else:
            self.tf = True
            self.setWindowTitle('My_App :)')


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
