from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from datetime import datetime
import os

from geometry.material import MATERIALS
from geometry.parallelepiped import calculate_volume as para_vol, calculate_surface_area as para_area, calculate_mass as para_mass
from geometry.sphere import calculate_volume as sphere_vol, calculate_surface_area as sphere_area, calculate_mass as sphere_mass
from geometry.tetrahedron import calculate_volume as tetra_vol, calculate_surface_area as tetra_area, calculate_mass as tetra_mass

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        
        self.shape_choice = Spinner(
            text='Выберите фигуру',
            values=['Параллелепипед', 'Шар', 'Тетраэдр'],
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.shape_choice)
        
        self.size1 = TextInput(hint_text='Размер 1', size_hint=(1, None), height=40)
        self.size2 = TextInput(hint_text='Размер 2', size_hint=(1, None), height=40, opacity=0)
        self.size3 = TextInput(hint_text='Размер 3', size_hint=(1, None), height=40, opacity=0)
        self.add_widget(self.size1)
        self.add_widget(self.size2)
        self.add_widget(self.size3)
        
        self.material = Spinner(
            text='Выберите материал',
            values=list(MATERIALS.keys()),
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.material)
        
        self.calc_btn = Button(text='Рассчитать', size_hint=(1, None), height=40)
        self.calc_btn.bind(on_press=self.calculate)
        self.add_widget(self.calc_btn)
        
        self.results = Label(text='Результаты появятся здесь')
        self.add_widget(self.results)
        
        self.save_btn = Button(text='Сохранить в файл', size_hint=(1, None), height=40)
        self.save_btn.bind(on_press=self.save_to_doc)
        self.add_widget(self.save_btn)
        
        self.shape_choice.bind(text=self.update_inputs)
        self.current_results = ""
    
    def update_inputs(self, spinner, text):
        if text == 'Параллелепипед':
            self.size1.hint_text = 'Длина (a)'
            self.size2.hint_text = 'Ширина (b)'
            self.size3.hint_text = 'Высота (c)'
            self.size2.opacity = 1
            self.size3.opacity = 1
        elif text == 'Шар':
            self.size1.hint_text = 'Радиус (r)'
            self.size2.opacity = 0
            self.size3.opacity = 0
        elif text == 'Тетраэдр':
            self.size1.hint_text = 'Длина ребра (a)'
            self.size2.opacity = 0
            self.size3.opacity = 0
    
    def calculate(self, instance):
        shape = self.shape_choice.text
        material = self.material.text
        
        if material not in MATERIALS:
            self.results.text = 'Ошибка: выберите материал'
            return
        
        try:
            if shape == 'Параллелепипед':
                a = float(self.size1.text)
                b = float(self.size2.text)
                c = float(self.size3.text)
                vol = para_vol(a, b, c)
                area = para_area(a, b, c)
                mass = para_mass(vol, MATERIALS[material])
            elif shape == 'Шар':
                r = float(self.size1.text)
                vol = sphere_vol(r)
                area = sphere_area(r)
                mass = sphere_mass(vol, MATERIALS[material])
            elif shape == 'Тетраэдр':
                a = float(self.size1.text)
                vol = tetra_vol(a)
                area = tetra_area(a)
                mass = tetra_mass(vol, MATERIALS[material])
            
            self.current_results = f"""Результаты для {shape} из {material}:
Объем: {vol:.2f} м³
Площадь: {area:.2f} м²
Масса: {mass:.2f} кг"""
            
            self.results.text = self.current_results
        except:
            self.results.text = 'Ошибка: проверьте введенные размеры'
    
    def save_to_doc(self, instance):
        if not self.current_results:
            self.results.text = 'Сначала выполните расчет'
            return
        
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filename = datetime.now().strftime("results_%Y-%m-%d_%H-%M-%S.doc")
            filepath = os.path.join(script_dir, filename)
            
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            file_content = f"Отчет создан: {now}\n\n{self.current_results}"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(file_content)
            
            self.results.text = f"Файл успешно сохранен:\n{filename}"
        except Exception as e:
            self.results.text = f"Ошибка при сохранении файла:\n{str(e)}"

class GeometryApp(App):
    def build(self):
        self.title = 'Калькулятор геометрических тел'
        return MainScreen()

if __name__ == '__main__':
    GeometryApp().run()