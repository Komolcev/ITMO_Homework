# # 25-1:
# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout


# class Calculator(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Калькулятор')
#         self.setGeometry(100, 100, 400, 200)

#         layout = QVBoxLayout()

#         # "Число А
#         num1_layout = QVBoxLayout()
#         self.num1_label = QLabel('Число А:', self)
#         num1_layout.addWidget(self.num1_label)
#         self.num1_input = QLineEdit(self)
#         num1_layout.addWidget(self.num1_input)
#         layout.addLayout(num1_layout)

#         # Число Б
#         num2_layout = QVBoxLayout()
#         self.num2_label = QLabel('Число Б:', self)
#         num2_layout.addWidget(self.num2_label)
#         self.num2_input = QLineEdit(self)
#         num2_layout.addWidget(self.num2_input)
#         layout.addLayout(num2_layout)

#         # Центральная область для кнопок и операций
#         central_layout = QHBoxLayout()

#         # Клавиши цифр от 0 до 9
#         num_layout = QVBoxLayout()
#         for i in range(1, 10):
#             button = QPushButton(str(i), self)
#             button.clicked.connect(lambda ch=i: self.append_to_input(str(ch)))
#             num_layout.addWidget(button)

#         # Клавиша 0
#         button_0 = QPushButton('0', self)
#         button_0.clicked.connect(lambda: self.append_to_input('0'))
#         num_layout.addWidget(button_0)

#         central_layout.addLayout(num_layout)

#         # Клавиши операций и кнопка "Сброс"
#         operation_layout = QVBoxLayout()
#         button_add = QPushButton('+', self)
#         button_subtract = QPushButton('-', self)
#         button_multiply = QPushButton('*', self)
#         button_divide = QPushButton('/', self)
#         button_reset = QPushButton('Сброс', self)

#         button_add.clicked.connect(lambda: self.calculate('+'))
#         button_subtract.clicked.connect(lambda: self.calculate('-'))
#         button_multiply.clicked.connect(lambda: self.calculate('*'))
#         button_divide.clicked.connect(lambda: self.calculate('/'))
#         button_reset.clicked.connect(self.reset)

#         operation_layout.addWidget(button_add)
#         operation_layout.addWidget(button_subtract)
#         operation_layout.addWidget(button_multiply)
#         operation_layout.addWidget(button_divide)
#         operation_layout.addWidget(button_reset)

#         central_layout.addLayout(operation_layout)

#         layout.addLayout(central_layout)

#         # Нижняя область для "Результата"
#         self.result_label = QLabel('Результат: ', self)
#         layout.addWidget(self.result_label)

#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Добавим стили для красивого вида
#         self.setStyleSheet(
#             "QLabel { font-size: 14px; }"
#             "QLineEdit { font-size: 14px; }"
#             "QPushButton { font-size: 14px; padding: 5px; }"
#         )

#     def append_to_input(self, value):
#         current_text = self.sender().text()
#         current_input = self.num1_input if self.num1_input.hasFocus() else self.num2_input
#         current_input.setText(current_input.text() + current_text)

#     def calculate(self, operation):
#         try:
#             num1 = float(self.num1_input.text())
#             num2 = float(self.num2_input.text())
#             result = 0

#             if operation == '+':
#                 result = num1 + num2
#             elif operation == '-':
#                 result = num1 - num2
#             elif operation == '*':
#                 result = num1 * num2
#             elif operation == '/':
#                 if num2 != 0:
#                     result = num1 / num2
#                 else:
#                     self.result_label.setText('Ошибка: деление на ноль')
#                     return

#             self.result_label.setText(f'Результат: {result}')

#         except ValueError:
#             self.result_label.setText('Ошибка: введите числа')

#     def reset(self):
#         self.num1_input.clear()
#         self.num2_input.clear()
#         self.result_label.clear()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     calculator = Calculator()
#     calculator.show()
#     sys.exit(app.exec())


# # 25-2
# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     if len(s) <= 1:
#         return True
#     elif s[0] == s[-1]:
#         return is_palindrome(s[1:-1])
#     else:
#         return False

# input_str = str(input('Введите строку на проверку на полиндромность: '))
# result = is_palindrome(input_str)
# print(result)


# # 25-3
# def to_camel_case(input_string):
#     words = input_string.split()
#     camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
#     camel_case_string = ''.join(camel_case_words)
#     return camel_case_string


# input_str = str(input('Введите строку: '))
# camel_case_result = to_camel_case(input_str)
# print(camel_case_result)
