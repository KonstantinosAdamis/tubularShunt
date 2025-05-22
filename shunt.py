from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from math import pi, sqrt, atan, degrees, log10
from kivy.core.window import Window

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.r_input = TextInput(hint_text='Enter R (mΩ)', input_filter='float', multiline=False)
        self.l_input = TextInput(hint_text='Enter L (pH)', input_filter='float', multiline=False)
        self.f_input = TextInput(hint_text='Enter f (Hz)', input_filter='float', multiline=False)

        self.magnitude_label = Label(text='Magnitude (dB) will appear here')
        self.phase_label = Label(text='Phase (degrees) will appear here')
        self.bandwidth_label = Label(text='Bandwidth (Hz) will appear here')

        calc_button = Button(text='Calculate')
        calc_button.bind(on_press=self.calculate)

        self.add_widget(self.r_input)
        self.add_widget(self.l_input)
        self.add_widget(self.f_input)
        self.add_widget(calc_button)
        self.add_widget(self.magnitude_label)
        self.add_widget(self.phase_label)
        self.add_widget(self.bandwidth_label)

    def calculate(self, instance):
        try:
            R_mohm = float(self.r_input.text)
            L_ph = float(self.l_input.text)
            f = float(self.f_input.text)

            R = R_mohm * 1e-3
            L = L_ph * 1e-12
            omega = 2 * pi * f

            magnitude = R**2 / sqrt(4 * R**2 + (omega * L)**2)
            magnitude_db = 20 * log10(magnitude)
            phi_deg = degrees(atan(-omega * L / (2 * R)))
            bandwidth = R / (pi * L)

            self.magnitude_label.text = f"Magnitude: {magnitude_db:.2f} dB"
            self.phase_label.text = f"Phase: {phi_deg:.4f}°"
            self.bandwidth_label.text = f"Bandwidth: {bandwidth:.2f} Hz"

        except ValueError:
            self.magnitude_label.text = "Invalid input."
            self.phase_label.text = ""
            self.bandwidth_label.text = ""

class TubularShuntApp(App):
    def build(self):
        Window.title = "Tubular Shunt"
        return CalculatorLayout()

if __name__ == '__main__':
    TubularShuntApp().run()