# Oda Kontrol Sistemi

 Bu projenin amacı, bir odadaki çevresel faktörlere göre ısıtma ve havalandırma sistemini otomatik olarak ayarlayan akıllı bir kontrol sistemi geliştirmektir. Geliştirilen sistem, sıcaklık, nem, karbondioksit (CO₂) seviyesi, ışık miktarı ve odadaki kişi sayısı gibi beş farklı girdi parametresini dikkate alarak, istenilen ortam konforunu sağlayacak şekilde ısıtıcı gücünü ve havalandırma seviyesini ayarlamaktadır.

Bu sistem, klasik koşullu yapılar yerine insan benzeri kararlar verebilen bulanık mantık (fuzzy logic) algoritması kullanılarak geliştirilmiştir. Projede ayrıca kullanıcı dostu bir arayüz aracılığıyla kullanıcıların değerleri kolayca girmesi ve çıktıları görmesi sağlanmıştır.

#Kullanılan Yazılım ve Kütüphaneler
Python 3.10: Programlama dili

scikit-fuzzy: Bulanık mantık işlemleri için

PyQt5: Grafik arayüz tasarımı için

NumPy: Sayısal işlemler için

![giris](https://github.com/user-attachments/assets/d78dcc5b-b7e9-46c4-9020-9b6b23356934)

İstenilen verileri aşağıdaki gibi girip sonucu göreceğiz.

Sıcaklık=5

Nem=19

CO2=467

Işık=172

Kişi Sayısı=4

![sonuc](https://github.com/user-attachments/assets/c32c1a53-791d-43a2-9482-b7524a582d24)

Sonuç olarak;

Isıtıcı Gücü=%50.0

Havalandırma seviyesi= %50.0  

olarak bulunmuştur.




