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

    def draw_turtle(self, start_pos, start_angle):
        turtle.tracer(1, 0)  # форсажный режим
        self.t.up()  # поднимаем черепаху (линия не рисуется)
        self.t.setpos(start_pos)  # начальная стартовая позиция
        self.t.seth(start_angle)  # начальный угол поворота
        self.t.down()  # опускаем черепаху (рисуем линию)

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
    f_len = 10  # длинна 1 сегмента прямой (пиксель)
    angle = 60  # фиксированный угол поворота (градус)

    axiom = "F"  # прямая Коха 60 градусов
    '''axiom = "F" # прямая Коха 60 градусов
    axiom = "F--F--F" # снежинка Коха 60 градусов
    axiom ="F-F-F-F" # крестик из прямоугольных фракталов 90 градусов
    axiom ="F+F+F+F" # обратный крест/ ковер из прямоугольников 90
    axiom ="FX" # дракон Хартера-Хайтвея 90
    axiom ="FXF--FF--FF" # ковер Серпинского 60
    axiom ="X" # Кривая Гилберта 90'''

    l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
    l_sys.add_rules(('F', 'F+F--F+F'))  # прямая/снежинка Коха
    '''l_sys.add_rules(('F','F+F--F+F')) # прямая/снежинка Коха
    # крестик из прямоугольных фракталов 90 градусов
    l_sys.add_rules(('F','F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F'))
    # Ковер из прямоугольников
    l_sys.add_rules(('F', 'F+S-FF+F+FF+FS+FF-S+FF-F-FF-FS-FFF'), ('S', 'SSSSS'))
    l_sys.add_rules(('FX','FX+FY+'),('FY','-FX-FY')) # дракон Хартера-Хайтвея
    l_sys.add_rules(('F','FF'),('X','--FXF++FXF++FXF--')) # ковер Серпинского
    l_sys.add_rules(('X','-YF+XFX+FY-'),('Y','+XF-YFY-FX+')) # Кривая Гилберта'''
    l_sys.generate_path(3)  # фрактал определенной точности (количество итераций)
    l_sys.draw_turtle((0, 0), 0)  # -900, 400; -180

    turtle.done()  # Теперь закрываем окно после всех отрисовок

if __name__ == "__main__":
    main()
