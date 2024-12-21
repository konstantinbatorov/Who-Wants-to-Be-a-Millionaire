from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QGroupBox, QButtonGroup, QMessageBox
)
from random import *


class Question():
    def init(self, question_text, right_answer, answer1, answer2, answer3, right_help, help1, help2, help3):
        self.question_text = question_text
        self.right_answer = right_answer
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.right_help = right_help
        self.help1 = help1
        self.help2 = help2
        self.help3 = help3


questions = list()
questions.append(Question('Что такое десница?', 'Рука', 'Бровь', 'Глаз', 'Шея', '45', '30', '15','10'))
questions.append(Question('В какое море впадает река Урал?', 'Каспийское', 'Азовское', 'Чёрное', 'Средиземное','30','25','10','35'))
questions.append(Question('Как называется каменный монумент на котором установлен памятник Петру 1 в Санкт-Петербурге?', 'Гром камень', 'Гора камень', 'Дом камень', 'Разрыв камень', '50','25','10','15'))
questions.append(Question('Какое животное имеет второе название ?', 'Пума', 'Ацелот', 'Леопард', 'Пантера', '34', '20', '36', '10'))
questions.append(Question('Что в России 19-го века делали в дортуаре?', 'Спали', 'Ели', 'Ездили верхом', 'Купались', '40', '30', '20', '10'))
questions.append(Question('Какая из планет солнечная система самая горячая ?', 'Венера', 'Сатурн', 'Земля', 'Плутон', '21', '38', '29', '12'))
questions.append(Question('Из каких плодов можно получить копру?', 'Кокос', 'Ананас', 'Вишная', 'Абрикос', '10', '12', '8', '70'))
questions.append(Question('Какой химический элемент обозначается символом O?', 'Кислород', 'Золото', 'Олово', 'Осмий', '80', '1', '9', '10'))
questions.append(Question('Кто написал роман «Война и мир»?', 'Лев Толстой', 'Фёдор Достоевский', 'Антон Чехов', 'Александр Пушкин', '24', '25', '26', '25'))
questions.append(Question('В каком году произошла Великая Октябрьская Революция?', '1917', '1914', '1921', '1939', '14', '22', '40', '24'))
questions.append(Question('Какая из этих картин принадлежит кисти Иеронима Босха?', 'Сад земных наслаждений', 'Крик', 'Звёздная ночь', 'Тайная вечеря', '48', '24', '2', '26'))
questions.append(Question('В какой стране находится пустыня Руб-эль-Хали?', 'Саудовская Аравия', 'Египет', 'Иран', 'Индия', '90', '0', '3', '7'))
questions.append(Question('Какой физический процесс описывает уравнение Шрёдингера?', 'Движение частиц в квантовом поле', 'Распад атома', 'Электромагнитное излучение', 'Сопротивление материалов', '30', '53', '12', '5'))
questions.append(Question('Какой город был столицей Османской империи доо Константинополя?', 'Бруса', 'Эдирне', 'Анкара', 'Измир', '40', '20', '10', '30'))
questions.append(Question('Какой элемент имеет атомный номер 92 ?', 'Уран', 'Радон', 'Торий', 'Плутоний', '20', '20', '20', '40'))
questions.append(Question('В какой части человеческого тела находится гипофиз?', 'В мозге', 'В сердце', 'В печени', 'В почках', '31', '31', '31', '7'))

players = dict()



def auth():
    global nickname
    RadioGroupBox.hide()
    ResultGroupBox.hide()
    help_button1.hide()
    help_button2.hide()
    help_button3.hide()
    nickname_edit.show()
    question.setText('Напишите своё имя')
    ok.setText('Авторизоваться')


    



#показ формы ответа
def show_result():
    RadioGroupBox.hide()
    ResultGroupBox.show()
    ok.setText('Следующий вопрос')

#показ формы вопроса
def show_question():
    ResultGroupBox.hide()
    RadioGroupBox.show()
    ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    radiobutton1.setChecked(False)
    radiobutton2.setChecked(False)
    radiobutton3.setChecked(False)
    radiobutton4.setChecked(False)
    RadioGroup.setExclusive(True)


#задание вопроса
def ask(q: Question):
    shuffle(answers)
    q = questions[q - 1]
    question.setText(q.question_text)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.answer1)
    answers[2].setText(q.answer2)
    answers[3].setText(q.answer3)
    correct.setText(q.right_answer)
    show_question()

#показ вопроса
def next_question():
    
    nickname_edit.hide()
    ask(players[nickname])

#показ ответа
def show_correct(result_text):
    result.setText(result_text)
    show_result()

#проверка ответа
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильный ответ!')
        players[nickname] += 1
        print(players[nickname])
        
    else:
        show_correct('Неправильный ответ!')

        finish()

def click_ok():
    if ok.text() == 'Следующий вопрос':
        help_button1.show()
        help_button2.show()
        help_button3.show()
        next_question()
        finish()

    elif ok.text() == 'Ответить':
        help_button1.hide()
        help_button2.hide()
        help_button3.hide()
        check_answer()
    elif ok.text() == 'Авторизоваться':
        global nickname
        nickname = nickname_edit.text()
        if nickname in players.keys():
            finish()
        else:
            players[nickname] = 1
            help1_flag = True
            help2_flag = True
            help3_flag = True
            next_question()
            help_button1.show()
            help_button2.show()
            help_button3.show()


def rating():
    print(players)
def finish():
    ok.setText('Авторизоваться')
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    
    if players[nickname] == 15:
        auth()
        question.setText('Вы победили! Давайте ещё раз?')
        msg.setText('Поздравляем! Вы выигрывайте миллион рублей!')

        
    else:
        auth()
        question.setText('Вы проиграли! Приходите через год!')
    
        msg.setText('К сожалению, для вас наша игра заканчивается! Вы ответили на ' + str(players[nickname]) + ' вопросов из 15')
    
    rating()
    msg.exec_()


def helper1():
    global help1_flag
    if help1_flag:
        answers[2].setText(' ')
        answers[3].setText(' ')
        help1_flag = False

def helper2():
    global help2_flag
    if help2_flag:
        ask(-1)
        help2_flag = False
        

def helper3():
    global help3_flag
    if help3_flag:
        q = questions[players[nickname]]
        answers[0].setText(q.right_answer + ' ' + q.right_help)
        answers[1].setText(q.answer1 + ' ' + q.help1)
        answers[2].setText(q.answer2 + ' ' + q.help2)
        answers[3].setText(q.answer3 + ' ' + q.help3)
        help3_flag = False

#приложение и окно
app = QApplication([])
window = QWidget()
window.setWindowTitle('Кто хочет стать миллионером?')
window.resize(512, 384)

help1_flag = True
help2_flag = True
help3_flag = True

#форма авторизации

nickname_edit = QLineEdit()
nickname = ''

#подсказка
help_button1 = QPushButton('50 на 50')
help_button2 = QPushButton('Поменять вопрос')
help_button3 = QPushButton('Помощь зала')


#вопрос и ответ
question = QLabel('Вопрос?')
ok = QPushButton('Ответить')

#форма вопроса
RadioGroupBox = QGroupBox('Варианты ответов:')
radiobutton1 = QRadioButton('Вариант 1')
radiobutton2 = QRadioButton('Вариант 2')
radiobutton3 = QRadioButton('Вариант 3')
radiobutton4 = QRadioButton('Вариант 4')
answers = [radiobutton1, radiobutton2, radiobutton3, radiobutton4]
RadioGroup = QButtonGroup()
RadioGroup.addButton(radiobutton1)
RadioGroup.addButton(radiobutton2)
RadioGroup.addButton(radiobutton3)
RadioGroup.addButton(radiobutton4)

#расположение формы вопроса
HBoxLayout = QHBoxLayout()
VBoxLayout1 = QVBoxLayout()
VBoxLayout2 = QVBoxLayout()
VBoxLayout1.addWidget(radiobutton1)
VBoxLayout1.addWidget(radiobutton2)
VBoxLayout2.addWidget(radiobutton3)
VBoxLayout2.addWidget(radiobutton4)
HBoxLayout.addLayout(VBoxLayout1)
HBoxLayout.addLayout(VBoxLayout2)
RadioGroupBox.setLayout(HBoxLayout)

#форма ответа
ResultGroupBox = QGroupBox('Результат теста:')
result = QLabel('Правильный ответ/Неправильный ответ')
correct = QLabel('Ответ')

#расположение формы ответа
VBoxLayout3 = QVBoxLayout() #это центральная линия
VBoxLayout3.addWidget(result, alignment = Qt.AlignLeft | Qt.AlignTop)
VBoxLayout3.addWidget(correct, alignment = Qt.AlignCenter, stretch = 2)
ResultGroupBox.setLayout(VBoxLayout3)



#расположение всего
VLayout = QVBoxLayout()
HLayout1 = QHBoxLayout()
HLayout2 = QHBoxLayout()
HLayout3 = QHBoxLayout()
HLayout4 = QHBoxLayout()

HLayout2.addWidget(nickname_edit)
HLayout1.addWidget(question, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
HLayout2.addWidget(RadioGroupBox)
HLayout2.addWidget(ResultGroupBox)
HLayout3.addStretch(1)
HLayout3.addWidget(ok, stretch = 2)
HLayout3.addStretch(1)
HLayout4.addWidget(help_button1)
HLayout4.addWidget(help_button2)
HLayout4.addWidget(help_button3)
VLayout.addLayout(HLayout1, stretch = 2)
VLayout.addLayout(HLayout2, stretch = 8)
VLayout.addStretch(1)
VLayout.addLayout(HLayout3, stretch = 1)
VLayout.addLayout(HLayout4, 4)
VLayout.addStretch(1)
VLayout.setSpacing(5)
window.setLayout(VLayout)
ResultGroupBox.hide()


#подсказки







auth()
ok.clicked.connect(click_ok)

help_button1.clicked.connect(helper1)
help_button2.clicked.connect(helper2)
help_button3.clicked.connect(helper3)






window.show()
app.exec_()