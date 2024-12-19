# DijitalImageProcessing# Görüntü İşleme Programı

Bu Python programı, OpenCV ve NumPy kullanarak çeşitli görüntü işleme işlevleri sağlar. Aşağıda mevcut işlevlerin bir özeti ve nasıl kullanılacağı açıklanmaktadır.

## Özellikler

1. **Tuz ve Karabiber Gürültüsü Ekleme**  
   Görüntüye rastgele beyaz (tuz) ve siyah (karabiber) gürültü ekler.
   - **Kullanım:** Gürültü giderme algoritmalarını test etmek için gürültülü görüntüler simüle eder.
   - **Varsayılan Gürültü Miktarı:** Görüntü piksellerinin %2'si.

2. **Gauss Filtresi Uygulama**  
   Görüntüye Gauss bulanıklığı uygulayarak gürültüyü azaltır ve görüntüyü yumuşatır.
   - **Çekirdek Boyutu:** 5x5.

3. **Medyan Filtresi Uygulama**  
   Gri tonlamalı görüntülerdeki gürültüyü, her bir piksel değerini komşuluğundaki medyan ile değiştirerek azaltır.
   - **Çekirdek Boyutu:** 5x5.

4. **Görüntüyü Bulanıklaştırma**  
   Görüntüye basit bir ortalama filtre uygular ve bulanıklaştırır.
   - **Çekirdek Boyutu:** 5x5.

5. **Görüntü Boyutlandırma**  
   Görüntüyü orijinal boyutunun belirli bir yüzdesine yeniden boyutlandırır.
   - **Girdi:** Ölçek yüzdesi (örneğin, %50 için 50).

6. **Görüntüyü Yeniden Renklendirme**  
   Görselleştirme için görüntünün gri tonlamalı bir sürümüne bir renk haritası (JET) uygular.
   - **Renk Haritası:** COLORMAP_JET.

7. **Görüntü Kırpma**  
   Kullanıcı tarafından belirlenen koordinatlar ve boyutlara göre görüntüden dikdörtgen bir alan çıkarır.
   - **Girdi:** Başlangıç koordinatları (x, y) ve boyutlar (genişlik, yükseklik).

## Nasıl Kullanılır

1. **Gerekli Kütüphaneleri Kurun:**
   - OpenCV, NumPy ve Matplotlib kütüphanelerinin yüklü olduğundan emin olun. Şu komutla kurabilirsiniz:
     ```bash
     pip install opencv-python numpy matplotlib
     ```

2. **Programı Çalıştırın:**
   - Betiği bir `.py` dosyasına kaydedin ve çalıştırın. Örneğin:
     ```bash
     python image_processing.py
     ```

3. **Menü Talimatlarını Takip Edin:**
   - Menüden istenen işlevi seçmek için ilgili numarayı girin.
   - Gerekirse ek girdiler sağlayın (örneğin, yeniden boyutlandırma için ölçek yüzdesi veya kırpma koordinatları).

4. **Bir Görüntü Yükleyin:**
   - Betikteki görüntü dosyası yolunun doğru olduğundan emin olun. Yer tutucu yolu kendi görüntü yolunuzla değiştirebilirsiniz:
     ```python
     image_path = r"C:\Users\bingl\Downloads\pexels-flowerstofox-27082077.jpg"
     ```

5. **Sonuçları Görüntüleyin:**
   - Orijinal ve işlenmiş görüntüler Matplotlib kullanılarak yan yana gösterilecektir.

## Örnekler

### Tuz ve Karabiber Gürültüsü Ekleme
- **Orijinal:** Yüklenen görüntünün gri tonlamalı sürümü.
- **İşlenmiş:** Tuz ve karabiber gürültüsü eklenmiş görüntü.

### Görüntü Boyutlandırma
- **Orijinal:** Tam boyutlu yüklenen görüntü.
- **İşlenmiş:** Kullanıcı tarafından belirtilen yüzdeye göre yeniden boyutlandırılmış görüntü.

## Notlar
- Program hem renkli hem de gri tonlamalı görüntüleri işleyebilir.
- Görüntü dosyasının belirtilen yolda mevcut olduğundan emin olun; aksi takdirde program bir hata mesajıyla sonlanır.
- Belirli kullanım durumları için çekirdek boyutlarını ve diğer parametreleri kodda gerektiği gibi ayarlayın.

## Teşekkürler
Bu program, görüntü işleme için güçlü OpenCV kütüphanesinden ve görselleştirme için Matplotlib'den yararlanır.

