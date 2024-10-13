'''
The rgb function is incomplete.
Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
'''


def rgb(r, g, b):
    # Функция для ограничения значений от 0 до 255
    def clamp(value):
        return max(0, min(255, value))

    # Применяем функцию clamp ко всем компонентам цвета
    r = clamp(r)
    g = clamp(g)
    b = clamp(b)

    # Преобразование RGB в HEX формат
    hex_color = f'{r:02X}{g:02X}{b:02X}'

    # Преобразование RGB в HSL формат
    r_norm, g_norm, b_norm = r / 255, g / 255, b / 255
    max_color = max(r_norm, g_norm, b_norm)
    min_color = min(r_norm, g_norm, b_norm)
    delta = max_color - min_color

    # Вычисление яркости (Luminance)
    l = (max_color + min_color) / 2

    # Вычисление насыщенности (Saturation)
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))

    # Вычисление оттенка (Hue)
    if delta == 0:
        h = 0
    elif max_color == r_norm:
        h = (60 * ((g_norm - b_norm) / delta) + 360) % 360
    elif max_color == g_norm:
        h = (60 * ((b_norm - r_norm) / delta) + 120) % 360
    else:
        h = (60 * ((r_norm - g_norm) / delta) + 240) % 360

    # Форматирование значений HSL
    hsl_color = (round(h), round(s * 100), round(l * 100))

    # Вывод всех форматов
    print("Цвет в HEX формате:", hex_color)
    print(f"Цвет в RGB формате: ({r}, {g}, {b})")
    print(f"Цвет в HSL формате: ({hsl_color[0]}, {hsl_color[1]}%, {hsl_color[2]}%)")


# Пример использования
rgb(148, 0, 211) # фиолетовый цвет
rgb(14, 232, 88) # салатовый цвет