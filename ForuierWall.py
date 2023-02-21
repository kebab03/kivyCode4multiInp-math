import kivy

kivy.require('1.11.1')
import numpy as np
import matplotlib.pyplot as plt

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MyBoxLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        # self.cols = 4
        # self.orientation='vertical'
        self.cols = 2
        # Input widgets
        self.k_input = TextInput(text='0', multiline=False)
        self.L_input = TextInput(text='0', multiline=False)

        self.A_input = TextInput(text='0', multiline=False)

        # Output widgets
        self.sum_label = Label(text='Spessore: 0')
        self.product_label = Label(text='Product: 0')
        # ,size_hint_y=None, height=10, font_size=50)

        # Add widgets to layout
        self.add_widget(Label(text='Enter coeffi di condu  k:', pos_hint={'center_x': .7, 'center_y': .9}))
        self.add_widget(self.k_input)

        self.P_c_input = TextInput(text='0', multiline=False)
        self.add_widget(Label(text='Etr Spec P(W/m^2) :'))
        self.add_widget(self.P_c_input)

        self.add_widget(Label(text='Enter Lenth:'))
        self.add_widget(self.L_input)

        self.add_widget(Label(text='Enter Area:'))
        self.add_widget(self.A_input)

        self.dx_input = TextInput(text='0', multiline=False)
        self.add_widget(Label(text='wall dx:'))
        self.add_widget(self.dx_input)

        self.dt_input = TextInput(text='0', multiline=False)
        self.add_widget(Label(text='Enter dt:'))
        self.add_widget(self.dt_input)


        self.T_Fi_input = TextInput(text='0', multiline=False)
        self.add_widget(Label(text='Enter T_Fi:'))
        self.add_widget(self.T_Fi_input)


        self.t_end_input = TextInput(text='0', multiline=False)
        self.add_widget(Label(text='Enter t_end:'))
        self.add_widget(self.t_end_input)



        self.T0_input = TextInput(text='0', multiline=False)
        self.add_widget(Label(text='Enter T0_initial:'))
        self.add_widget(self.T0_input)


        self.T_in_input = TextInput(text='0', multiline=False)
        self.add_widget(Label(text='Enter T_intr= '))
        self.add_widget(self.T_in_input)




        self.add_widget(self.sum_label)
        self.add_widget(self.product_label)


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        # self.add_widget(Label(text='=p'))
        # self.add_widget(Button(text='=', on_press=self.calculateN))


class BottonLayout(BoxLayout):
    def __init__(self, my_box_layou3t, **kwargs):
        super(BottonLayout, self).__init__(**kwargs)
        self.my_box_layout = my_box_layou3t
        self.add_widget(Button(text='=', on_press=self.calculateN))
    # def calculate(self):
    #     # Get input values
    #     x = float(self.my_box_layout.k_input.text)
    #     y = float(self.my_box_layout.L_input.text)
    #     # Calculate sum and product
    #     s = x + y
    #     p = x * y
    #     # Update output labels
    #     self.my_box_layout.sum_label.text = 'Sum: {}'.format(s)
    #     self.my_box_layout.product_label.text = 'Product: {}'.format(p)
    def calculateN(self, button):
        # Get input values
        x = float(self.my_box_layout.k_input.text)
        y = float(self.my_box_layout.L_input.text)
        # Calculate sum and product
        s = x + y
        p = x * y

        k = float(self.my_box_layout.k_input.text)
        L = float(self.my_box_layout.L_input.text)

        P_c = float(self.my_box_layout.P_c_input.text)
        T0= float(self.my_box_layout.T0_input.text)

        T_in = float(self.my_box_layout.T_in_input.text)
        A = float(self.my_box_layout.A_input.text)
        sp = (T0-T_in)*k/P_c
        #        y = float(self.my_box_layout.L_input.text)
        # Update output labels
        self.my_box_layout.sum_label.text = 'Spessore: {}'.format(sp)
        self.my_box_layout.product_label.text = 'Product: {}'.format(p)


class MyApp(App):
    def build(self):
        main_layout = MainLayout(orientation='vertical')
        second_layout = MyBoxLayout()
        tird_layout = BottonLayout(second_layout)  # cui sto passando  MyBoxLayout() che
        # in 40 row stiamo dando al init function di class BottonLayout(BoxLayout)
        # per

        # Add the second layout to the main layout
        main_layout.add_widget(second_layout)
        main_layout.add_widget(tird_layout)
        return main_layout


if __name__ == '__main__':
    MyApp().run()
#
# class BottonLayout(BoxLayout):
#         def __init__(self, **kwargs):
#             super(BottonLayout, self).__init__(**kwargs)
#             # self.add_widget(Label(text='=p'))
#             self.add_widget(Button(text='=', on_press=self.calculateN))
#
#         def calculate(self):
#         # Get input values
#             x = float(self.x_input.text)
#             y = float(self.y_input.text)
#         #print("x:",x)
#         # Calculate sum and product
#             s = x + y
#             p = x * y
#         #print("s:" ,s)
#         # Update output labels
#             self.sum_label.text = 'Sum: {}'.format(s)
#             self.product_label.text = 'Product: {}'.format(p)
#
#         def calculateN(self, button):
#     # Get input values
#             x = float(self.x_input.text)
#             y = float(self.y_input.text)
#     # Calculate sum and product
#             s = x + y
#             p = x * y
#     # Update output labels
#             self.sum_label.text = 'Sum: {}'.format(s)
#             self.product_label.text = 'Product: {}'.format(p)
#
# class MyApp(App):
#     def build(self):
#
#
#         main_layout= MainLayout(orientation='vertical')
#         second_layout= MyBoxLayout()
#         tird_layout = BottonLayout (MyBoxLayout)
#         # Add the second layout to the main layout
#         main_layout.add_widget(second_layout)
#         main_layout.add_widget(tird_layout)
#         return main_layout
#
#
# if __name__ == '__main__':
#     MyApp().run()
