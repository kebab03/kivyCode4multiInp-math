from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class InputScreen(Screen):
    input_number1 = ObjectProperty(None)
    input_number2 = ObjectProperty(None)

    def submit(self):
        number1 = int(self.input_number1.text)
        number2 = int(self.input_number2.text)
        app = App.get_running_app()
        app.root.get_screen('output').generate_input_boxes(number1, number2)
        app.root.current = 'output'

class OutputScreen(Screen):
    inputs_layout1 = ObjectProperty(None)
    inputs_layout2 = ObjectProperty(None)
    math_operation = ObjectProperty(None)

    def generate_input_boxes(self, number1, number2):
        self.inputs_layout1.clear_widgets()
        self.inputs_layout2.clear_widgets()
        for i in range(number1):
            label1 = Label(text=f'Input {i+1}')
            input_box1 = TextInput(hint_text=f'MInput {i + 1}')
            box1 = BoxLayout()
            box1.add_widget(label1)
            box1.add_widget(input_box1)
            self.inputs_layout1.add_widget(box1)

        for i in range(number2):
            label2 = Label(text=f'Input {i+1}')
            input_box2 = TextInput(hint_text=f'Input {i + 1}')
            box2 = BoxLayout()
            box2.add_widget(label2)
            box2.add_widget(input_box2)
            self.inputs_layout2.add_widget(box2)

    def calculate_math_operation(self):
        values1 = [float(child.text) for child in self.inputs_layout1.children if isinstance(child, TextInput)]
        values2 = [float(child.text) for child in self.inputs_layout2.children if isinstance(child, TextInput)]
        print("values1:", values1)
        print("values2:", values2)
        if self.math_operation.text == '+':
            result = sum(values1) + sum(values2)
        elif self.math_operation.text == '-':
            result = sum(values1) - sum(values2)
        elif self.math_operation.text == '*':
            result = sum(values1) * sum(values2)
        elif self.math_operation.text == '/':
            result = sum(values1) / sum(values2)
        else:
            result = None

        self.ids.result_label.text = f"Result: {result}"


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
        orientation: 'vertical'
        Label:
            text: 'Enter the input values for First Input:'
        ScrollView:
            BoxLayout:
                id: inputs_layout1_id
                orientation: 'vertical'
        Label:
            text: 'Enter the input values for Second Input:'
        ScrollView:
            BoxLayout:
                id: inputs_layout2_id
                orientation: 'vertical'
        Label:
            text: 'Choose math operation:'
        Spinner:
            id: math_operation_id
            values: ['+', '-', '*', '/']
        Button:
            text: 'Calculate'
            on_press: root.calculate_math_operation()
        Label:
            id: result_label
            text: 'Result: '

''')

class MyApp(App):

    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()