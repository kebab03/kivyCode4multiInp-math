from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.core.window import Window

class InputScreen(Screen):
    input_number1 = ObjectProperty(None)
    input_number2 = ObjectProperty(None)

    def submit(self):
        try:
            number1 = int(self.input_number1.text)
            number2 = int(self.input_number2.text)
            app = App.get_running_app()
            app.root.get_screen('output').generate_input_boxes(number1, number2)
            app.root.current = 'output'
        except ValueError:
            self.input_number1.text = ""
            self.input_number2.text = ""
            self.input_number1.hint_text = "Please enter a valid number"
            self.input_number2.hint_text = "Please enter a valid number"

class OutputScreen(Screen):
    inputs_layout1 = ObjectProperty(None)
    inputs_layout2 = ObjectProperty(None)
    math_operation = ObjectProperty(None)

    def generate_input_boxes(self, number1, number2):
        self.inputs_layout1.clear_widgets()
        self.inputs_layout2.clear_widgets()
        for i in range(number1):
            input_box1 = TextInput(hint_text=f'Input {i + 1}')
            self.inputs_layout1.add_widget(input_box1)

        for i in range(number2):
            input_box2 = TextInput(hint_text=f'Input {i + 1}')
            self.inputs_layout2.add_widget(input_box2)

    def calculate_math_operation(self):
        values1 = self.get_input_values(self.inputs_layout1)
        values2 = self.get_input_values(self.inputs_layout2)
        print("values1:", values1)
        print("values2:", values2)
        operation = self.math_operation.text
        result = self.perform_math_operation(values1, values2, operation)
        self.ids.result_label.text = f"Result: {result}"

    def get_input_values(self, inputs_layout):
        return [float(child.text) for child in inputs_layout.children]

    def perform_math_operation(self, values1, values2, operation):
        operations = {'+': lambda x, y: x + y,
                      '-': lambda x, y: x - y,
                      '*': lambda x, y: x * y,
                      '/': lambda x, y: x / y if y != 0 else None}
        function = operations.get(operation)
        if function:
            return function(sum(values1), sum(values2))
        else:
            return None

class WindowManager(ScreenManager):
    pass

kv = Builder.load_string('''
WindowManager:
    InputScreen:
    OutputScreen:

<InputScreen>:
    name: 'input'
    input_number1: input_number1_id
    input_number2: input_number2_id
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter the number of input boxes for First Input:'
        TextInput:
            id: input_number1_id
            multiline: False
        Label:
            text: 'Enter the number of input boxes for Second Input:'
        TextInput:
            id: input_number2_id
            multiline: False
        Button:
            text: 'Submit'
            on_press: root.submit()
<OutputScreen>:
    name: 'output'
    inputs_layout1: inputs_layout1_id
    inputs_layout2: inputs_layout2_id
    math_operation: math_operation_id
    BoxLayout:
        size_hint: 1, 1
        orientation: 'vertical'
        Label:
            size_hint: 1, 0.6
            text: 'Enter the input values for First Input:'
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                id: inputs_layout1_id
                orientation: 'vertical'
        Label:
            size_hint: 1, 0.6
            text: 'Enter the input values for Second Input:'
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                id: inputs_layout2_id
                orientation: 'vertical'
        Label:
            size_hint: 1, 0.6
            text: 'Choose math operation:'
        Spinner:
            id: math_operation_id
            values: ['+', '-', '*', '/']
        Button:
            size_hint: 1, 0.6
            text: 'Calculate'
            on_press: root.calculate_math_operation()
        Label:
            id: result_label
            text: 'Result: '

''')

class MyApp(App):

    def build(self):
        Window.size = (600, 700)  # set the window size to 400x600
        return kv


if __name__ == '__main__':
    MyApp().run()