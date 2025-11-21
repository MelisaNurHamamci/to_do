# 📝 Django To-Do App

Bu proje, **Python** ve **Django** framework'ü kullanılarak geliştirilmiş basit ve etkili bir "Yapılacaklar Listesi" (To-Do List) uygulamasıdır. Kullanıcıların günlük görevlerini ekleyebileceği, takip edebileceği ve yönetebileceği bir arayüz sunar.

## 🚀 Özellikler

* **Görev Ekleme:** Yeni yapılacak maddeleri veritabanına kaydetme.
* **Listeleme:** Eklenen tüm görevleri görüntüleme.
* **Tamamlandı İşaretleme:** Yapılan görevlerin durumunu güncelleme.
* **Silme:** Gereksiz veya bitmiş görevleri listeden kaldırma.
* **Admin Paneli:** Django admin paneli üzerinden tam kontrol.

## 🛠️ Kullanılan Teknolojiler

* **Backend:** Python 3, Django
* **Veritabanı:** SQLite (Varsayılan)
* **Frontend:** HTML, CSS (Template yapısı)

## 💻 Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  **Projeyi klonlayın:**
    ```bash
    git clone [https://github.com/MelisaNurHamamci/to_do.git](https://github.com/MelisaNurHamamci/to_do.git)
    ```

2.  **Sanal ortamı kurun ve aktif edin:**
    ```bash
    python -m venv venv
    # Windows için:
    .\venv\Scripts\activate
    ```

3.  **Gereksinimleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Veritabanını oluşturun:**
    ```bash
    python manage.py migrate
    ```

5.  **Sunucuyu başlatın:**
    ```bash
    python manage.py runserver
    ```

Tarayıcınızda `http://127.0.0.1:8000/` adresine giderek uygulamayı görebilirsiniz.

---
