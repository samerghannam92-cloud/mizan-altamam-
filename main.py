from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class MizanAltamamAdvancedApp(App):
    def build(self):
        self.title = "ساعة التمام الشاملة - الهندسة الإلهية"
        root = ScrollView(size_hint=(1, 1))
        
        main_layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=15,
            size_hint_y=None
        )
        main_layout.bind(minimum_height=main_layout.setter('height'))

        # الترويسة الرئيسية للمشروع
        header = Label(
            text="[b]البروفيسور سامر سلمان غنام[/b]\nخوارزمية ساعة التمام الشاملة والإسقاط الهندسي\n[i]Divine Geometry & Golden Ratio Matrix[/i]",
            markup=True,
            font_size=15,
            halign="center",
            valign="middle",
            color=(1.0, 0.84, 0.0, 1), # لون ذهبي مهيب
            size_hint_y=None,
            height=120
        )
        header.bind(size=header.setter('text_size'))
        main_layout.add_widget(header)

        # لوحة ثوابت الهندسة الإلهية والنسبة الذهبية
        phi = 1.618033988749895
        constants_text = (
            f"• الثابت الذهبي (Phi): {phi}\n"
            f"• زاوية الإسقاط الهندسي: 137.508° (الزاوية المقدسة)\n"
            f"• النظام: التمام الشامل - معايرة زمن البناء المطلق"
        )
        const_lbl = Label(
            text=constants_text,
            font_size=13,
            halign="center",
            valign="middle",
            color=(0.9, 0.9, 0.9, 1),
            size_hint_y=None,
            height=90
        )
        const_lbl.bind(size=const_lbl.setter('text_size'))
        main_layout.add_widget(const_lbl)

        # صندوق إدخال المقياس أو البعد الهندسي
        input_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=55, spacing=10)
        
        self.input_dim = TextInput(
            text='1000',
            multiline=False,
            font_size=16,
            halign='center',
            size_hint_x=0.6
        )
        lbl_dim = Label(
            text="المقياس الأساسي:",
            font_size=13,
            color=(1, 1, 1, 1),
            size_hint_x=0.4,
            halign="right"
        )
        lbl_dim.bind(size=lbl_dim.setter('text_size'))
        
        input_box.add_widget(self.input_dim)
        input_box.add_widget(lbl_dim)
        main_layout.add_widget(input_box)

        # شاشة عرض مخرجات الإسقاط والتحليل
        self.result_lbl = Label(
            text="اضغط الزر أدناه لتفعيل خوارزمية الإسقاط الهندسي...",
            font_size=13,
            halign="center",
            valign="middle",
            color=(0.0, 1.0, 0.8, 1),
            size_hint_y=None,
            height=150
        )
        self.result_lbl.bind(size=self.result_lbl.setter('text_size'))
        main_layout.add_widget(self.result_lbl)

        # زر التشغيل والمعايرة المطلقة
        calc_btn = Button(
            text="تشغيل مصفوفة ساعة التمام والإسقاط",
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.5, 0.8, 1)
        )
        calc_btn.bind(on_press=self.calculate_projection)
        main_layout.add_widget(calc_btn)

        root.add_widget(main_layout)
        return root

    def calculate_projection(self, instance):
        try:
            base_val = float(self.input_dim.text)
        except ValueError:
            base_val = 1000.0

        phi = 1.618033988749895
        p_sub = base_val / phi
        p_sup = base_val * phi
        p_grand = base_val * (phi ** 2)
        
        output_str = (
            f"=== مصفوفة الإسقاط الهندسي الشامل ===\n"
            f"القيمة المرصودة: {base_val}\n"
            f"• الإسقاط الأدنى (÷ Phi): {p_sub:.3f}\n"
            f"• الإسقاط الأعلى (× Phi): {p_sup:.3f}\n"
            f"• المدى الكلي للتمام (× Phi²): {p_grand:.3f}\n"
            f"حالة النظام: متوافق مع النسبة الذهبية ومنضبط."
        )
        self.result_lbl.text = output_str

if __name__ == '__main__':
    MizanAltamamAdvancedApp().run()
  
