import turtle


def draw_koch_segment(t, way):
    if way>6:
        new_way = way //3
        draw_koch_segment(t, new_way)
        t.left(60)
        draw_koch_segment(t, new_way)
        t.right(120)
        draw_koch_segment(t, new_way)
        t.left(60)
        draw_koch_segment(t, new_way)
    else:
        t.fd(way)
        t.left(60)
        t.fd(way)
        t.right(120)
        t.fd(way)
        t.left(60)
        t.fd(way)


def main():
    SEGMENT = 150 # от значения сегмента зависит количество уровней фрактала,
    direction = 'L' # 'R'
    # чем больше сегментов, тем сложнее фрактал
    width = 1200
    height = 800
    screen = turtle.Screen()
    screen.setup(width, height, 0, 0)

    tortoise = turtle.Turtle()
    tortoise.ht()
    tortoise.speed(180)
    draw_koch_segment(tortoise, SEGMENT)
    if direction=='R':
        for i in range(2):
            tortoise.right(120)
            draw_koch_segment(tortoise, SEGMENT)
    else:
        for i in range(2):
            tortoise.left(120)
            draw_koch_segment(tortoise, SEGMENT)
    turtle.done()


if __name__ == "__main__":
    main()
