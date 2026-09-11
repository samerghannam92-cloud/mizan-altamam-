from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class MizanAltamamApp(App):
    def build(self):
        root = ScrollView(size_hint=(1, 1))
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # العنوان الرئيسي والتعريف الهندسي
        title_lbl = Label(
            text="PROFESSOR SAMER GHANNAM\nMIZAN AL-TAMAM FULL OPTION\nDivine Geometry & Golden Ratio Matrix",
            font_size=16,
            bold=True,
            halign="center",
            valign="middle",
            color=(1, 0.84, 0, 1),
            size_hint_y=None,
            height=110
        )
        title_lbl.bind(size=title_lbl.setter('text_size'))
        layout.add_widget(title_lbl)

        # خوارزمية النسبة الذهبية
        phi = 1.618033988749895
        ratio_lbl = Label(
            text=f"Golden Ratio (Phi): {phi}\nAbsolute Hour Protocol Active",
            font_size=14,
            halign="center",
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=70
        )
        ratio_lbl.bind(size=ratio_lbl.setter('text_size'))
        layout.add_widget(ratio_lbl)

        # زر المعايرة المباشر
        def calibrate(instance):
            instance.text = f"تمت المعايرة الهندسية بنجاح (Phi = {phi})"

        btn = Button(
            text="بدء معايرة ميزان التمام",
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.6, 0.8, 1)
        )
        btn.bind(on_press=calibrate)
        layout.add_widget(btn)

        root.add_widget(layout)
        return root

if __name__ == '__main__':
    MizanAltamamApp().run()
  
