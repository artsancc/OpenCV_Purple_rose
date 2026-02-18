# OpenCV_Purple_rose

Görüntü işleme (Computer Vision) öğrenme sürecimde yaptığım bu projede, bir görseldeki nesneyi arka plandan ayırmayı ve rengini değiştirmeyi denedim.
Bu kod; kırmızı bir gülü alıyor, renk uzay dönüşümleri kullanarak maske oluşturuyor, Morfolojik İşlemler (Kernel, Closing) ile maskeyi pürüzsüzleştiriyor ve son olarak gülün rengini mora çeviriyor.


# Projenin Amacı
BGR formatındaki renk karmaşasını aşarak, rengi (Hue) parlaklıktan (Value) ayırıp daha hassas tespit yapmak.

Çoklu Maske Birleştirme

Morfolojik işlemler (Kernel) ile gürültü temizlemek ve maske iyileştirmek.

Piksel Bazlı Manipülasyon ile boyama yapmak.


# Teknik İşleyiş ve Kod Mantığı

1.Maskeleme
Kırmızı renk, HSV renk çemberinin hem başında hem sonunda yer aldığı için tek bir aralık yeterli olmaz. Kodda iki ayrı maske oluşturulmuştur ve bu maskeler cv2.bitwise_or kullanılarak tek bir rose_mask içerisinde toplanmıştır.


2.Gürültü Temizleme

Maske oluşturulurken eklenemeyen gölge alanları maskeye dahil edebilmek için:

Kernel Tanımlama: (9,7) boyutunda bir matris ile tarama yapılarak pikseller gruplanmıştır.

Morphology (Closing): Gül üzerindeki gölgelerden kaynaklanan küçük siyah delikler bu işlemle kapatılmıştır.

Gaussian Blur: Maskenin kenarları hafifçe bulanıklaştırılarak, renk değişiminin orijinal resimle "keskin" durması yerine daha doğal kaynaşması sağlanmıştır.


3.Dijital Renk Değişimi
Sadece maskenin olduğu piksellerin Hue (Renk Tonu) kanalı hedef renk olan 145 (Mor) değerine atanmıştır.

# Kullanılan Kütüphaneler

Projeyi çalıştırmak için şu kütüphanelere ihtiyacınız var:

Python 3

OpenCV (cv2)

NumPy

Gerekli kütüphaneleri indirin:

pip install opencv-python numpy

Proje klasörüne rose.jpeg adında bir görsel ekleyin (veya kod içindeki dosya adını değiştirin).

Kodu çalıştırın.

#Input
![rose](https://github.com/user-attachments/assets/704118f9-ffea-4dc1-ae8c-84328170cd87)

#Output
<img width="1000" height="667" alt="maske" src="https://github.com/user-attachments/assets/dfb8164d-9844-458b-bb2b-4f90f15681e5" />
<img width="1000" height="667" alt="sonuc" src="https://github.com/user-attachments/assets/67bd23f8-c358-47f2-8936-6acba5851270" />

# Sonuç
Arka plan karartılır ve sadece rengi değiştirilmiş, temizlenmiş gül ekrana yansıtılır.

