import ccxt, threading, time
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class QuantApp(App):
    def build(self):
        self.label = Label(text="正在连接欧易...", font_size="20sp", halign="center")
        threading.Thread(target=self.update_price, daemon=True).start()
        return self.label

    def update_price(self):
        e = ccxt.okx()
        last_p = 0
        while True:
            try:
                p = e.fetch_ticker("BTC/USDT")["last"]
                if last_p == 0:
                    text = f"初始价格: {p} USDT"
                else:
                    diff = p - last_p
                    if diff > 0:
                        text = f"涨了! 现价: {p} USDT\n(+{diff:.2f})"
                    else:
                        text = f"跌了! 现价: {p} USDT\n({diff:.2f})"
                last_p = p
                Clock.schedule_once(lambda dt, t=text: setattr(self.label, "text", t))
            except Exception as err:
                Clock.schedule_once(lambda dt: setattr(self.label, "text", "网络波动，重连中..."))
            time.sleep(3)

if __name__ == "__main__":
    QuantApp().run()
