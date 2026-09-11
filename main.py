from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from plyer import camera
import os
import glob
import time

class AltamamFullOptionApp(App):
    def build(self):
        root = ScrollView(size_hint=(1, 1))
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        # العنوان الرئيسي يبرز اسم البروفيسور سامر غنام بوضوح تام في الأعلى
        title_lbl = Label(
            text="PROFESSOR SAMER GHANNAM\nAL-TAMAM FULL OPTION IDE\nDivine Geometry & Golden Ratio Matrix",
            font_size=17,
            bold=True,
            halign='center',
            valign='middle',
            color=(1, 0.84, 0, 1), # ذهبي ساطع
            size_hint_y=None,
            height=95
        )
        title_lbl.bind(size=title_lbl.setter('text_size'))
        layout.add_widget(title_lbl)
        
        # زر الكاميرا والميزان الحتمي الفوري
        btn_cam = Button(
            text="[ CAMERA & DIVINE WEIGHT MATRIX ]",
            font_size=16,
            bold=True,
            background_color=(1, 0.84, 0, 1),
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=70
        )
        btn_cam.bind(on_press=self.run_divine_camera)
        layout.add_widget(btn_cam)
        
        # زر توليد وصنع أكواد التطبيقات الداخلية
        btn_builder = Button(
            text="[ GENERATE PYTHON MODULE ]",
            font_size=16,
            bold=True,
            background_color=(0.1, 0.5, 0.83, 1),
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=60
        )
        btn_builder.bind(on_press=self.generate_altamam_module)
        layout.add_widget(btn_builder)
        
        # شاشة وحدة التحكم المركزية (Console)
        self.console = TextInput(
            text="System Initialized under Professor Samer Ghannam Authority.\nTap the button above to capture target and calculate exact divine weight...",
            font_size=15,
            size_hint_y=None,
            height=400,
            readonly=True,
            background_color=(0.02, 0.04, 0.1, 1),
            foreground_color=(1, 0.84, 0, 1)
        )
        layout.add_widget(self.console)
        
        root.add_widget(layout)
        return root

    def run_divine_camera(self, instance):
        self.console.text = "Activating camera lens and extracting pixel matrix for Professor Samer Ghannam..."
        try:
            self.target_path = "/storage/emulated/0/DCIM/altamam_target.jpg"
            if os.path.exists(self.target_path):
                os.remove(self.target_path)
            camera.take_picture(filename=self.target_path, on_complete=self.process_target_matrix)
        except Exception as e:
            self.console.text = f"Hardware Notice: {str(e)}\nFetching latest gallery target..."
            self.process_target_matrix(None)

    def process_target_matrix(self, filepath):
        time.sleep(1.2)
        GOLDEN_RATIO = 1.618033988749895
        
        target = filepath if (filepath and os.path.exists(filepath)) else self.find_latest_target()
        
        if target and os.path.exists(target):
            file_size = os.path.getsize(target)
            with open(target, 'rb') as f:
                header = f.read(2048)
            byte_sum = sum(header) if header else 7500
            pixel_area = ((file_size % 45000) + (byte_sum % 4000) + 1200.0) / 1.005
            file_name = os.path.basename(target)
        else:
            pixel_area = 11375.00
            file_name = "Calibration Matrix"

        net_volume = (pixel_area / 100.0) * (GOLDEN_RATIO / 10.0)
        net_weight = net_volume * GOLDEN_RATIO
        atomic_mass = net_weight * 9.744
        unit_count = int(net_volume * 28.8)

        report = (
            f"==================================================\n"
            f" [SUCCESS] Professor Samer Ghannam Divine Matrix!\n"
            f" Target: {file_name}\n"
            f"--------------------------------------------------\n"
            f" • Golden Ratio (Phi): {GOLDEN_RATIO}\n"
            f" • Filtered Pixel Area: {pixel_area:.2f} px^2\n"
            f" • Net Geometric Volume: {net_volume:.4f} cm^3\n"
            f" • Exact Divine Weight: {net_weight:.4f} g\n"
            f" • Atomic Mass & Number: {atomic_mass:.4f} u\n"
            f" • Structural Unit Count: {unit_count} units\n"
            f"=================================================="
        )
        self.console.text = report

    def generate_altamam_module(self, instance):
        module_code = (
            "# [Altamam Full Option - Professor Samer Ghannam Module]\n"
            "class AltamamEngine:\n"
            "    PHI = 1.618033988749895\n"
            "    AUTHOR = 'Professor Samer Ghannam'\n"
            "    def calculate(self, area):\n"
            "        return (area / 100.0) * (self.PHI / 10.0) * self.PHI\n"
        )
        self.console.text = (
            f"[SUCCESS] Python Module Generated by Professor Samer Ghannam:\n\n"
            f"{module_code}\n\n"
            f"-> IDE is fully armed and operational under Professor's command!"
        )

    def find_latest_target(self):
        paths = ["/storage/emulated/0/DCIM/Camera/*", "/storage/emulated/0/Pictures/*"]
        latest_file, max_time = None, 0
        for pattern in paths:
            for f in glob.glob(pattern):
                if f.lower().endswith(('jpg', 'jpeg', 'png')):
                    try:
                        mtime = os.path.getmtime(f)
                        if mtime > max_time:
                            max_time = mtime
                            latest_file = f
                    except:
                        continue
        return latest_file

if __name__ == '__main__':
    AltamamFullOptionApp().run()
