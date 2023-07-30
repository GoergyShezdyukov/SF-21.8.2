from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(int(input('укажите сторону прямоугольника: ')),
                   int(input('укажите сторону прямоугольника: ')))
rect_2 = Rectangle(int(input('укажите сторону прямоугольника: ')),
                   int(input('укажите сторону прямоугольника: ')))

square_1 = Square(int(input('укажите сторону квадрата: ')))
square_2 = Square(int(input('укажите сторону квадрата: ')))

circle_1 = Circle(int(input('укажите радиус круга: ')))
circle_2 = Circle(int(input('укажите радиус круга: ')))

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(int(figure.get_area_circle()))
    else:
        print(figure.get_area())