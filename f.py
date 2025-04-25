import sys

from PyQt6.QtGui import QFont, QColor, QPainter
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QPushButton, QButtonGroup, QLineEdit, QMessageBox
from PyQt6.QtWidgets import QLCDNumber, QMainWindow


class MyProgr(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle('Главное окно')

        self.calc = QPushButton('Калькулятор', self)
        self.calc.clicked.connect(self.conect)
        self.calc.move(50, 100)

        self.metr = QPushButton('Перевод длины', self)
        self.metr.clicked.connect(self.met)
        self.metr.move(150, 100)

        self.gr = QPushButton('Скидки', self)
        self.gr.clicked.connect(self.graph)
        self.gr.move(50, 140)

        self.al = QPushButton('Валюта', self)
        self.al.clicked.connect(self.alf)
        self.al.move(150, 140)

        self.vac = QPushButton('V и S', self)
        self.vac.clicked.connect(self.va)
        self.vac.move(50, 180)

    def conect(self):
        self.ex = Calculator()
        self.ex.show()

    def met(self):
        self.ex = trans()
        self.ex.show()

    def graph(self):
        self.ex = discount()
        self.ex.show()

    def alf(self):
        self.ex = valut()
        self.ex.show()

    def va(self):
        self.ex = vacalc()
        self.ex.show()


class valut(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 200, 400, 100)
        self.setWindowTitle('Конвертер валют')

        self.currency_from = QComboBox(self)
        self.currency_from.move(50, 10)
        self.currency_from.addItems(['Доллары', 'Евро', 'Рубли', 'Кроны', 'Тенге'])

        self.amount_input = QLineEdit(self)
        self.amount_input.move(50, 60)
        self.amount_input.resize(90, 20)

        self.input_label = QLabel('Ввод:', self)
        self.input_label.move(10, 60)

        self.result_label = QLabel(self)
        self.result_label.move(310, 60)
        self.result_label.resize(100, 18)

        self.result_text = QLabel('Результат:', self)
        self.result_text.move(250, 60)

        self.currency_to = QComboBox(self)
        self.currency_to.move(250, 10)
        self.currency_to.addItems(['Доллары', 'Евро', 'Рубли', 'Кроны', 'Тенге'])

        self.convert_button = QPushButton('-->', self)
        self.convert_button.move(150, 30)
        self.convert_button.clicked.connect(self.convert)

    def convert(self):
        try:
            amount = float(self.amount_input.text())
            if amount <= 0:
                raise ValueError("Число должно быть положительным")
            currency_from = self.currency_from.currentText()
            currency_to = self.currency_to.currentText()

            exchange_rates = {
                'Доллары': {'Евро': 0.85, 'Рубли': 75.0, 'Кроны': 8.5, 'Тенге': 420.0},
                'Евро': {'Доллары': 1.18, 'Рубли': 88.0, 'Кроны': 10.0, 'Тенге': 500.0},
                'Рубли': {'Доллары': 0.013, 'Евро': 0.011, 'Кроны': 0.11, 'Тенге': 5.6},
                'Кроны': {'Доллары': 0.12, 'Евро': 0.10, 'Рубли': 9.0, 'Тенге': 50.0},
                'Тенге': {'Доллары': 0.0024, 'Евро': 0.0020, 'Рубли': 0.18, 'Кроны': 0.02}
            }

            if currency_from == currency_to:
                self.result_label.setText(str(amount))
            else:
                rate = exchange_rates[currency_from][currency_to]
                result = amount * rate
                self.result_label.setText(str(round(result, 2)))
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", "Введите корректное положительное число")


class discount(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 200, 400, 100)
        self.setWindowTitle('Калькулятор скидки')

        self.price_input = QLineEdit(self)
        self.price_input.move(20, 40)
        self.price_input.resize(90, 20)

        self.price_label = QLabel('Начальная цена:', self)
        self.price_label.move(10, 10)

        self.discount_input = QLineEdit(self)
        self.discount_input.move(250, 40)
        self.discount_input.resize(90, 20)

        self.discount_label = QLabel('Скидка (%):', self)
        self.discount_label.move(200, 10)

        self.result_label = QLabel(self)
        self.result_label.move(310, 60)
        self.result_label.resize(100, 18)

        self.result_text = QLabel('Итоговая цена:', self)
        self.result_text.move(220, 60)

        self.calculate_button = QPushButton('Рассчитать', self)
        self.calculate_button.move(150, 40)
        self.calculate_button.clicked.connect(self.calculate_discount)

    def calculate_discount(self):
        try:
            price = float(self.price_input.text())
            discount = float(self.discount_input.text())
            if price <= 0:
                raise ValueError("Цена должна быть положительной")
            if discount < 0 or discount > 100:
                raise ValueError("Скидка должна быть от 0 до 100%")
            final_price = price * (1 - discount / 100)
            self.result_label.setText(f"{final_price:.2f}")
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", str(e))


class vacalc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Площадь и Объем")
        self.setGeometry(100, 100, 400, 200)

        self.label_length = QLabel('Длина:', self)
        self.label_length.move(50, 20)

        self.input_length = QLineEdit(self)
        self.input_length.move(100, 20)

        self.label_width = QLabel('Ширина:', self)
        self.label_width.move(50, 50)

        self.input_width = QLineEdit(self)
        self.input_width.move(100, 50)

        self.label_height = QLabel('Высота:', self)
        self.label_height.move(50, 80)

        self.finish = QLabel(self)
        self.finish.move(250, 50)
        self.finish.resize(100, 12)

        self.input_height = QLineEdit(self)
        self.input_height.move(100, 80)

        self.btn_calculate = QPushButton("Объем", self)
        self.btn_calculate.move(75, 120)
        self.btn_calculate.clicked.connect(self.ob)

        self.btn_cal = QPushButton("Площадь", self)
        self.btn_cal.move(175, 120)
        self.btn_cal.clicked.connect(self.pl)

    def ob(self):
        try:
            l = float(self.input_length.text())
            w = float(self.input_width.text())
            h = float(self.input_height.text())
            if l <= 0 or w <= 0 or h <= 0:
                raise ValueError("Числа должны быть положительными")
            self.finish.setText("Объем: " + str(l * w * h))
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", "Введите корректные положительные числа")

    def pl(self):
        try:
            l = float(self.input_length.text())
            w = float(self.input_width.text())
            if l <= 0 or w <= 0:
                raise ValueError("Числа должны быть положительными")
            self.finish.setText("Площадь: " + str(l * w))
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", "Введите корректные положительные числа")


class trans(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 200, 400, 100)
        self.setWindowTitle('Перевод длины')

        self.cx = QComboBox(self)
        self.cx.move(50, 10)
        self.cx.addItems(['Километры', 'Метры', 'Сантиметры', 'Миллиметры'])

        self.sel = QLineEdit(self)
        self.sel.move(50, 60)
        self.sel.resize(90, 20)

        self.v = QLabel('Ввод:', self)
        self.v.move(10, 60)

        self.res = QLabel(self)
        self.res.move(310, 60)
        self.res.resize(100, 18)

        self.wes = QLabel('Результат:', self)
        self.wes.move(250, 60)

        self.cx2 = QComboBox(self)
        self.cx2.move(250, 10)
        self.cx2.addItems(['Километры', 'Метры', 'Сантиметры', 'Миллиметры'])

        self.sw = QPushButton('-->', self)
        self.sw.move(150, 30)
        self.sw.clicked.connect(self.col)

    def col(self):
        try:
            value = float(self.sel.text())
            if value <= 0:
                raise ValueError("Число должно быть положительным")
            tet = self.cx.currentText()
            tet2 = self.cx2.currentText()
            if tet == tet2:
                self.res.setText(str(value))
            elif tet == 'Метры' and tet2 == 'Сантиметры':
                self.res.setText(str(value * 100))
            elif tet == 'Метры' and tet2 == 'Миллиметры':
                self.res.setText(str(value * 1000))
            elif tet == 'Сантиметры' and tet2 == 'Метры':
                self.res.setText(str(value / 100))
            elif tet == 'Сантиметры' and tet2 == 'Миллиметры':
                self.res.setText(str(value * 10))
            elif tet == 'Миллиметры' and tet2 == 'Метры':
                self.res.setText(str(value / 1000))
            elif tet == 'Миллиметры' and tet2 == 'Сантиметры':
                self.res.setText(str(value / 10))
            elif tet == 'Километры' and tet2 == 'Метры':
                self.res.setText(str(value * 1000))
            elif tet == 'Километры' and tet2 == 'Сантиметры':
                self.res.setText(str(value * 100000))
            elif tet == 'Километры' and tet2 == 'Миллиметры':
                self.res.setText(str(value * 1000000))
            elif tet == 'Метры' and tet2 == 'Километры':
                self.res.setText(str(value / 1000))
            elif tet == 'Сантиметры' and tet2 == 'Километры':
                self.res.setText(str(value / 100000))
            elif tet == 'Миллиметры' and tet2 == 'Километры':
                self.res.setText(str(value / 1000000))
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", "Введите корректное положительное число")


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 250, 450)
        self.setWindowTitle('Калькулятор')

        self.b1 = QPushButton('1', self)
        self.b1.move(10, 250)
        self.b1.resize(50, 50)

        self.b2 = QPushButton('2', self)
        self.b2.move(60, 250)
        self.b2.resize(50, 50)

        self.b3 = QPushButton('3', self)
        self.b3.move(110, 250)
        self.b3.resize(50, 50)

        self.b4 = QPushButton('4', self)
        self.b4.move(10, 200)
        self.b4.resize(50, 50)

        self.b5 = QPushButton('5', self)
        self.b5.move(60, 200)
        self.b5.resize(50, 50)

        self.b6 = QPushButton('6', self)
        self.b6.move(110, 200)
        self.b6.resize(50, 50)

        self.b7 = QPushButton('7', self)
        self.b7.move(10, 150)
        self.b7.resize(50, 50)

        self.b8 = QPushButton('8', self)
        self.b8.move(60, 150)
        self.b8.resize(50, 50)

        self.b9 = QPushButton('9', self)
        self.b9.move(110, 150)
        self.b9.resize(50, 50)

        self.b0 = QPushButton('0', self)
        self.b0.move(60, 300)
        self.b0.resize(50, 50)

        self.btn_clear = QPushButton('C', self)
        self.btn_clear.move(10, 300)
        self.btn_clear.resize(50, 50)
        self.btn_clear.clicked.connect(self.clear)

        self.main_label = QLCDNumber(self)
        self.main_label.move(12, 110)
        self.main_label.resize(195, 40)
        self.main_label.setFont(QFont('Arial', 25))

        self.pl = QPushButton('+', self)
        self.pl.move(160, 150)
        self.pl.resize(50, 50)
        self.pl.setFont(QFont('Arial', 12))

        self.min = QPushButton('-', self)
        self.min.move(160, 200)
        self.min.resize(50, 50)

        self.umn = QPushButton('*', self)
        self.umn.move(160, 250)
        self.umn.resize(50, 50)

        self.delu = QPushButton('/', self)
        self.delu.move(160, 300)
        self.delu.resize(50, 50)

        self.step = QPushButton('^', self)
        self.step.move(10, 350)
        self.step.resize(50, 50)

        self.btn_dot = QPushButton('.', self)
        self.btn_dot.move(110, 300)
        self.btn_dot.resize(50, 50)
        self.btn_dot.clicked.connect(self.add_char)

        self.btn_eq = QPushButton('=', self)
        self.btn_eq.move(110, 350)
        self.btn_eq.resize(100, 50)
        self.btn_eq.clicked.connect(self.evaluate_result)

        self.btn_sqrt = QPushButton('√', self)
        self.btn_sqrt.move(60, 350)
        self.btn_sqrt.resize(50, 50)
        self.btn_sqrt.clicked.connect(self.sqrt)

        self.number_buttons = QButtonGroup(self)
        self.number_buttons.addButton(self.b0)
        self.number_buttons.addButton(self.b1)
        self.number_buttons.addButton(self.b2)
        self.number_buttons.addButton(self.b3)
        self.number_buttons.addButton(self.b4)
        self.number_buttons.addButton(self.b5)
        self.number_buttons.addButton(self.b6)
        self.number_buttons.addButton(self.b7)
        self.number_buttons.addButton(self.b8)
        self.number_buttons.addButton(self.b9)

        self.znaku = QButtonGroup(self)
        self.znaku.addButton(self.pl)
        self.znaku.addButton(self.min)
        self.znaku.addButton(self.umn)
        self.znaku.addButton(self.delu)
        self.znaku.addButton(self.step)

        for i in self.number_buttons.buttons():
            i.clicked.connect(self.add_char)
        for i in self.znaku.buttons():
            i.clicked.connect(self.calc)

        self.a = ''
        self.b = ''

    def clear(self):
        self.a = ''
        self.b = ''
        self.main_label.display('0')

    def add_char(self):
        if self.sender().text() == '.':
            if '.' in self.a:
                return
        if self.a != '0' or (self.a == '0' and self.sender().text() == '.'):
            self.a = self.a + self.sender().text()
            self.b = self.b + self.sender().text()
            self.main_label.display(self.a)
        else:
            self.a = self.sender().text()
            self.b = self.sender().text()
            self.main_label.display(self.a)

    def sqrt(self):
        if self.b:
            self.b = f'({self.b})**0.5'

    def evaluate_result(self):
        try:
            self.a = eval(self.b)
            self.b = str(self.a)
            self.main_label.display(self.a)
        except Exception as _:
            self.main_label.display('Error')
        self.a = ''

    def calc(self):
        if self.b:
            self.evaluate_result()
            if self.b[-1] not in ['+', '-', '/', '*']:
                self.b += self.sender().text()
            else:
                self.b = self.b[0:len(self.b) - 1] + self.sender().text()
            self.b = self.b.replace('^', '**')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyProgr()
    ex.show()
    sys.exit(app.exec())
