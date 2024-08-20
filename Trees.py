import turtle


class LSystem2D:
    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom  # инициатор (минимальный фрактал)
        self.state = axiom  # строка с набором команд
        self.width = width  # толщина линии рисования
        self.length = length  # длина одного линейного сегмента кривой
        self.angle = angle  # фиксированный угол поворота
        self.t = t  # сама черепашка
        self.rules = {}  # словарь правил формирования кривых (F, рисовать линию)
        self.t.pensize(self.width)  # ширина линии рисования

    def add_rules(self, *rules):  # добавляем правила, например F-> F+F--F+F
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        for n in range(n_iter):  # перебираем правила
            for key, value in self.rules.items():
                ''' заменяем текущий маршрут на новый подставляя вместо
                 ключа значения из правил, причем переводим значения 
                 ключей в нижний регистр, для избегания ошибок'''
                self.state = self.state.replace(key, value.lower())
            self.state = self.state.upper()  # меняем регистр обратно

    def set_turtle(self, my_tuple):
        self.t.up()  # поднять черепашку
        self.t.goto(my_tuple[0], my_tuple[1])  # переносим в нужные координаты
        self.t.seth(my_tuple[2])  # устанавливаем угол поворота
        self.t.down()  # опускаем черепашку

    def draw_turtle(self, start_pos, start_angle):
        turtle.tracer(1, 0)  # форсажный режим
        self.t.up()  # поднимаем черепаху (линия не рисуется)
        self.t.setpos(start_pos)  # начальная стартовая позиция
        self.t.seth(start_angle)  # начальный угол поворота
        self.t.down()  # опускаем черепаху (рисуем линию)
        turtle_stack = []  # стек, хранящий данные для ветвления
        for move in self.state:  # перебираем набор команд
            if move == 'F':  # рисует отрезок
                self.t.fd(self.length)
            elif move == 'S':  # не рисует отрезок
                self.t.up()
                self.t.fd(self.length)
                self.t.down()
            elif move == '+':  # поворот на заданный угол влево
                self.t.lt(self.angle)
            elif move == '-':  # поворот на заданный угол вправо
                self.t.rt(self.angle)
            elif move == '[':  # начало стека
                # Данные для вевления: координаты (x,y), угол поворота, толщина
                turtle_stack.append((self.t.xcor(), self.t.ycor(),  # линии
                                     self.t.heading(), self.t.pensize()))
            elif move == ']':  # конец стека
                xcor, ycor, head, w = turtle_stack.pop()  # извлекаем из стека данные
                self.set_turtle((xcor, ycor, head))  # возвращаем черепашку в координаты ветвления
                self.width = w  # толщина линии
                self.t.pensize(self.width)  # установка толщины для черепашки

        #turtle.done()  # Не закрывать окно после отрисовки


def window():
    width = 1200
    height = 600
    screen = turtle.Screen()
    screen.setup(width, height, 0, 0)


def main():
    window()  # параметры окна

    # Черепашка
    t = turtle.Turtle()
    t.ht()  # Скроем черепашку

    pen_width = 1  # толщина линии (пиксель)
    f_len = 7  # длинна 1 сегмента прямой (пиксель)
    angle = 22.5  # фиксированный угол поворота (градус)

    axiom = "F"  # дерево 33
    '''axiom = "F" # дерево 33, дерево2 25.7, дерево3 22.5
    axiom ="A" # дерево1 33
    '''

    l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
    l_sys.add_rules(('F','FF-[-F+F+F]+[+F-F-F]')) # дерево2
    '''l_sys.add_rules(('F', 'F[+F]F[-F]F')) # дерево, дерево2
    l_sys.add_rules(('F','FF'),('A', 'F[+A][-A]')) # дерево1
    l_sys.add_rules(('F','F[+F]F[-F]F')) # дерево2
    '''
    l_sys.generate_path(5)  # фрактал определенной точности (количество итераций)
    l_sys.draw_turtle((0, -300), 90)  # -900, 400; -180

    '''# Создаем новые L-системы для повтора фракталов (получится одуваньчик) 
    for i in range(15):
        ls = LSystem2D(t, axiom, pen_width, f_len, angle)
        ls.add_rules(('F', 'FF'), ('A', 'F[+A][-A]'))
        ls.generate_path(7)
        ls.draw_turtle((0, -200), 160-i*10)'''

    turtle.done()  # Теперь закрываем окно после всех отрисовок

if __name__ == "__main__":
    main()
