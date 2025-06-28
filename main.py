from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class CardLogger(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.card_input = TextInput(hint_text="💳 Karta raqami")
        self.expiry_input = TextInput(hint_text="📅 Amal qilish muddati (MM/YY)")
        self.cvv_input = TextInput(hint_text="🔐 CVV kodi", password=True)

        self.add_widget(self.card_input)
        self.add_widget(self.expiry_input)
        self.add_widget(self.cvv_input)

        submit_btn = Button(text="Tasdiqlash")
        submit_btn.bind(on_press=self.log_info)
        self.add_widget(submit_btn)

        self.output_label = Label()
        self.add_widget(self.output_label)

    def log_info(self, instance):
        card = self.card_input.text
        expiry = self.expiry_input.text
        cvv = self.cvv_input.text
        info = f"Karta: {card}\nMuddati: {expiry}\nCVV: {cvv}"
        print(info)
        self.output_label.text = f"[TEST] Ma'lumotlar loglandi!"

class TestApp(App):
    def build(self):
        return CardLogger()

if __name__ == '__main__':
    TestApp().run()
