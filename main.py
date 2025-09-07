from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase

# ודא שהקובץ NotoSansHebrew-Regular.ttf נמצא ליד הקובץ הזה
LabelBase.register(name="NotoHeb", fn_regular="NotoSansHebrew-Regular.ttf")

class MyApp(App):
    def build(self):
        return Label(text="שלום אנדרואיד!", font_name="NotoHeb", font_size="32sp")

if __name__ == "__main__":
    MyApp().run()
