# Gerekli kütüphaneler
import sys
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QSlider, QPushButton
)
from PyQt5.QtCore import Qt

# ========== Bulanık Mantık Tanımlamaları ==========

# Girdiler
sicaklik = ctrl.Antecedent(np.arange(0, 41, 1), 'sicaklik')
nem = ctrl.Antecedent(np.arange(0, 101, 1), 'nem')
co2 = ctrl.Antecedent(np.arange(300, 2001, 1), 'co2')
isik = ctrl.Antecedent(np.arange(0, 1001, 1), 'isik')
kisi = ctrl.Antecedent(np.arange(0, 11, 1), 'kisi')

# Çıktılar
isitici = ctrl.Consequent(np.arange(0, 101, 1), 'isitici')
havalandirma = ctrl.Consequent(np.arange(0, 101, 1), 'havalandirma')

# Üyelik fonksiyonları otomatik (düşük, orta, yüksek)
sicaklik.automf(3)
nem.automf(3)
co2.automf(3)
isik.automf(3)
kisi.automf(3)

isitici.automf(3)
havalandirma.automf(3)

# Kurallar
rules = [
    ctrl.Rule(sicaklik['poor'] & kisi['good'], isitici['good']),
    ctrl.Rule(co2['good'] & nem['good'], havalandirma['good']),
    ctrl.Rule(co2['average'], havalandirma['average']),
    ctrl.Rule(sicaklik['good'], isitici['poor']),
    ctrl.Rule(kisi['poor'] & sicaklik['average'], isitici['average']),
    ctrl.Rule(isik['poor'] & co2['good'], havalandirma['average'])  # YENİ KURAL
]


# Kontrol sistemi
kontrol = ctrl.ControlSystem(rules)
sim = ctrl.ControlSystemSimulation(kontrol)

# Hesaplama fonksiyonu
def hesapla(sic, n, c, i, k):
    sim.input['sicaklik'] = sic
    sim.input['nem'] = n
    sim.input['co2'] = c
    sim.input['isik'] = i
    sim.input['kisi'] = k
    sim.compute()
    return sim.output['isitici'], sim.output['havalandirma']

# ========== PyQt5 Arayüz ==========

class FuzzyApp(QWidget):
    def __init__(self):  # DÜZELTİLDİ
        super().__init__()  # DÜZELTİLDİ
        self.setWindowTitle("Akıllı Oda Isıtma ve Havalandırma Kontrolü")
        self.layout = QVBoxLayout()

        # Girdi sliderları
        self.sliders = {}
        self.labels = {}

        girdiler = {
            'Sıcaklık (0-40°C)': (0, 40),
            'Nem (0-100%)': (0, 100),
            'CO2 (300-2000 ppm)': (300, 2000),
            'Işık (0-1000 lux)': (0, 1000),
            'Kişi Sayısı (0-10)': (0, 10),
        }

        for name, (min_val, max_val) in girdiler.items():
            label = QLabel(f"{name}: {min_val}")
            slider = QSlider(Qt.Horizontal)
            slider.setMinimum(min_val)
            slider.setMaximum(max_val)
            slider.setValue(min_val)
            slider.valueChanged.connect(lambda val, l=label, n=name: l.setText(f"{n}: {val}"))
            self.layout.addWidget(label)
            self.layout.addWidget(slider)
            self.sliders[name] = slider
            self.labels[name] = label

        # Hesapla butonu ve sonuç etiketi
        self.button = QPushButton("Hesapla")
        self.button.clicked.connect(self.hesapla)
        self.result = QLabel("Sonuç: Isıtıcı ve Havalandırma değerleri burada görünecek.")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.result)
        self.setLayout(self.layout)

    def hesapla(self):
        s = self.sliders['Sıcaklık (0-40°C)'].value()
        n = self.sliders['Nem (0-100%)'].value()
        c = self.sliders['CO2 (300-2000 ppm)'].value()
        i = self.sliders['Işık (0-1000 lux)'].value()
        k = self.sliders['Kişi Sayısı (0-10)'].value()
        isitici, havalandirma = hesapla(s, n, c, i, k)
        self.result.setText(
            f"Isıtıcı Gücü: %{isitici:.1f} | Havalandırma Seviyesi: %{havalandirma:.1f}"
        )

# ========== Uygulamayı Başlat ==========

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = FuzzyApp()
    pencere.show()
    sys.exit(app.exec_())
