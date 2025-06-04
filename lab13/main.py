from abc import ABC, abstractmethod
from math import pi, sqrt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

# Плотности материалов (кг/м³)
MATERIALS = {
    'Алюминий': 2700,
    'Железо': 7870,
    'Дерево': 700,
    'Золото': 19320
}

class GeometricBody(ABC):
    """Абстрактный класс геометрического тела"""
    def __init__(self, material):
        self.material = material
        self.density = MATERIALS.get(material, 1000)
    
    @abstractmethod
    def volume(self):
        pass
    
    @abstractmethod
    def surface_area(self):
        pass
    
    def mass(self):
        return self.volume() * self.density
    
    def __str__(self):
        return f"{self.__class__.__name__} ({self.material})"

class Parallelepiped(GeometricBody):
    """Класс параллелепипеда"""
    def __init__(self, a, b, c, material):
        super().__init__(material)
        self.a = a
        self.b = b
        self.c = c
    
    def volume(self):
        return self.a * self.b * self.c
    
    def surface_area(self):
        return 2 * (self.a*self.b + self.b*self.c + self.a*self.c)
    
    def __repr__(self):
        return f"Parallelepiped(a={self.a}, b={self.b}, c={self.c})"

class Tetrahedron(GeometricBody):
    """Класс тетраэдра"""
    def __init__(self, a, material):
        super().__init__(material)
        self.a = a
    
    def volume(self):
        return (self.a ** 3) / (6 * sqrt(2))
    
    def surface_area(self):
        return sqrt(3) * (self.a ** 2)
    
    def __repr__(self):
        return f"Tetrahedron(a={self.a})"

class Sphere(GeometricBody):
    """Класс шара"""
    def __init__(self, r, material):
        super().__init__(material)
        self.r = r
    
    def volume(self):
        return (4/3) * pi * (self.r ** 3)
    
    def surface_area(self):
        return 4 * pi * (self.r ** 2)
    
    def __repr__(self):
        return f"Sphere(r={self.r})"

class GeometryApp(App):
    def build(self):
        self.current_body = None
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Выбор фигуры
        self.shape_spinner = Spinner(
            text='Выберите фигуру',
            values=('Параллелепипед', 'Тетраэдр', 'Шар')
        )
        self.shape_spinner.bind(text=self.on_shape_select)
        
        # Поля параметров
        self.param1 = TextInput(hint_text='Параметр 1', disabled=True)
        self.param2 = TextInput(hint_text='Параметр 2', disabled=True)
        self.param3 = TextInput(hint_text='Параметр 3', disabled=True)
        
        # Выбор материала
        self.material_spinner = Spinner(
            text='Выберите материал',
            values=list(MATERIALS.keys())
        )
        
        # Кнопка расчета
        self.calc_btn = Button(text='Рассчитать', disabled=True)
        self.calc_btn.bind(on_press=self.calculate)
        
        # Результаты
        self.result_label = Label(text='Результаты будут здесь', size_hint_y=2)
        
        # Добавление виджетов
        layout.add_widget(self.shape_spinner)
        layout.add_widget(self.param1)
        layout.add_widget(self.param2)
        layout.add_widget(self.param3)
        layout.add_widget(self.material_spinner)
        layout.add_widget(self.calc_btn)
        layout.add_widget(self.result_label)
        
        return layout
    
    def on_shape_select(self, spinner, text):
        self.param1.disabled = False
        self.param2.disabled = text != 'Параллелепипед'
        self.param3.disabled = text != 'Параллелепипед'
        
        self.param1.hint_text = 'Длина ребра' if text == 'Тетраэдр' else 'Радиус' if text == 'Шар' else 'Длина'
        self.param2.hint_text = 'Ширина'
        self.param3.hint_text = 'Высота'
        
        self.calc_btn.disabled = False
    
    def calculate(self, instance):
        try:
            material = self.material_spinner.text
            shape = self.shape_spinner.text
            
            if shape == 'Параллелепипед':
                a = float(self.param1.text)
                b = float(self.param2.text)
                c = float(self.param3.text)
                body = Parallelepiped(a, b, c, material)
            elif shape == 'Тетраэдр':
                a = float(self.param1.text)
                body = Tetrahedron(a, material)
            else:  # Шар
                r = float(self.param1.text)
                body = Sphere(r, material)
            
            result = (
                f"Фигура: {body}\n"
                f"Объем: {body.volume():.2f} м³\n"
                f"Площадь поверхности: {body.surface_area():.2f} м²\n"
                f"Масса: {body.mass():.2f} кг"
            )
            
            self.result_label.text = result
        
        except ValueError:
            self.result_label.text = "Ошибка: введите корректные числа"

if __name__ == '__main__':
    GeometryApp().run()