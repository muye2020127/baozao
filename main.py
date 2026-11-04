from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class QuantApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        title = Label(text="🚀 暴躁小海量化终端", font_size='24sp', color=(0,1,0,1))
        price = Label(text="BTC: 78,600 USDT\n(+1.16%)", font_size='40sp', color=(0,1,0,1))
        btn = Button(text="启动量化机器人", size_hint=(1, 0.2), background_color=(0,1,0,1))
        
        layout.add_widget(title)
        layout.add_widget(price)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    QuantApp().run()
